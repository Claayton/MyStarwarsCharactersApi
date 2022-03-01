"""Testes para StarwarsCharactersColectorController"""
from my_starwars.infra.tests import StarWarsCharactersConsumerSpy
from my_starwars.data.chraracters import StarwarsCharactersColector
from my_starwars.presenters.controllers.characters import (
    StarwarsCharactersColectorController,
)


def test_handler():
    """Testando o metodo handler"""

    infra = StarWarsCharactersConsumerSpy()
    starwars_characters_colector = StarwarsCharactersColector(api_consumer=infra)
    controller = StarwarsCharactersColectorController(starwars_characters_colector)

    response = controller.handler(None)

    assert response.status_code == 200
    assert "error" not in response.body
