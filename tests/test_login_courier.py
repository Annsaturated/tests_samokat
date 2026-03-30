import allure
import pytest
import requests
from test_data import CourierData
from courier_helpers import register_new_courier_and_return_login_password
from api.courier_api import CourierApi
from conftest import BASE_URL

class ErrorMessages:
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"

@allure.feature("Логин курьера")
class TestLoginCourier:
    
    @allure.title("Позитивный тест: успешная авторизация")
    @allure.description("Проверяем, что курьер может авторизоваться и получает id")
    def test_login_courier_success(self):
        courier_api = CourierApi(BASE_URL)
        courier_data = register_new_courier_and_return_login_password()
        assert courier_data, "Не удалось создать курьера"
        
        login, password, first_name, create_response = courier_data
        
        login_data = CourierData.login_data(login, password)
        
        response = courier_api.login_courier(login_data)
        
        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

        courier_api.delete_courier_by_credentials(login, password)
        

    @allure.title("Негативный тест: авторизация без обязательных полей")
    @pytest.mark.parametrize("login_data,expected_message", [
        (CourierData.login_data_missing_login(), "Недостаточно данных для входа"),
        (CourierData.login_data_missing_password(), "Недостаточно данных для входа"),
    ])
    def test_login_missing_fields(self, login_data, expected_message):

        courier_api = CourierApi(BASE_URL)
        response = courier_api.login_courier(login_data)
        
        assert response.status_code == 400
        assert expected_message in response.text
    
    @allure.title("Негативный тест: авторизация с неверным логином")
    def test_login_invalid_login(self):
        courier_api = CourierApi(BASE_URL)
        courier_data = register_new_courier_and_return_login_password()
        assert courier_data, "Не удалось создать курьера"
        
        login, password, first_name, create_response = courier_data
        
        login_data = CourierData.invalid_login_data()
        login_data["password"] = password
        
        response = courier_api.login_courier(login_data)
        
        assert response.status_code == 404
        assert ErrorMessages.ACCOUNT_NOT_FOUND in response.text
        
    @allure.title("Негативный тест: авторизация с неверным паролем")
    def test_login_invalid_password(self):
        courier_api = CourierApi(BASE_URL)
        courier_data = register_new_courier_and_return_login_password()
        assert courier_data, "Не удалось создать курьера"
        
        login, password, first_name, create_response = courier_data
        
        login_data = CourierData.login_data(login, "wrong_password")
        
        response = courier_api.login_courier(login_data)
        
        assert response.status_code == 404
        assert ErrorMessages.ACCOUNT_NOT_FOUND in response.text
        
      
    @allure.title("Негативный тест: авторизация несуществующего пользователя")
    def test_login_none_user(self):

        courier_api = CourierApi(BASE_URL)
        
        login_data = CourierData.invalid_login_data()
        
        response = courier_api.login_courier(login_data)
        
        assert response.status_code == 404
        assert ErrorMessages.ACCOUNT_NOT_FOUND in response.text