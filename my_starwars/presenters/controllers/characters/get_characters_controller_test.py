"""Testes para a classe GetCharacterController"""
from faker import Faker
from my_starwars.domain.models import Character
from my_starwars.presenters.helpers import HttpRequest
from my_starwars.infra.tests import CharacterRepoSpy
from my_starwars.data.chraracters import GetCharacter
from .get_characters_controller import GetCharacterController

fake = Faker()


def test_handler():
    """Testando o método handler"""

    infra_repo = CharacterRepoSpy()
    get_character = GetCharacter(infra_repo)
    controller = GetCharacterController(get_character)

    attributes = {"id": fake.random_number(digits=3)}

    response = controller.handler(HttpRequest(query=attributes))

    assert response.status_code == 200
    assert isinstance(response.body, Character)
    assert response.body.name
    assert response.body.hair_color
