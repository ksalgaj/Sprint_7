import pytest
from api_client.client import APIClient

class TestCreateCourier:

    def test_create_courier_success(self, api_client: APIClient, generate_random_string):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = api_client.create_courier(payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    def test_create_duplicate_courier(self, api_client: APIClient, registered_courier):

        response = api_client.create_courier(registered_courier)

        assert response.status_code == 409
        assert "message" in response.json()

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_required_field(self, api_client: APIClient, generate_random_string, missing_field):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        del payload[missing_field]

        response = api_client.create_courier(payload)

        assert response.status_code == 400
        assert "message" in response.json()

