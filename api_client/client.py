import requests


class APIClient:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

    def create_courier(self, payload):
        return requests.post(f"{self.BASE_URL}/courier", data=payload)

    def login_courier(self, payload):
        return requests.post(f"{self.BASE_URL}/courier/login", data=payload)
    
    def create_order(self, payload):
        return requests.post(f"{self.BASE_URL}/orders", data=payload)

    def list_orders(self):
        return requests.get(f"{self.BASE_URL}/orders")
    
    def delete_courier(self, id):
        return requests.delete(f"{self.BASE_URL}/courier/{id}")
    
    def accept_orders(self, order_id, courier_id):
        url = f"{self.BASE_URL}/orders/accept/{order_id}"
        params = {}

        if courier_id is not None:
            params["courierId"] = courier_id

        return requests.put(url, params=params)
    
    def accept_order_without_order_id(self, courier_id):
        url = f"{self.BASE_URL}/orders/accept/courierId={courier_id}"
        response = requests.put(url)
        return response
    
    def get_track(self, track_id):
        params = {"t": track_id}
        return requests.get(f"{self.BASE_URL}/orders/track", params=params)
