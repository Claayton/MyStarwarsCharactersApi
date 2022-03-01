"""Arquivo para montar o caso de uso RegisterCharacter"""
from my_starwars.infra.database.repo import CharacterRepo
from my_starwars.infra.consumer import StarWarsCharactersConsumer
from my_starwars.data.chraracters import (
    StarwarsCharactersColector,
    RegisterCharacter,
    GetCharacter,
)
from my_starwars.config import SEARCH_URL
from my_starwars.presenters.controllers.characters import RegisterCharacterController
from my_starwars.config import CONNECTION_STRING


def register_character_composer():
    """Montagem do caso de uso RegisterCharacter"""

    infra_repo = CharacterRepo(CONNECTION_STRING)
    infra_consumer = StarWarsCharactersConsumer(SEARCH_URL)
    colector = StarwarsCharactersColector(infra_consumer)
    get_character = GetCharacter(infra_repo)
    usecase = RegisterCharacter(colector, infra_repo, get_character)
    controller = RegisterCharacterController(usecase)

    return controller
