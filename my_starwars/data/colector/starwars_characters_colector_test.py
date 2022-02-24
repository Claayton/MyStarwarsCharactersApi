"""Testes para a classe StarwarsCharactersColector"""
from my_starwars.infra.consumer import StarWarsCharactersConsumer
from my_starwars.data.colector import StarwarsCharactersColector
from my_starwars.config import SEARCH_URL


def test_starwars_characters_colector():
    """Testando o metodo starwars_characters_colector"""

    api_consumer = StarWarsCharactersConsumer(url=SEARCH_URL)
    starwars_characters_colector = StarwarsCharactersColector(api_consumer=api_consumer)

    response = starwars_characters_colector.starwars_characters_colector()

    # Implementar Spy para testar a entrada

    # Testando a saída:
    assert isinstance(response, dict)
    assert isinstance(response["data"], list)
    assert isinstance(response["data"][0], dict)
    assert "name" in response["data"][0]
    assert "hair_color" in response["data"][0]
