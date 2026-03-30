import allure
import requests

class OrderAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.endpoints = {
            "create_order": "/api/v1/orders",
            "list": "/api/v1/orders"
        }

    @allure.step("Создание заказа")
    def create_order(self, order_data):
        return requests.post(
            f"{self.base_url}{self.endpoints['create_order']}",
            json=order_data
        )

    @allure.step("Получение списка заказов")
    def get_orders_list(self):
        return requests.get(
            f"{self.base_url}{self.endpoints['list']}",
            params={"limit": 10}
        )