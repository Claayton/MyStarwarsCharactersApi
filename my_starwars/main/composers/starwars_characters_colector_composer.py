"""Arquivo para montar o caso de uso StarwarsCharactersColector"""
from typing import Type
from my_starwars.data.interfaces import StarWarsCharactersConsumerInterface
from my_starwars.infra.consumer import StarWarsCharactersConsumer
from my_starwars.data.chraracters import StarwarsCharactersColector
from my_starwars.presenters.controllers.characters import (
    StarwarsCharactersColectorController,
)
from my_starwars.config import SEARCH_URL


def starwars_characters_colector_composer(
    infra: Type[StarWarsCharactersConsumerInterface] = StarWarsCharactersConsumer(
        SEARCH_URL
    ),
) -> any:
    """Montagem do caso de uso StarwarsCharactersColector"""

    usecase = StarwarsCharactersColector(infra)
    controller = StarwarsCharactersColectorController(usecase)

    return controller
