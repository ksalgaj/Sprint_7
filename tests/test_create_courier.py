import pytest
import allure
from api_client.client import APIClient


@allure.feature("Создание курьера")
@allure.story("POST /courier")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    @allure.description("Проверка, что курьер создаётся при передаче всех обязательных полей")
    def test_create_courier_success(self, api_client: APIClient, generate_random_string, login_and_delete_courier):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = api_client.create_courier(payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        courier = login_and_delete_courier({
            "login": payload["login"],
            "password": payload["password"]
        })

        assert "id" in courier

    @allure.title("Нельзя создать двух одинаковых курьеров")
    @allure.description("Проверка ошибки при создании курьера с уже существующим логином")
    def test_create_duplicate_courier(self, api_client: APIClient, registered_courier):

        response = api_client.create_courier(registered_courier)

        assert response.status_code == 409
        assert response.json().get("message") == "Этот логин уже используется. Попробуйте другой."

    @allure.title("Ошибка при отсутствии обязательного поля")
    @allure.description("Проверка, что без login или password курьер не создаётся")
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
        assert response.json().get("message") == "Недостаточно данных для создания учетной записи"

