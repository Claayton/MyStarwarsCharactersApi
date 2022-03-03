"""Controllers para RegisterCharacter"""
from typing import Type
from my_starwars.presenters.helpers import HttpRequest, HttpResponse
from my_starwars.presenters.interfaces import ControllerInterface
from my_starwars.domain.usecases import (
    RegisterCharacterInterface as RegisterCharacter,
)


class RegisterCharacterController(ControllerInterface):
    """Controller para o caso de uso RegisterCharacter"""

    def __init__(self, usecase: Type[RegisterCharacter]) -> None:
        self.__usecase = usecase

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        response = self.__usecase.register_characters()

        if not response["data"]:

            return HttpResponse(
                status_code=201,
                body={
                    "message": "Todos os personagens ja estao cadastrados!",
                    "data": response["data"],
                },
            )

        return HttpResponse(
            status_code=201,
            body={
                "message": "Personagens registrados com successo!",
                "data": response["data"],
            },
        )
