import requests
import allure

from curl import Urls

@allure.feature("Создание курьера")
class TestCreateCourier:
    
    @allure.title("Успешное создание курьера")
    @allure.description("Проверка создания курьера с корректными данными.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_courier_success(self, courier_data):
        response = requests.post(
            Urls.CREATE_COURIER_URL,
            data=courier_data,
        )

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Создание двух одинаковых курьеров")
    @allure.description("Проверка, что нельзя создать двух курьеров с одинаковыми данными.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_two_identical_couriers(self, courier_data):
        first_response = requests.post(
            Urls.CREATE_COURIER_URL,
            data=courier_data,
        )
        second_response = requests.post(
            Urls.CREATE_COURIER_URL,
            data=courier_data,
        )

        assert first_response.status_code == 201
        assert second_response.status_code == 409
        assert second_response.json()["message"] == "Этот логин уже используется"

    @allure.title("Создание курьера без логина")
    @allure.description("Проверка ошибки при отсутствии обязательного поля login.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_courier_without_login(self, courier_data):
        payload = courier_data.copy()
        del payload["login"]

        response = requests.post(
            Urls.CREATE_COURIER_URL,
            data=payload,
        )

        assert response.status_code == 400
        assert response.json()["message"] == (
            "Недостаточно данных для создания учетной записи"
        )

    @allure.title("Создание курьера без пароля")
    @allure.description("Проверка ошибки при отсутствии обязательного поля password.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_courier_without_password(self, courier_data):
        payload = courier_data.copy()
        del payload["password"]

        response = requests.post(
            Urls.CREATE_COURIER_URL,
            data=payload,
        )

        assert response.status_code == 400
        assert response.json()["message"] == (
            "Недостаточно данных для создания учетной записи"
        )

    @allure.title("Создание курьера с уже существующим логином")
    @allure.description("Проверка ошибки при регистрации курьера с занятым логином.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_courier_with_existing_login(
        self,
        registered_courier,
        courier_helper,
    ):
        payload = {
            "login": registered_courier["login"],
            "password": courier_helper.generate_random_string(),
            "firstName": courier_helper.generate_random_string(),
        }

        response = requests.post(
            Urls.CREATE_COURIER_URL,
            data=payload,
        )

        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется"
