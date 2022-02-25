"""Arquivo para montar o caso de uso StarwarsCharactersColector"""
from my_starwars.infra.consumer import StarWarsCharactersConsumer
from my_starwars.data.colector import StarwarsCharactersColector
from my_starwars.presenters.controllers.colector import (
    StarwarsCharactersColectorController,
)
from my_starwars.config import SEARCH_URL


def starwars_characters_colector_composer() -> any:
    """Montagem do caso de uso StarwarsCharactersColector"""

    infra = StarWarsCharactersConsumer(SEARCH_URL)
    usecase = StarwarsCharactersColector(infra)
    controller = StarwarsCharactersColectorController(usecase)

    return controller
