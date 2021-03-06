"""Caso de uso: RegisterUser"""
from typing import Type, Dict
from my_starwars.domain.models import User
from my_starwars.domain.usecases import RegisterUserInterface, HashPasswordInterface
from my_starwars.data.interfaces import UserRepoInterface
from my_starwars.errors.http_error400 import HttpBadRequestError


class RegisterUser(RegisterUserInterface):
    """Classe responsavel por registrar novos usuarios no sistema"""

    def __init__(
        self,
        user_repo: Type[UserRepoInterface],
        hash_password: Type[HashPasswordInterface],
    ) -> None:
        self.__user_repo = user_repo
        self.__hash_password = hash_password

    def register(
        self, name: str, email: str, password: str, character_id: int = None
    ) -> Dict[bool, User]:
        """
        Classe responsavel por realizar o registro de novo usuario no banco de dados.
        :param name: Nome do usuario.
        :param email: Email do usuario.
        :para password_hash: Um hash da senha do usuario.
        :param character_id: ID do personagem favorito do usuario.
        :return: Uma mensagem de sucesso e um usuario.
        """

        validate_entry = (
            isinstance(name, str)
            and isinstance(email, str)
            and isinstance(password, str)
        )

        if validate_entry:

            password_hash = self.__hash_password.hash_password(password)

            user_insertion = self.__user_repo.insert_user(
                name=name,
                email=email,
                password_hash=password_hash.decode(),
                character_id=character_id,
            )

            return {"success": validate_entry, "data": user_insertion}

        raise HttpBadRequestError(
            message="Esta requisiçao necessita dos parametros:\
            'name', 'email', 'password'"
        )
