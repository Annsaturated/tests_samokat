import allure
import pytest
import requests
from test_data import OrderData


@allure.feature("Создание заказа")
class TestCreateOrder:
    
    @allure.title("Создание заказа с разными цветами")
    @allure.description("Проверяем создание заказа с BLACK, GREY, обоими цветами и без цвета")
    @pytest.mark.parametrize("order_data", [
        OrderData.order_with_black_color(),
        OrderData.order_with_grey_color(),
        OrderData.order_with_both_colors(),
        OrderData.order_without_color()
    ])
    def test_create_order_with_colors(self, base_url, order_data):
        
        response = requests.post(
            f"{base_url}/api/v1/orders",
            json=order_data
        )
        
        assert response.status_code == 201
        assert "track" in response.json()
        assert isinstance(response.json()["track"], int)
        assert response.json()["track"] > 0
