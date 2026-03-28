import allure

class CourierAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.endpoints = {
            "create": "/api/v1/courier",
            "login": "/api/v1/courier/login",
            "delete": "/api/v1/courier/"
        }

    @allure.step("Создание курьера")
    def create_courier(self, session, courier_data):
        return session.post(
            f"{self.base_url}{self.endpoints['create']}",
            json=courier_data
        )

    @allure.step("Логин курьера")
    def login_courier(self, session, login_data):
        return session.post(
            f"{self.base_url}{self.endpoints['login']}",
            json=login_data
        )

    @allure.step("Удаление курьера")
    def delete_courier(self, session, courier_id):
        return session.delete(
            f"{self.base_url}{self.endpoints['delete']}{courier_id}"
        )