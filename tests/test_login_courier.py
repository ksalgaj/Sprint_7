import pytest
from api_client.client import APIClient


class TestLoginCourier:

    def test_successful_login_courier(self, api_client: APIClient, registered_courier):
        payload = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }

        response = api_client.login_courier(payload)

        assert response.status_code == 200
        assert "id" in response.json()

    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_courier_login_missing_required_field(self, api_client: APIClient, registered_courier, missing_field):
        payload = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }

        payload[missing_field] = "" 

        response = api_client.login_courier(payload)

        assert response.status_code == 400
        assert "message" in response.json()

    def test_login_fails_for_nonexistent_user(self, api_client: APIClient, generate_random_string):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }

        response = api_client.login_courier(payload)

        assert response.status_code == 404
        assert "message" in response.json()

    def test_login_fails_with_invalid_credentials(self, api_client: APIClient, registered_courier):
        test_cases = [
            {"login": "wrong_login", "password": registered_courier["password"]},
            {"login": registered_courier["login"], "password": "wrong_password"},
        ]

        for payload in test_cases:
            response = api_client.login_courier(payload)
            assert response.status_code == 404
            assert "message" in response.json()
