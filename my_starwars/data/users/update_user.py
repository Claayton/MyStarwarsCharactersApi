"""Caso de uso: UpdateUser"""
from typing import Type, Dict
from my_starwars.domain.models import User
from my_starwars.domain.usecases import UpdateUserInterface
from my_starwars.data.interfaces import UserRepoInterface


class UpdateUser(UpdateUserInterface):
    """Classe responsavel pela atualização de dados do usuarios no sistema"""

    def __init__(self, user_repo: Type[UserRepoInterface]) -> None:
        self.__user_repo = user_repo

    def update(
        self, user_id: int, name: str, email: str, character_id: int
    ) -> Dict[bool, User]:
        """
        Classe responsavel por realizar a atualização dos dados de um usuário cadastrado no sistema.
        :param user_id: ID do usuario.
        :param name: Nome do usuario.
        :param email: Email do usuario.
        :param character_id: ID do personagem favorito do usuário.
        :return: Uma mensagem de sucesso e um usuario.
        """

        response = None

        validate_entry = (
            isinstance(user_id, int)
            and isinstance(name, str)
            and isinstance(email, str)
            and isinstance(character_id, int)
        )

        if validate_entry:

            response = self.__user_repo.update_user(
                user_id=user_id, name=name, email=email, character_id=character_id
            )

        return {"success": validate_entry, "data": response}
