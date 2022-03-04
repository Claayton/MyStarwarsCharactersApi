"""Arquivo para montar o caso de uso Authentication"""
from my_starwars.infra.database.repo import UserRepo, CharacterRepo
from my_starwars.data.auth import Authentication
from my_starwars.data.users import HashPassword, GetUser
from my_starwars.presenters.controllers.auth import AuthenticationController
from my_starwars.config import CONNECTION_STRING


def authentication_composer():
    """Montagem do caso de uso Authentication"""

    infra = UserRepo(CONNECTION_STRING)
    character_repo = CharacterRepo(CONNECTION_STRING)
    get_user = GetUser(infra)
    hash_password = HashPassword()
    usecase = Authentication(get_user, hash_password)
    controller = AuthenticationController(usecase, character_repo)

    return controller
