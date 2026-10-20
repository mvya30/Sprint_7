class DataForCourier:
    # Длина генерируемых строк для логина, пароля и имени
    RANDOM_STRING_LENGTH = 10

    # Корректные данные для авторизации
    VALID_LOGIN_DATA = {
        "login": "test_courier",
        "password": "1234",
    }

    # Неправильный логин
    INVALID_LOGIN_DATA_1 = {
        "login": "wrong_login",
        "password": "1234",
    }

    # Неправильный пароль
    INVALID_LOGIN_DATA_2 = {
        "login": "test_courier",
        "password": "wrong_password",
    }

    # Пустой логин
    INVALID_LOGIN_DATA_3 = {
        "login": "",
        "password": "201",
    }

    # Пустой пароль
    INVALID_LOGIN_DATA_4 = {
        "login": "tort",
        "password": "",
    }

    ORDER_DATA = [
    {
        "firstName": "Марина",
        "lastName": "Ярцева",
        "address": "Москва, улица Пушкина, 5",
        "metroStation": 4,
        "phone": "+7 918 447 01 67",
        "rentTime": 5,
        "deliveryDate": "2026-10-25",
        "comment": "Заказ с черным цветом",
        "color": ["BLACK"],
    },
    {
        "firstName": "Дмитрий",
        "lastName": "Ярцев",
        "address": "Санкт-Петербург, улица Вавилова, 10",
        "metroStation": 4,
        "phone": "+7 918 123 45 88",
        "rentTime": 5,
        "deliveryDate": "2026-10-25",
        "comment": "Заказ с серым цветом",
        "color": ["GREY"],
    },
    {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, улица Пушкина, 10",
        "metroStation": 4,
        "phone": "+7 999 123 45 67",
        "rentTime": 5,
        "deliveryDate": "2026-10-25",
        "comment": "Заказ с двумя цветами",
        "color": ["BLACK", "GREY"],
    },
    {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2026-10-25",
        "comment": "Order without specifying the color",
    },
]
class CourierMessages:
    LOGIN_ALREADY_USED = "Этот логин уже используется"
    NOT_ENOUGH_DATA = "Недостаточно данных для создания учетной записи"

class LoginMessages:
    NOT_ENOUGH_DATA = "Недостаточно данных для входа"
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    