from api_client.client import APIClient
from test_data import INVALID_COURIER_ID


class TestDeleteCourier:

    def test_delete_courier_success(self, api_client: APIClient, registered_courier):
        
        response = api_client.delete_courier(registered_courier["id"])

        assert response.status_code == 200
        assert response.json() == {"ok":True}

    def test_delete_courier_missing_id(self, api_client: APIClient):

        response = api_client.delete_courier(id="")

        assert response.status_code == 404
        assert "message" in response.json()

    def test_delete_courier_nonexistent_id(self, api_client: APIClient):

        response = api_client.delete_courier(id=INVALID_COURIER_ID)

        assert response.status_code == 404
        assert "message" in response.json()


