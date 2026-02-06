from api_client.client import APIClient
from test_data import NONEXISTENT_TRACK


class TestGetTrack:

    def test_get_order_success(self, api_client: APIClient, created_order):
        order_id, track_id = created_order
        response = api_client.get_track(track_id)

        assert response.status_code == 200
        assert "order" in response.json()
        assert response.json()["order"]["id"] == int(order_id)

    def test_get_order_missing_tracking(self, api_client: APIClient):
        response = api_client.get_track(track_id="")

        assert response.status_code == 400
        assert "message" in response.json()

    def test_get_order_nonexistent(self, api_client: APIClient):
        response = api_client.get_track(track_id=NONEXISTENT_TRACK)

        assert response.status_code == 404
        assert "message" in response.json()
        