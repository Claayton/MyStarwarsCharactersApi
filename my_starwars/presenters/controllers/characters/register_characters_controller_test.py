"""Testes para a classe RegisterCharacterController"""
from faker import Faker
from my_starwars.infra.tests import CharacterRepoSpy, StarWarsCharactersConsumerSpy
from my_starwars.data.chraracters import StarwarsCharactersColector
from my_starwars.data.chraracters import RegisterCharacter
from .register_characters_controller import RegisterCharacterController

faker = Faker()


def test_handler():
    """Testando o método handler"""

    infra_consumer = StarWarsCharactersConsumerSpy()
    colector = StarwarsCharactersColector(infra_consumer)
    infra_repo = CharacterRepoSpy()
    register_character = RegisterCharacter(colector, infra_repo)
    controller = RegisterCharacterController(register_character)

    response = controller.handler(None)

    assert response.status_code == 200
    assert "error" not in response.body
