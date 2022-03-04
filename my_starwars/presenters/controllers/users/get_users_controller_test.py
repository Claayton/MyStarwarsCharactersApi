"""Testes para GetUsersController"""
from faker import Faker
from my_starwars.data.users import GetUser
from my_starwars.infra.tests import UserRepoSpy, CharacterRepoSpy
from . import GetUsersController

fake = Faker()


def test_handler():
    """Testando o metodo handler"""

    infra = UserRepoSpy()
    character_repo = CharacterRepoSpy()
    usecase = GetUser(infra)
    controller = GetUsersController(usecase, character_repo)

    response = controller.handler(None)

    # Testando as saidas:
    assert response.status_code == 200
    assert "error" not in response.body
