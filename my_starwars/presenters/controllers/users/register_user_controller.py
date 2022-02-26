"""Controllers para RegisterUser"""
from typing import Type
from my_starwars.presenters.helpers import HttpRequest, HttpResponse
from my_starwars.domain.usecases import RegisterUserInterface as RegisterUser
from my_starwars.presenters.interfaces import ControllerInterface
from my_starwars.errors import HttpBadRequestError


class RegisterUserController(ControllerInterface):
    """Controller para o caso de uso RegisterUser"""

    def __init__(self, usecase: Type[RegisterUser]) -> None:
        self.__usecase = usecase

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        response = None

        if http_request.body:

            body_params = http_request.body.keys()

            if (
                "name" in body_params
                and "email" in body_params
                and "password" in body_params
            ):
                name = http_request.body["name"]
                email = http_request.body["email"]
                password = http_request.body["password"]

                response = self.__usecase.register(
                    name=name, email=email, password=password
                )

                return HttpResponse(status_code=201, body=response["data"])

        raise HttpBadRequestError(
            message="Esta rota necessita dos seguintes parametros:\
                'name: str', 'email: str', 'password: str'"
        )
