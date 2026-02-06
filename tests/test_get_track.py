from api_client.client import APIClient
from test_data import NONEXISTENT_TRACK
import allure

@allure.feature("Получение заказа по его номеру")
@allure.story("GET /orders/track")
class TestGetTrack:

    @allure.title("Успешное получение заказа по его номеру")
    @allure.description("Проверка, что по корректному track возвращается заказ")
    def test_get_order_success(self, api_client: APIClient, created_order):
        order_id, track_id = created_order
        response = api_client.get_track(track_id)

        assert response.status_code == 200
        assert "order" in response.json()
        assert response.json()["order"]["id"] == int(order_id)

    @allure.title("Ошибка при запросе заказа без номера")
    @allure.description("Проверка, что запрос без track возвращает ошибку")
    def test_get_order_missing_tracking(self, api_client: APIClient):
        response = api_client.get_track(track_id="")

        assert response.status_code == 400
        assert response.json().get("message") == "Недостаточно данных для поиска"

    @allure.title("Ошибка при запросе несуществующего заказа")
    @allure.description("Проверка, что при запросе с несуществующим track возвращается ошибка")
    def test_get_order_nonexistent(self, api_client: APIClient):
        response = api_client.get_track(track_id=NONEXISTENT_TRACK)

        assert response.status_code == 404
        assert response.json().get("message") == "Заказ не найден"
        