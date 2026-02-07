import pytest
from api_client.client import APIClient
import allure

@allure.feature("Авторизация курьера")
@allure.story("POST /courier/login")
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    @allure.description("Проверка, что курьер может авторизоваться с корректными логином и паролем")
    def test_successful_login_courier(self, api_client: APIClient, registered_courier):
        payload = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }

        response = api_client.login_courier(payload)

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Ошибка авторизации при отсутствии обязательного поля")
    @allure.description("Проверка, что без логина или пароля авторизация невозможна")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_courier_login_missing_required_field(self, api_client: APIClient, registered_courier, missing_field):
        payload = {
            "login": registered_courier["login"],
            "password": registered_courier["password"]
        }

        payload[missing_field] = "" 

        response = api_client.login_courier(payload)

        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для входа"

    @allure.title("Ошибка авторизации несуществующего курьера")
    @allure.description("Проверка, что авторизация под несуществующим пользователем возвращает ошибку")
    def test_login_fails_for_nonexistent_user(self, api_client: APIClient, generate_random_string):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10)
        }

        response = api_client.login_courier(payload)

        assert response.status_code == 404
        assert response.json().get("message") == "Учетная запись не найдена"

    @allure.title("Ошибка авторизации при неверных логине или пароле")
    @allure.description("Проверка, что при передаче неверных логина или пароля возвращается ошибка")
    def test_login_fails_with_invalid_credentials(self, api_client: APIClient, registered_courier):
        test_cases = [
            {"login": "wrong_login", "password": registered_courier["password"]},
            {"login": registered_courier["login"], "password": "wrong_password"},
        ]

        for payload in test_cases:
            response = api_client.login_courier(payload)
            assert response.status_code == 404
            assert response.json().get("message") == "Учетная запись не найдена"
