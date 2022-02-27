"""Controllers para GetUsers"""
from typing import Type
from my_starwars.errors import HttpBadRequestError
from my_starwars.presenters.helpers import HttpRequest, HttpResponse
from my_starwars.domain.usecases import GetUserInterface
from my_starwars.presenters.interfaces import ControllerInterface


class GetUsersController(ControllerInterface):
    """Controller para o caso de uso Getuser"""

    def __init__(self, usecase: Type[GetUserInterface]) -> None:
        self.__usecase = usecase

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        response = self.__usecase.get_users()

        if not response["data"]:

            raise HttpBadRequestError(message="Nenhum usuario encontrado!")

        formated_response = self.__format_response(response["data"])

        return formated_response

    @classmethod
    def __format_response(cls, response_method: list) -> HttpResponse:
        """Formatando a resposta"""

        full_response = []

        for user in response_method:

            full_response.append(
                {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "password": "Não mostramos isso aqui!",
                }
            )

        response = {"message": "Usuarios encontrados!", "data": full_response}

        return HttpResponse(status_code=200, body=response)
