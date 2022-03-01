"""Arquivo para montar o caso de uso RegisterCharacter"""
from my_starwars.infra.database.repo import CharacterRepo
from my_starwars.infra.consumer import StarWarsCharactersConsumer
from my_starwars.data.chraracters import RegisterCharacter
from my_starwars.data.chraracters import StarwarsCharactersColector
from my_starwars.config import SEARCH_URL
from my_starwars.presenters.controllers.characters import RegisterCharacterController
from my_starwars.config import CONNECTION_STRING


def register_character_composer():
    """Montagem do caso de uso RegisterCharacter"""

    infra_repo = CharacterRepo(CONNECTION_STRING)
    infra_consumer = StarWarsCharactersConsumer(SEARCH_URL)
    colector = StarwarsCharactersColector(infra_consumer)
    usecase = RegisterCharacter(colector, infra_repo)
    controller = RegisterCharacterController(usecase)

    return controller
