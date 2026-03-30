import allure
import requests
from test_data import ListOrderData
from api.order_api import OrderAPI
from conftest import BASE_URL


@allure.feature("Список заказов")
class TestOrdersList:
    
    @allure.title("Тест: получение списка заказов")
    @allure.description("Проверяем, что ручка возвращает список заказов")
    def test_get_orders_list(self):
        order_api = OrderAPI(BASE_URL)
        order_data = ListOrderData.order_for_list_test()
        
        # Создаем заказ
        create_response = requests.post(f"{BASE_URL}/api/v1/orders", json=order_data)
        assert create_response.status_code == 201
        track = create_response.json().get("track")
        assert track is not None, "Трек заказа не получен"

        # Получаем список заказов
        response = order_api.get_orders_list()
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
        
        # Проверяем структуру заказов в списке
        if len(response.json()["orders"]) > 0:
            order = response.json()["orders"][0]
            # Проверяем наличие ключевых полей
            expected_fields = ListOrderData.expected_order_fields()

            for field in expected_fields:
                assert field in order, f"Поле {field} отсутствует в заказе"
    
