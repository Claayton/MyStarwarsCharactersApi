"""Arquivo para montar o caso de uso Authentication"""
from typing import Type
from my_starwars.data.interfaces import UserRepoInterface, CharacterRepoInterface
from my_starwars.infra.database.repo import UserRepo, CharacterRepo
from my_starwars.data.auth import Authentication
from my_starwars.data.users import HashPassword, GetUser
from my_starwars.presenters.controllers.auth import AuthenticationController
from my_starwars.config import CONNECTION_STRING


def authentication_composer(
    infra: Type[UserRepoInterface] = UserRepo(CONNECTION_STRING),
    character_repo: Type[CharacterRepoInterface] = CharacterRepo(CONNECTION_STRING),
):
    """Montagem do caso de uso Authentication"""

    get_user = GetUser(infra)
    hash_password = HashPassword()
    usecase = Authentication(get_user, hash_password)
    controller = AuthenticationController(usecase, character_repo)

    return controller
