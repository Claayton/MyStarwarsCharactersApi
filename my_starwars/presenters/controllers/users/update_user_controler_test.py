"""Testes para UpdateUserController"""
from faker import Faker
from my_starwars.presenters.helpers import HttpRequest
from my_starwars.data.users import UpdateUser
from my_starwars.infra.tests import UserRepoSpy
from .update_user_controller import UpdateUserController

fake = Faker()


def test_handler():
    """Testando o metodo handler"""

    infra = UserRepoSpy()
    usecase = UpdateUser(infra)
    controller = UpdateUserController(usecase)

    attributes = {
        "user_id": fake.random_number(digits=1),
        "name": fake.name(),
        "email": f"{fake.word()}@test.com",
        "character_id": fake.random_number(digits=1),
    }

    response = controller.handler(HttpRequest(body=attributes))

    # Testando as entradas:
    assert infra.updated_user_params["user_id"] == attributes["user_id"]
    assert infra.updated_user_params["name"] == attributes["name"]
    assert infra.updated_user_params["email"] == attributes["email"]
    assert infra.updated_user_params["character_id"] == attributes["character_id"]

    # Testando as saidas:
    assert response.status_code == 201
    assert "error" not in response.body
