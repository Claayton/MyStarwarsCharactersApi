"""Arquivo para montar o caso de uso RegisterUser"""
from typing import Type
from my_starwars.infra.database.repo import UserRepo
from my_starwars.data.interfaces import UserRepoInterface
from my_starwars.data.users import RegisterUser, HashPassword
from my_starwars.presenters.controllers.users import RegisterUserController
from my_starwars.config import CONNECTION_STRING


def register_user_composer(
    infra: Type[UserRepoInterface] = UserRepo(CONNECTION_STRING),
):
    """Montagem do caso de uso RegisterUser"""

    hash_password = HashPassword()
    usecase = RegisterUser(infra, hash_password)
    controller = RegisterUserController(usecase)

    return controller
