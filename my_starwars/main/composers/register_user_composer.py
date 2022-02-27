"""Arquivo para montar o caso de uso Registeruser"""
from my_starwars.infra.database.repo import UserRepo
from my_starwars.data.users import RegisterUser, HashPassword
from my_starwars.presenters.controllers.users import RegisterUserController
from my_starwars.config import CONNECTION_STRING


def register_user_composer():
    """Montagem do caso de uso Registeruser"""

    infra = UserRepo(CONNECTION_STRING)
    hash_password = HashPassword()
    usecase = RegisterUser(infra, hash_password)
    controller = RegisterUserController(usecase)

    return controller
