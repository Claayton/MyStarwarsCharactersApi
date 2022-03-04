"""Arquivo para montar o caso de uso UpdateUser"""
from typing import Type
from my_starwars.infra.database.repo import UserRepo, CharacterRepo
from my_starwars.data.interfaces import UserRepoInterface, CharacterRepoInterface
from my_starwars.data.users import UpdateUser
from my_starwars.presenters.controllers.users import UpdateUserController
from my_starwars.config import CONNECTION_STRING


def update_user_composer(
    infra: Type[UserRepoInterface] = UserRepo(CONNECTION_STRING),
    character_repo: Type[CharacterRepoInterface] = CharacterRepo(CONNECTION_STRING),
):
    """Montagem do caso de uso UpdateUser"""

    usecase = UpdateUser(infra)
    controller = UpdateUserController(usecase, character_repo)

    return controller
