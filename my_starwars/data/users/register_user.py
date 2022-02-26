"""Caso de uso: RegisterUser"""
from typing import Type, Dict
from my_starwars.domain.models import User
from my_starwars.domain.usecases import RegisterUserInterface
from my_starwars.data.interfaces import UserRepoInterface


class RegisterUser(RegisterUserInterface):
    """Classe responsavel por registrar novos usuarios no sistema"""

    def __init__(self, user_repo: Type[UserRepoInterface]) -> None:
        self.__user_repo = user_repo

    def register(self, name: str, email: str, password_hash: str) -> Dict[bool, User]:
        """
        Classe responsavel por realizar o registro de novo usuario no banco de dados.
        :param name: Nome do usuario.
        :param email: Email do usuario.
        :para password_hash: Um hash da senha do usuario.
        :return: Uma mensagem de sucesso e um usuario.
        """

        validate_entry = (
            isinstance(name, str)
            and isinstance(email, str)
            and isinstance(password_hash, str)
        )

        if validate_entry:

            user_insertion = self.__user_repo.insert_user(
                name=name, email=email, password_hash=password_hash
            )

        return {"success": validate_entry, "data": user_insertion}
