"""Arquivo para montar o caso de uso GetCharacter"""
from typing import Type
from my_starwars.data.interfaces import CharacterRepoInterface
from my_starwars.infra.database.repo import CharacterRepo
from my_starwars.data.chraracters import GetCharacter
from my_starwars.presenters.controllers.characters import GetCharactersController
from my_starwars.config import CONNECTION_STRING


def get_character_composer(
    infra: Type[CharacterRepoInterface] = CharacterRepo(CONNECTION_STRING),
):
    """Montagem do caso de uso GetCharacter"""

    usecase = GetCharacter(infra)
    controller = GetCharactersController(usecase)

    return controller
