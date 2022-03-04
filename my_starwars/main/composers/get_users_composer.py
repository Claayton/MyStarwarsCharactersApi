"""Arquivo para montar o caso de uso GetUsers"""
from typing import Type
from my_starwars.infra.database.repo import UserRepo
from my_starwars.data.interfaces import UserRepoInterface
from my_starwars.data.users import GetUser
from my_starwars.presenters.controllers.users import GetUsersController
from my_starwars.config import CONNECTION_STRING


def get_users_composer(infra: Type[UserRepoInterface] = UserRepo(CONNECTION_STRING)):
    """Montagem do caso de uso GetUsers"""

    usecase = GetUser(infra)
    controller = GetUsersController(usecase)

    return controller
