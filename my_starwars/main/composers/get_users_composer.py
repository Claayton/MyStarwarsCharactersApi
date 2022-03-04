"""Arquivo para montar o caso de uso GetUsers"""
from typing import Type
from my_starwars.infra.database.repo import UserRepo, CharacterRepo
from my_starwars.data.interfaces import UserRepoInterface, CharacterRepoInterface
from my_starwars.data.users import GetUser
from my_starwars.presenters.controllers.users import GetUsersController
from my_starwars.config import CONNECTION_STRING


def get_users_composer(
    infra: Type[UserRepoInterface] = UserRepo(CONNECTION_STRING),
    character_repo: Type[CharacterRepoInterface] = CharacterRepo(CONNECTION_STRING),
):
    """Montagem do caso de uso GetUsers"""

    usecase = GetUser(infra)
    controller = GetUsersController(usecase, character_repo)

    return controller
