import pytest
import json
import allure
from api_client.client import APIClient
from test_data import ORDER_PAYLOAD

@allure.feature("Создание заказа")
@allure.story("POST /orders")
class TestCreateOrder:

    @allure.title("Создание заказа с разными вариантами цвета")
    @allure.description("Проверка, что заказ можно создать с одним цветом, двумя цветами или без указания цвета. В ответе должен возвращаться track.")
    @pytest.mark.parametrize(
            "color_payload", 
            [
                {"color": ["BLACK"]},
                {"color": ["GREY"]},
                {"color": ["BLACK", "GREY"]},
                {}
            ]
    )
    def test_create_order_with_different_colors(self, api_client: APIClient, color_payload):

        payload = ORDER_PAYLOAD.copy()
        payload.pop("color", None)
        payload.update(color_payload)

        response = api_client.create_order(json.dumps(payload))

        assert response.status_code == 201
        assert "track" in response.json()
        