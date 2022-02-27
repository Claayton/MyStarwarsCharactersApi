"""Caso de uso: Authorization"""
from typing import Type
from fastapi import Request, HTTPException
import jwt
from my_starwars.config import SECRET_KEY
from my_starwars.errors import HttpUnauthorized
from my_starwars.domain.usecases import AuthorizationInterface, GetUserInterface


class Authorization(AuthorizationInterface):
    """
    Classe responsavel pela autorizaçao dos usuarios no sistema.
    """

    def __init__(self, get_user: Type[GetUserInterface]) -> None:
        self.__get_user = get_user

    async def token_required(self, request: Request):
        """
        Decorador para funçoes que necessitam de authorizaçao.
        "param token: Token de acesso para a rota.
        """

        try:

            token = request.headers["Authorization"]

        except KeyError as error:
            http_error = HttpUnauthorized(message="Token invalido ou expirado!")
            raise HTTPException(
                status_code=http_error.status_code, detail=http_error.message
            ) from error

        try:

            data = jwt.decode(jwt=token, key=SECRET_KEY, algorithms="HS256")
            current_user = self.__get_user.get_user_by_email(data["email"])

        except Exception:  # pylint: disable=W0703

            http_error = HttpUnauthorized(message="Token invalido ou expirado!")
            return {"success": False, "data": {"error": http_error.message}}

        return current_user
