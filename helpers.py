import requests
import random
import allure
import string
from curl import Urls

class CourierHelper:
    
    def generate_random_string(self, length=10):
        letters = string.ascii_lowercase
        return "".join(random.choice(letters) for _ in range(length))

    def generate_courier_data(self):
        return {
            "login": self.generate_random_string(),
            "password": self.generate_random_string(),
            "firstName": self.generate_random_string(),
        }
    
    @allure.step("Зарегистрировать нового курьера")
    def register_new_courier_and_return_login_password(self):
        payload = self.generate_courier_data()
        response = requests.post(Urls.CREATE_COURIER_URL, data=payload)

        return response, payload

    def get_login_payload(self, courier_data):
        return {
            "login": courier_data["login"],
            "password": courier_data["password"],
        }
    @allure.step("Удалить курьера")
    def delete_courier(self, courier_data):
        login_response = requests.post(
            Urls.LOGIN_COURIER_URL,
            data=self.get_login_payload(courier_data),
            timeout=10,
        )

        courier_id = login_response.json()["id"]

        requests.delete(
            f"{Urls.CREATE_COURIER_URL}/{courier_id}",
            timeout=10,
        )
