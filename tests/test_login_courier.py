import allure
import pytest
import requests
from test_data import CourierData
from courier_helpers import register_new_courier_and_return_login_password


@allure.feature("Логин курьера")
class TestLoginCourier:
    
    @allure.title("Позитивный тест: успешная авторизация")
    @allure.description("Проверяем, что курьер может авторизоваться и получает id")
    def test_login_courier_success(self, base_url):
        courier_data = register_new_courier_and_return_login_password()
        assert courier_data, "Не удалось создать курьера"
        
        login, password, first_name, create_response = courier_data
        
        login_data = CourierData.login_data(login, password)
        
        response = requests.post(
            f"{base_url}/api/v1/courier/login",
            json=login_data
        )
        
        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)
        

    @allure.title("Негативный тест: авторизация без обязательных полей")
    @pytest.mark.parametrize("login_data,expected_message", [
        (CourierData.login_data_missing_login(), "Недостаточно данных для входа"),
        (CourierData.login_data_missing_password(), "Недостаточно данных для входа"),
    ])
    def test_login_missing_fields(self, base_url, login_data, expected_message):
        response = requests.post(
            f"{base_url}/api/v1/courier/login",
            json=login_data
        )
        
        assert response.status_code == 400
        assert expected_message in response.text
    
    @allure.title("Негативный тест: авторизация с неверным логином")
    def test_login_invalid_login(self, base_url):
        courier_data = register_new_courier_and_return_login_password()
        assert courier_data, "Не удалось создать курьера"
        
        login, password, first_name, create_response = courier_data
        
        login_data = CourierData.invalid_login_data()
        login_data["password"] = password
        
        response = requests.post(
            f"{base_url}/api/v1/courier/login",
            json=login_data
        )
        
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text
        
    @allure.title("Негативный тест: авторизация с неверным паролем")
    def test_login_invalid_password(self, base_url):
        courier_data = register_new_courier_and_return_login_password()
        assert courier_data, "Не удалось создать курьера"
        
        login, password, first_name, create_response = courier_data
        
        login_data = CourierData.login_data(login, "wrong_password")
        
        response = requests.post(
            f"{base_url}/api/v1/courier/login",
            json=login_data
        )
        
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text
        
      
    @allure.title("Негативный тест: авторизация несуществующего пользователя")
    def test_login_none_user(self, base_url):
        
        login_data = CourierData.invalid_login_data()
        
        response = requests.post(
            f"{base_url}/api/v1/courier/login",
            json=login_data
        )
        
        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.text