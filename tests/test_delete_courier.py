from api_client.client import APIClient
from test_data import INVALID_COURIER_ID
import allure


@allure.feature("Удаление курьера")
@allure.story("DELETE /courier/{id}")
class TestDeleteCourier:

    @allure.title("Успешное удаление курьера")
    @allure.description("Проверка, что курьер успешно удаляется при передаче корректного id")
    def test_delete_courier_success(self, api_client: APIClient, registered_courier):
        
        response = api_client.delete_courier(registered_courier["id"])

        assert response.status_code == 200
        assert response.json() == {"ok":True}

    @allure.title("Ошибка при удалении курьера без id")
    @allure.description("Проверка, что запрос на удаление курьера без id возвращает ошибку")
    def test_delete_courier_missing_id(self, api_client: APIClient):

        response = api_client.delete_courier(id="")

        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title("Ошибка при удалении несуществующего курьера")
    @allure.description("Проверка, что при передаче несуществующего id возвращается ошибка")
    def test_delete_courier_nonexistent_id(self, api_client: APIClient):

        response = api_client.delete_courier(id=INVALID_COURIER_ID)

        assert response.status_code == 404
        assert "message" in response.json()


