"""Testes para a classe RegisterCharacters"""
from my_starwars.infra.tests import StarWarsCharactersConsumerSpy
from my_starwars.data.chraracters import StarwarsCharactersColector
from my_starwars.infra.tests import CharacterRepoSpy
from .register_characters import RegisterCharacter


def test_register_characters():
    """Testando o metodo register_characters"""

    infra_consumer = StarWarsCharactersConsumerSpy()
    infra_repo = CharacterRepoSpy()
    colector = StarwarsCharactersColector(infra_consumer)
    usecase = RegisterCharacter(colector, infra_repo)

    response = usecase.register_characters()

    assert response["success"] is True
    assert isinstance(response["data"], list)
    assert isinstance(response["data"][0], dict)
    assert "name" in response["data"][0]
    assert "hair_color" in response["data"][0]
