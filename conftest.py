import pytest
import requests

from helpers import CourierHelper
from curl import Urls

@pytest.fixture
def courier_helper():
    return CourierHelper()

@pytest.fixture
def courier_data(courier_helper):
    payload = courier_helper.generate_courier_data()
    yield payload
    courier_helper.delete_courier(payload)


@pytest.fixture
def registered_courier(courier_data):
    response = requests.post(
        Urls.CREATE_COURIER_URL,   # ← используйте Urls, а не «голый» CREATE_COURIER_URL
        data=courier_data,
    )
    assert response.status_code == 201
    yield courier_data
    