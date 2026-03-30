import pytest
import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru"

@pytest.fixture
def session():
    with requests.Session() as session:
        yield session