"""Caso de uso: Authentication"""
from typing import Type, Dict
from datetime import datetime, timedelta
import jwt
from my_starwars.config import SECRET_KEY
from my_starwars.errors import HttpUnprocessableEntity
from my_starwars.domain.usecases import GetUserInterface, HashPasswordInterface
from my_starwars.errors.http_error401 import HttpUnauthorized
from my_starwars.domain.usecases import AuthenticationInterface


class Authentication(AuthenticationInterface):
    """
    Classe responsavel pela autenticaçao e autorizaçao dos usuarios no sistema.
    """

    def __init__(
        self,
        get_user: Type[GetUserInterface],
        hash_password: type[HashPasswordInterface],
    ) -> None:
        self.__get_user = get_user
        self.__hash_password = hash_password

    def authentication(self, email: str, password: str) -> Dict[bool, Dict]:
        """
        Realiza autenticaçao de usuarios.
        :return: Uma mensagem de sucesso e um dicionario com informaçoes e um token.
        """

        user = self.__get_user.get_user_by_email(email=email)["data"]
        verify_password = self.__hash_password.verify_password(
            password, user.password_hash
        )

        if not user:
            return HttpUnprocessableEntity(message="Usuario nao cadastrado!")

        if user and verify_password:

            payloads = {
                "exp": datetime.utcnow() + timedelta(hours=12),
                "iat": datetime.utcnow(),
                "email": user.email,
                "name": user.name,
            }

            token = jwt.encode(payload=payloads, key=SECRET_KEY)

            return {
                "success": True,
                "data": {
                    "Authorization": token,
                    "exp": payloads["exp"],
                    "id": user.id,
                    "user": {"id": user.id, "name": user.name, "email": user.email},
                },
            }

        return HttpUnauthorized(message="Erro de authenticaçao!")
