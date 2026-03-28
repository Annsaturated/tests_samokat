import allure

class OrderAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.endpoints = {
            "create": "/api/v1/orders",
            "list": "/api/v1/orders"
        }

    @allure.step("Создание заказа")
    def create_order(self, session, order_data):
        return session.post(
            f"{self.base_url}{self.endpoints['create']}",
            json=order_data
        )

    @allure.step("Получение списка заказов")
    def get_orders_list(self, session):
        return session.get(
            f"{self.base_url}{self.endpoints['list']}",
            params={"limit": 10}
        )