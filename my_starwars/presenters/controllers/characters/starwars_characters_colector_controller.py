"""Controllers para StarwarsCharactersColector"""
from typing import Type
from my_starwars.presenters.helpers import HttpRequest, HttpResponse
from my_starwars.errors import HttpBadRequestError
from my_starwars.presenters.interfaces import ControllerInterface
from my_starwars.domain.usecases import (
    StarwarsCharactersColectorInterface as StarwarsCharactersColector,
)


class StarwarsCharactersColectorController(ControllerInterface):
    """Controller para o caso de uso StarwarsCharactersColector"""

    def __init__(self, usecase: Type[StarwarsCharactersColector]) -> None:
        self.__usecase = usecase

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        response = self.__usecase.starwars_characters_colector()

        if response["success"] is True:

            return HttpResponse(
                status_code=200,
                body={"message": "Usuarios encontrados!", "data": response["data"]},
            )

        raise HttpBadRequestError(
            message={"error": "Algo inesperado aconteceu nos controllers do servidor!"}
        )
