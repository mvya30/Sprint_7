import requests
import allure
from data import DataForCourier 
from curl import Urls

@allure.feature("Логин курьера")
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    @allure.description("Проверка авторизации зарегистрированного курьера с корректными логином и паролем.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_courier_success(
        self,
        registered_courier,
        courier_helper,
    ):
        payload = courier_helper.get_login_payload(
            registered_courier
        )

        response = requests.post(
            Urls.LOGIN_COURIER_URL,
            data=payload,
        )

        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @allure.title("Авторизация с пустым логином")
    @allure.description("Проверка ошибки при отсутствии обязательного поля login.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_courier_without_login(self, registered_courier):
        
        payload = {
        "login": DataForCourier.INVALID_LOGIN_DATA_3["login"],
        "password": registered_courier["password"],
        }

        response = requests.post(
            Urls.LOGIN_COURIER_URL,
            data=payload,
        )

        assert response.status_code == 400
        assert response.json()["message"] == (
            "Недостаточно данных для входа"
        )

    @allure.title("Авторизация с пустым паролем")
    @allure.description("Проверка ошибки при отсутствии обязательного поля password.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_courier_without_password(self, registered_courier):
        
        payload = {
        "login": registered_courier["login"],
        "password": DataForCourier.INVALID_LOGIN_DATA_4["password"],
        }

        response = requests.post(Urls.LOGIN_COURIER_URL,data=payload)

        assert response.status_code == 400
        assert response.json()["message"] == (
            "Недостаточно данных для входа"
        )

    @allure.title("Авторизация с неправильным логином")
    @allure.description("Проверка ошибки при вводе логина, которого нет в системе.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_courier_with_wrong_login(
        self,
        registered_courier,
    ):
        payload = {
            "login": DataForCourier.INVALID_LOGIN_DATA_1["login"],
            "password": registered_courier["password"],
        }

        response = requests.post(
            Urls.LOGIN_COURIER_URL,
            data=payload,
        )

        assert response.status_code == 404
        assert response.json()["message"] == ("Учетная запись не найдена")

    @allure.title("Авторизация с неправильным паролем")
    @allure.description("Проверка ошибки при вводе неверного пароля.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_courier_with_wrong_password(
        self,
        registered_courier,
    ):
        payload = {
        "login": registered_courier["login"],
        "password": DataForCourier.INVALID_LOGIN_DATA_2["password"],
    }

        response = requests.post(
            Urls.LOGIN_COURIER_URL,
            data=payload,
        )

        assert response.status_code == 404
        assert response.json()["message"] == ("Учетная запись не найдена")

    @allure.title("Авторизация несуществующего курьера")
    @allure.description("Проверка ошибки при попытке авторизации пользователя, который не зарегистрирован.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_nonexistent_courier(self, courier_helper):
        payload = {
            "login": courier_helper.generate_random_string(),
            "password": courier_helper.generate_random_string(),
        }

        response = requests.post(
            Urls.LOGIN_COURIER_URL,
            data=payload,
        )

        assert response.status_code == 404
        assert response.json()["message"] == ("Учетная запись не найдена")
