import pytest
import requests

from helpers import CourierHelper
from curl import Urls

@pytest.fixture
def courier_helper():
    return CourierHelper()


@pytest.fixture
def courier_data(courier_helper):
    return courier_helper.generate_courier_data()


@pytest.fixture
def registered_courier(courier_helper):
    response, payload = (
        courier_helper.register_new_courier_and_return_login_password()
    )
    assert response.status_code == 201

    yield payload

    courier_helper.delete_courier(payload)
