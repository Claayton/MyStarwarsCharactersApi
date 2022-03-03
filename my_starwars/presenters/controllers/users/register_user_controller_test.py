"""Testes para RegisterUserController"""
from faker import Faker
from my_starwars.presenters.helpers import HttpRequest
from my_starwars.data.users import RegisterUser, HashPassword
from my_starwars.infra.tests import UserRepoSpy
from .register_user_controller import RegisterUserController

fake = Faker()


def test_handler():
    """Testando o metodo handler"""

    infra = UserRepoSpy()
    hash_password = HashPassword()
    usecase = RegisterUser(infra, hash_password)
    controller = RegisterUserController(usecase)

    attributes = {
        "name": fake.name(),
        "email": f"{fake.word()}@test.com",
        "password": fake.word(),
    }

    response = controller.handler(HttpRequest(body=attributes))

    # Testando as entradas:
    assert infra.insert_user_params["name"] == attributes["name"]
    assert infra.insert_user_params["email"] == attributes["email"]
    assert infra.insert_user_params["password_hash"] is not None

    # Testando as saidas:
    assert response.status_code == 201
    assert "error" not in response.body
