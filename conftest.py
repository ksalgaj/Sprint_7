import pytest
import random
import string
import json
from api_client.client import APIClient
from tests.helpers import register_new_courier_and_return_login_password
from tests.test_data import ORDER_PAYLOAD

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def generate_random_string():
        def _generate(length=10):
            letters = string.ascii_lowercase
            return ''.join(random.choice(letters) for _ in range(length))
        return _generate

@pytest.fixture
def registered_courier(api_client: APIClient):
    login_pass = register_new_courier_and_return_login_password()
    if not login_pass:
        pytest.fail("Не удалось создать курьера через API")
    courier = {
        "login": login_pass[0],
        "password": login_pass[1],
        "firstName": login_pass[2]
    }

    response = api_client.login_courier({"login": courier["login"], "password": courier["password"]})
    courier["id"] = response.json().get("id")
    yield courier

    if courier.get("id"):
        api_client.delete_courier(courier["id"])


@pytest.fixture
def created_order(api_client: APIClient):

    order_response = api_client.create_order(json.dumps(ORDER_PAYLOAD))

    track_id = order_response.json().get("track")

    track_response = api_client.get_track(track_id)

    track_json = track_response.json()

    order_id = str(track_json["order"]["id"])

    return order_id, track_id