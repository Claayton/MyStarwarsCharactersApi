"""Controllers para Authentication"""
from typing import Type
from my_starwars.presenters.helpers import HttpRequest, HttpResponse
from my_starwars.errors import HttpBadRequestError, HttpUnprocessableEntity
from my_starwars.domain.usecases import AuthenticationInterface
from my_starwars.presenters.interfaces import ControllerInterface


class AuthenticationController(ControllerInterface):
    """Controller para o caso de uso Authentication"""

    def __init__(self, usecase: Type[AuthenticationInterface]) -> None:
        self.__usecase = usecase

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        response = None

        if http_request.body:

            body_params = http_request.body.keys()

            if "email" in body_params and "password" in body_params:

                email = http_request.body["email"]
                password = str(http_request.body["password"])

                response = self.__usecase.authentication(email, password)

                return HttpResponse(status_code=200, body=response)

            raise HttpUnprocessableEntity(
                message="Talvez haja algo de errado com as informaçoes passadas."
            )

        raise HttpBadRequestError(
            message="Esta rota necessita dos seguintes parametros:\
            'email: str', 'password: str'"
        )
