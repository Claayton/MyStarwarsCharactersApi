"""Testes para a classe GetCharacterController"""
from faker import Faker
from my_starwars.presenters.helpers import HttpRequest
from my_starwars.infra.tests import CharacterRepoSpy
from my_starwars.data.chraracters import GetCharacter
from .get_characters_controller import GetCharactersController

fake = Faker()


def test_handler():
    """Testando o método handler"""

    infra_repo = CharacterRepoSpy()
    get_character = GetCharacter(infra_repo)
    controller = GetCharactersController(get_character)

    attributes = {"id": fake.random_number(digits=3)}

    response = controller.handler(HttpRequest(query=attributes))

    assert response.status_code == 200
    assert isinstance(response.body, dict)
    assert isinstance(response.body["data"], list)
    assert response.body["data"] is not None
    assert "error" not in response.body
    assert "hair_color" in response.body["data"][0]
    assert "birth_year" in response.body["data"][0]
