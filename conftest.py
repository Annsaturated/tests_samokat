import pytest
import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru"

@pytest.fixture
def base_url():
    return BASE_URL