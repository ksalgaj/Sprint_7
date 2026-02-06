from api_client.client import APIClient
import allure


@allure.feature("Получение заказов")
@allure.story("GET /orders")
class TestGetOrders:

    @allure.title("Получение списка заказов")
    @allure.description("Проверка, что API возвращает список заказов")
    def test_get_orders_returns_orders_list(self, api_client: APIClient):

        response = api_client.list_orders()

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
