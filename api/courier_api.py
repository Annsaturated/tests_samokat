import allure
import requests

class CourierApi:
    def __init__(self, base_url):
        self.base_url = base_url
        self.endpoints = {
            "create": "/api/v1/courier",
            "login": "/api/v1/courier/login",
            "delete": "/api/v1/courier/"
        }
    
    @allure.step("Создание курьера")
    def create_courier(self, courier_data):
        return requests.post(
            f"{self.base_url}{self.endpoints['create']}",
            json=courier_data
        )

    @allure.step("Логин курьера")
    def login_courier(self, login_data):
        return requests.post(
            f"{self.base_url}{self.endpoints['login']}",
            json=login_data
        )

    @allure.step("Удаление курьера")
    def delete_courier(self, courier_id):
        return requests.delete(
            f"{self.base_url}{self.endpoints['delete']}{courier_id}"
        )
    
    @allure.step("Удаление курьера по логину и паролю")
    def delete_courier_by_credentials(self, login, password):
        login_data = {"login": login, "password": password}
        login_response = self.login_courier(login_data)
        
        if login_response.status_code == 200:
            courier_id = login_response.json().get("id")
            if courier_id:
                return self.delete_courier(courier_id)
        return None