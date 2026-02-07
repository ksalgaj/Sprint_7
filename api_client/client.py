import requests
import allure


class APIClient:
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

    @allure.step("Создать курьера с данными: {payload}")
    def create_courier(self, payload):
        return requests.post(f"{self.BASE_URL}/courier", data=payload)

    @allure.step("Авторизация курьера с данными: {payload}")
    def login_courier(self, payload):
        return requests.post(f"{self.BASE_URL}/courier/login", data=payload)
    
    @allure.step("Создать заказ с данными: {payload}")
    def create_order(self, payload):
        return requests.post(f"{self.BASE_URL}/orders", data=payload)

    @allure.step("Получить список всех заказов")
    def list_orders(self):
        return requests.get(f"{self.BASE_URL}/orders")
    
    @allure.step("Удалить курьера с id: {id}")
    def delete_courier(self, id):
        return requests.delete(f"{self.BASE_URL}/courier/{id}")
    
    @allure.step("Принять заказ order_id={order_id} курьером courier_id={courier_id}")
    def accept_orders(self, order_id, courier_id):
        url = f"{self.BASE_URL}/orders/accept/{order_id}"
        params = {}

        if courier_id is not None:
            params["courierId"] = courier_id

        return requests.put(url, params=params)
    
    @allure.step("Принять заказ без указания order_id курьером courier_id={courier_id}")
    def accept_order_without_order_id(self, courier_id):
        url = f"{self.BASE_URL}/orders/accept/courierId={courier_id}"
        response = requests.put(url)
        return response
    
    @allure.step("Получить заказ по track_id={track_id}")
    def get_track(self, track_id):
        params = {"t": track_id}
        return requests.get(f"{self.BASE_URL}/orders/track", params=params)
    
    @allure.step("Отменить заказ по track_id={track_id}")
    def cancel_order(self, track_id):
        params = {"track": track_id}
        return requests.put(f"{self.BASE_URL}/orders/cancel", params=params)
