"""Testes para AuthenticationController"""
from faker import Faker
from my_starwars.presenters.helpers import HttpRequest
from my_starwars.data.tests import HashPasswordSpy
from my_starwars.data.users import GetUser
from my_starwars.data.auth import Authentication
from my_starwars.infra.tests import UserRepoSpy
from .authentication_controller import AuthenticationController

fake = Faker()


def test_handler():
    """Testando o metodo handler"""

    infra = UserRepoSpy()
    get_user = GetUser(infra)
    hash_password = HashPasswordSpy()
    usecase = Authentication(get_user, hash_password)
    controller = AuthenticationController(usecase)

    attributes = {"email": f"{fake.name()}@test.com", "password": fake.word()}

    response = controller.handler(HttpRequest(body=attributes))

    # Testando as entradas:
    assert hash_password.verify_password_params["password"] == attributes["password"]

    # Testando as saidas:
    assert response.status_code == 200
    assert "error" not in response.body
