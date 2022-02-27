"""Caso de uso: Authorization"""
from typing import Callable, Type
from functools import wraps
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

    def token_required(self, function: Callable):
        """
        Decorador para funçoes que necessitam de authorizaçao.
        "param token: Token de acesso para a rota.
        """

        @wraps(function)
        def decorated(token: str, *args, **kwargs):
            """
            Responsavel por garantir que o usuario tem um token de acesso
            """

            try:

                data = jwt.decode(jwt=token, key=SECRET_KEY, algorithms="HS256")
                current_user = self.__get_user.get_user_by_email(data["email"])

            except Exception:  # pylint: disable=W0703

                http_error = HttpUnauthorized(message="Token invalido ou expirado!")
                return {"success": False, "data": {"error": http_error.message}}

            return function(current_user, *args, **kwargs)

        return decorated
