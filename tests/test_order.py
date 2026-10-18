import pytest
import requests
import allure

from curl import Urls
from data import DataForCourier 


class TestCreateOrder:
    @allure.title("Создание заказа с разными цветами")
    @allure.description(
    "Проверка создания заказа с различными вариантами цветов "
    "и получения номера трека заказа."
)
    @pytest.mark.parametrize("order_data", DataForCourier.ORDER_DATA)
    def test_create_order_with_different_colors_returns_track(
        self, order_data
    ):
        response = requests.post(
            Urls.CREATE_ORDER_URL,
            json=order_data,
            timeout=10
        )

        assert response.status_code == 201
        assert "track" in response.json()
