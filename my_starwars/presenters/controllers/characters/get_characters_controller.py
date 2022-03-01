"""Controllers para GetCharacters"""
from typing import Type, List
from my_starwars.errors import HttpUnprocessableEntity, HttpBadRequestError
from my_starwars.presenters.helpers import HttpRequest, HttpResponse
from my_starwars.presenters.interfaces import ControllerInterface
from my_starwars.domain.usecases import (
    GetCharacterInterface as GetCharacter,
)


class GetCharactersController(ControllerInterface):
    """Controller para o caso de uso GetCharacters"""

    def __init__(self, usecase: Type[GetCharacter]) -> None:
        self.__usecase = usecase

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        response = self.__usecase.all_characters()

        if not response["data"]:

            raise HttpBadRequestError(message="Nenhum personagem encontrado!")

        formated_response = self.__format_response(response["data"])

        return formated_response

    @classmethod
    def __format_response(cls, response_method: list) -> HttpResponse:
        """Formatando a resposta"""

        full_response = []

        for character in response_method:

            full_response.append(
                {
                    "id": character.id,
                    "name": character.name,
                    "height": character.height,
                    "mass": character.mass,
                    "hair_color": character.hair_color,
                    "skin_color": character.skin_color,
                    "eye_color": character.eye_color,
                    "birth_year": character.birth_year,
                    "gender": character.gender,
                }
            )

        response = {"message": "Usuarios encontrados!", "data": full_response}

        return HttpResponse(status_code=200, body=response)
