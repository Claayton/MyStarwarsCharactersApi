"""Testes para a rota register_user"""
from fastapi.testclient import TestClient
from faker import Faker
from .users_routes import users

fake = Faker()
client = TestClient(users)


def test_register_user():
    """Testando a rota register_user"""

    url = "/api/users/"
    data = {
        "name": fake.name(),
        "email": f"{fake.word()}@test.com",
        "password": fake.word(),
    }

    response = client.post(url=url, json=data)

    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert response.json()["message"] is not None
    assert isinstance(response.json()["data"], dict)
    assert "name" in response.json()["data"]
    assert "email" in response.json()["data"]
    assert "password" in response.json()["data"]


def test_register_user_error402_with_invalid_name_param():
    """
    Testando o erro 402 - Unprocessable Entity na rota register_user.
    Utilizando um valor invalido para o parametro 'name'.
    """

    url = "/api/users/"
    data = {
        "name": fake.random_number(),
        "email": f"{fake.word()}@test.com",
        "password": fake.word(),
    }

    response = client.post(url=url, json=data)

    assert response.status_code == 402
    assert "error" in response.json()


def test_register_user_error402_with_invalid_email_param():
    """
    Testando o erro 402 - Unprocessable Entity na rota register_user.
    Utilizando um valor invalido para o parametro 'email'.
    """

    url = "/api/users/"
    data = {"name": fake.name(), "email": fake.random_number(), "password": fake.word()}

    response = client.post(url=url, json=data)

    assert response.status_code == 402
    assert "error" in response.json()


def test_register_user_error402_without_params():
    """
    Testando o erro 402 - Unprocessable Entity na rota register_user.
    Utilizando um valor invalido para o parametro 'name'.
    """

    url = "/api/users/"

    response = client.post(url=url)

    assert response.status_code == 400
    assert "error" in response.json()
