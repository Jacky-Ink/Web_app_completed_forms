import pytest
from app.config import Config


@pytest.fixture
def get_form_url() -> str:
    return f'http://{Config.SERVER_NAME}/get_form'


@pytest.fixture
def request_data() -> dict:
    return {
        "name": "Jacky1nk",
        "email": "youmail@email.com",
        "phone": "+7 800 555 35 35",
        "date_of_birth": "1995-01-01"
    }


@pytest.fixture
def incorrect_email() -> dict:
    return {"email": "incorrect_email"}


@pytest.fixture
def incorrect_phone() -> dict:
    return {"phone": "incorrect_phone"}


@pytest.fixture
def incorrect_date() -> dict:
    return {"date_of_birth": "01 01 1995"}
