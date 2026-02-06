import pytest
import json
from api_client.client import APIClient


class TestCreateOrder:

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
        payload = {
            "firstName": "Мария",
            "lastName": "Иванова",
            "address": "Москва",
            "metroStation": 5,
            "phone": "+7 903 333 333",
            "rentTime": 5,
            "deliveryDate": "2026-05-30",
            "comment": "Позвонить перед доставкой",
            **color_payload
        }

        response = api_client.create_order(json.dumps(payload))

        assert response.status_code == 201
        assert "track" in response.json()
        