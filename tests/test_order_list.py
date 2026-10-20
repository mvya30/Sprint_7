import requests
import allure
from curl import Urls


class TestOrdersList:

    @allure.title("Получение списка заказов")
    @allure.description("Проверка успешного получения списка заказов и структуры ответа")
    def test_get_orders_returns_list(self):
        response = requests.get(
            Urls.GET_ORDERS_URL,
            timeout=30
        )

        assert response.status_code == 200

        response_body = response.json()

        assert "orders" in response_body
        assert isinstance(response_body["orders"], list)
        