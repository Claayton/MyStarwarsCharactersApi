"""Arquivo para montar o caso de uso getuser"""
from my_starwars.infra.database.repo import UserRepo
from my_starwars.data.users import GetUser
from my_starwars.presenters.controllers.users import GetUserController
from my_starwars.config import CONNECTION_STRING


def register_user_composer():
    """Montagem do caso de uso Registeruser"""

    infra = UserRepo(CONNECTION_STRING)
    usecase = GetUser(infra)
    controller = GetUserController(usecase)

    return controller
