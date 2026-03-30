import allure
import pytest
import requests
from test_data import CourierData 
from courier_helpers import register_new_courier_and_return_login_password
from api.courier_api import CourierApi
from conftest import BASE_URL

class ErrorMessages:
    LOGIN_ALREADY_USED = "Этот логин уже используется"
    INSUFFICIENT_DATA = "Недостаточно данных для создания учетной записи"

@allure.feature("Создание курьера")
class TestCreateCourier:
    
    @allure.title("Позитивный тест: создание курьера")
    @allure.description("Проверяем, что курьера можно успешно создать")
    def test_create_courier_success(self):
        courier_api = CourierApi(BASE_URL)
        result  = register_new_courier_and_return_login_password()
        assert result, "Курьер должен быть создан"
        assert len(result) == 4
       
        login, password, first_name, create_response = result
        
        # Проверяем ответ на создание
        assert create_response.status_code == 201
        assert create_response.json() == {"ok": True}
        
        courier_api.delete_courier_by_credentials(login, password)

    @allure.title("Негативный тест: создание дубликата курьера")
    @allure.description("Проверяем, что нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self):
        courier_api = CourierApi(BASE_URL)
        result = register_new_courier_and_return_login_password()
        assert result, "Не удалось создать первого курьера"
        
        login, password, first_name, create_response = result
        
        payload = CourierData.valid_courier_data()
        payload["login"] = login
        payload["password"] = password
        payload["firstName"] = first_name
        
        create_response = courier_api.create_courier(payload)
        
        assert create_response.status_code == 409
        assert ErrorMessages.LOGIN_ALREADY_USED in create_response.text
        
        courier_api.delete_courier_by_credentials(login, password)
       
    @allure.title("Негативный тест: создание курьера без обязательных полей")
    @pytest.mark.parametrize("payload,expected_message", [
        (
            CourierData.courier_without_login(),
            ErrorMessages.INSUFFICIENT_DATA
        ),
        (
            CourierData.courier_without_password(),
            ErrorMessages.INSUFFICIENT_DATA
        ),
        (
            CourierData.courier_without_firstname(),
            ErrorMessages.INSUFFICIENT_DATA
        ),
    ])
    def test_create_courier_missing_fields(self, payload, expected_message):
        response = requests.post(
            f"{BASE_URL}/api/v1/courier",
            json=payload
        )
        
        assert response.status_code == 400
        assert expected_message in response.text
    
    @allure.title("Негативный тест: создание курьера с уже существующим логином")
    @allure.description("Проверяем, что если создать пользователя с логином, который уже есть, возвращается ошибка")
    def test_create_courier_existing_login(self):
        courier_data = register_new_courier_and_return_login_password()
        assert courier_data, "Не удалось создать первого курьера"
        
        login = courier_data[0]
        
        payload = CourierData.courier_with_existing_login(login)
        
        response = requests.post(
            f"{BASE_URL}/api/v1/courier",
            json=payload
        )
        
        assert ErrorMessages.LOGIN_ALREADY_USED in response.text
    