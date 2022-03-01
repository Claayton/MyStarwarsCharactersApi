"""Testes para a classe RegisterCharacterController"""
from faker import Faker
from my_starwars.infra.tests import CharacterRepoSpy, StarWarsCharactersConsumerSpy
from my_starwars.data.chraracters import (
    StarwarsCharactersColector,
    RegisterCharacter,
    GetCharacter,
)
from .register_characters_controller import RegisterCharacterController

faker = Faker()


def test_handler():
    """Testando o método handler"""

    infra_consumer = StarWarsCharactersConsumerSpy()
    colector = StarwarsCharactersColector(infra_consumer)
    infra_repo = CharacterRepoSpy()
    get_character = GetCharacter(infra_repo)
    register_character = RegisterCharacter(colector, infra_repo, get_character)
    controller = RegisterCharacterController(register_character)

    response = controller.handler(None)

    assert response.status_code == 201
    assert "error" not in response.body
