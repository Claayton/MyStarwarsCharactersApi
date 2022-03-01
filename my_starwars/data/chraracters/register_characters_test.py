"""Testes para a classe RegisterCharacters"""
from my_starwars.infra.tests import StarWarsCharactersConsumerSpy
from my_starwars.data.chraracters import StarwarsCharactersColector, GetCharacter
from my_starwars.infra.tests import CharacterRepoSpy
from .register_characters import RegisterCharacter


def test_register_characters():
    """Testando o metodo register_characters"""

    infra_consumer = StarWarsCharactersConsumerSpy()
    infra_repo = CharacterRepoSpy()
    colector = StarwarsCharactersColector(infra_consumer)
    get_character = GetCharacter(infra_repo)
    usecase = RegisterCharacter(colector, infra_repo, get_character)

    response = usecase.register_characters()

    assert response["success"] is True
    assert isinstance(response["data"], list)
    assert isinstance(response["data"][0], dict)
    assert "name" in response["data"][0]
    assert "hair_color" in response["data"][0]
