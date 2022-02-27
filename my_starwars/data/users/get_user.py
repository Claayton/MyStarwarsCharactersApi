"""Caso de uso: GetUser"""
from typing import Type, Dict
from my_starwars.data.interfaces import UserRepoInterface
from my_starwars.domain.models import User
from my_starwars.domain.usecases import GetUserInterface


class GetUser(GetUserInterface):
    """Classe responsavel por buscar usuario que esta cadastrado no db."""

    def __init__(self, user_repo: Type[UserRepoInterface]) -> None:
        self.__user_repo = user_repo

    def get_user_by_id(self, user_id: int) -> Dict[bool, User]:
        """
        Realiza a busca de um usuario no banco de dados pelo id.
        :param user_id: ID do usuario cadastrado.
        :return: Uma mensagem de sucesso e um usuario.
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:

            response = self.__user_repo.select_user(user_id=user_id)

        return {"success": validate_entry, "data": response}

    def get_user_by_name(self, name: str) -> Dict[bool, User]:
        """
        Realiza a busca de um usuario no banco de dados pelo nome.
        :param name: nome do usuario cadastrado.
        :return: Uma mensagem de sucesso e um usuario.
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:

            response = self.__user_repo.select_user(name=name)

        return {"success": validate_entry, "data": response}

    def get_user_by_email(self, email: str) -> Dict[bool, User]:
        """
        Realiza a busca de um usuario no banco de dados pelo email.
        :param email: nome do usuario cadastrado.
        :return: Uma mensagem de sucesso e um usuario.
        """

        response = None
        validate_entry = isinstance(email, str)

        if validate_entry:

            response = self.__user_repo.select_user(email=email)

        return {"success": validate_entry, "data": response}

    def get_users(self) -> Dict[bool, User]:
        """
        Realiza a busca de todos os usuarios cadastrados nobanco de dados.
        :return: Uma mensagem de sucesso e os usuario.
        """

        response = self.__user_repo.select_user(all_users=True)

        return {"success": True, "data": response}
