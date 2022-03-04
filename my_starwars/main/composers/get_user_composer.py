"""Arquivo para montar o caso de uso GetUser"""
from typing import Type
from my_starwars.infra.database.repo import UserRepo
from my_starwars.data.interfaces import UserRepoInterface
from my_starwars.data.users import GetUser
from my_starwars.presenters.controllers.users import GetUserController
from my_starwars.config import CONNECTION_STRING


def get_user_composer(infra: Type[UserRepoInterface] = UserRepo(CONNECTION_STRING)):
    """Montagem do caso de uso GetUser"""

    usecase = GetUser(infra)
    controller = GetUserController(usecase)

    return controller
