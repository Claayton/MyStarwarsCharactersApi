"""Testes para GetUserController"""
from faker import Faker
from my_starwars.presenters.helpers import HttpRequest
from my_starwars.data.users import GetUser
from my_starwars.infra.tests import UserRepoSpy
from .get_user_controller import GetUserController

fake = Faker()


def test_handler_with_query_param_user_id():
    """Testando o metodo handler"""

    infra = UserRepoSpy()
    usecase = GetUser(infra)
    controller = GetUserController(usecase)

    attributes = {"user_id": fake.random_number()}

    response = controller.handler(HttpRequest(query=attributes))

    # Testando as entradas:
    assert infra.insert_user_params["user_id"] == attributes["user_id"]

    # Testando as saidas:
    assert response.status_code == 200
    assert "error" not in response.body


def test_handler_with_query_param_name():
    """Testando o metodo handler"""

    infra = UserRepoSpy()
    usecase = GetUser(infra)
    controller = GetUserController(usecase)

    attributes = {"name": fake.name()}

    response = controller.handler(HttpRequest(query=attributes))

    # Testando as entradas:
    assert infra.insert_user_params["name"] == attributes["name"]

    # Testando as saidas:
    assert response.status_code == 200
    assert "error" not in response.body


def test_handler_with_query_param_email():
    """Testando o metodo handler"""

    infra = UserRepoSpy()
    usecase = GetUser(infra)
    controller = GetUserController(usecase)

    attributes = {"email": f"{fake.word()}@test.com"}

    response = controller.handler(HttpRequest(query=attributes))

    # Testando as entradas:
    assert infra.insert_user_params["email"] == attributes["email"]

    # Testando as saidas:
    assert response.status_code == 200
    assert "error" not in response.body
