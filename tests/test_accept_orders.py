from api_client.client import APIClient
from test_data import INVALID_COURIER_ID, INVALID_ORDER_ID
import allure


@allure.feature("Принятие заказа")
@allure.story("PUT /orders/accept/:id")
class TestAcceptOrders:

    @allure.title("Успешное принятие заказа")
    @allure.description("Заказ можно успешно принять при валидном orderId и courierId")
    def test_accept_order_success(self, api_client: APIClient, registered_courier, created_order):
        order_id, _ = created_order
        response = api_client.accept_orders(order_id, registered_courier["id"])

        assert response.status_code == 200
        assert response.json() == {"ok":True}

    @allure.title("Ошибка принятия заказа при отсутствие courierId")
    @allure.description("Если не передан id курьера, API возвращает 400 с сообщением об ошибке")
    def test_accept_order_missing_courier_id(self, api_client: APIClient, created_order):
        order_id, _ = created_order
        response = api_client.accept_orders(order_id, None)

        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Ошибка при неверном courierId")
    @allure.description("Если передан неверный id курьера, API возвращает 404 с сообщением")
    def test_accept_order_invalid_courier_id(self, api_client: APIClient, created_order):
        order_id, _ = created_order
        response = api_client.accept_orders(order_id, courier_id=INVALID_COURIER_ID)
        
        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title("Ошибка при отсутствии orderId")
    @allure.description("Если не передан id заказа, но передан courierId, API возвращает 400 с сообщением")
    def test_accept_order_missing_order_id(self, api_client: APIClient, registered_courier):
       response = api_client.accept_order_without_order_id(registered_courier["id"])
       
       assert response.status_code == 400 
       assert "message" in response.json()

    @allure.title("Ошибка при неверном orderId")
    @allure.description("Если передан неверный id заказа, API возвращает 404 с сообщением")
    def test_accept_order_invalid_order_id(self, api_client: APIClient, registered_courier):
       response = api_client.accept_orders(order_id=INVALID_ORDER_ID, courier_id=registered_courier["id"])

       assert response.status_code == 404
       assert "message" in response.json()
       