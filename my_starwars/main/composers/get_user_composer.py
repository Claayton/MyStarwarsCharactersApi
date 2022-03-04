"""Arquivo para montar o caso de uso GetUser"""
from typing import Type
from my_starwars.infra.database.repo import UserRepo, CharacterRepo
from my_starwars.data.interfaces import UserRepoInterface, CharacterRepoInterface
from my_starwars.data.users import GetUser
from my_starwars.presenters.controllers.users import GetUserController
from my_starwars.config import CONNECTION_STRING


def get_user_composer(
    infra: Type[UserRepoInterface] = UserRepo(CONNECTION_STRING),
    character_repo: Type[CharacterRepoInterface] = CharacterRepo(CONNECTION_STRING),
):
    """Montagem do caso de uso GetUser"""

    usecase = GetUser(infra)
    controller = GetUserController(usecase, character_repo)

    return controller
