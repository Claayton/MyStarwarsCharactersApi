"""Arquivo para montar o caso de uso UpdateUser"""
from my_starwars.infra.database.repo import UserRepo
from my_starwars.data.users import UpdateUser
from my_starwars.presenters.controllers.users import UpdateUserController
from my_starwars.config import CONNECTION_STRING


def update_user_composer():
    """Montagem do caso de uso UpdateUser"""

    infra = UserRepo(CONNECTION_STRING)
    usecase = UpdateUser(infra)
    controller = UpdateUserController(usecase)

    return controller
