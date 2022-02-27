"""Testes para a classe StarwarsCharactersColector"""
from my_starwars.infra.tests import StarWarsCharactersConsumerSpy
from my_starwars.data.chraracters import StarwarsCharactersColector


def test_starwars_characters_colector():
    """Testando o metodo starwars_characters_colector"""

    api_consumer = StarWarsCharactersConsumerSpy()
    starwars_characters_colector = StarwarsCharactersColector(api_consumer=api_consumer)

    response = starwars_characters_colector.starwars_characters_colector()

    # Testando a entrada:
    assert api_consumer.get_characters_attributes["page"] == list(range(1, 20))

    # Testando a saída:
    assert isinstance(response, dict)
    assert isinstance(response["data"], list)
    assert isinstance(response["data"][0], dict)
    assert "name" in response["data"][0]
    assert "hair_color" in response["data"][0]
