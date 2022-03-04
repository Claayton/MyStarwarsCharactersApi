"""Controllers para GetUsers"""
from typing import Type
from my_starwars.errors import HttpNotFound
from my_starwars.presenters.helpers import HttpRequest, HttpResponse
from my_starwars.domain.usecases import GetUserInterface
from my_starwars.data.interfaces import CharacterRepoInterface
from my_starwars.presenters.interfaces import ControllerInterface


class GetUsersController(ControllerInterface):
    """Controller para o caso de uso Getuser"""

    def __init__(
        self,
        usecase: Type[GetUserInterface],
        character_repo: Type[CharacterRepoInterface],
    ) -> None:
        self.__usecase = usecase
        self.__character_repo = character_repo

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        response = self.__usecase.get_users()

        if not response["data"]:

            raise HttpNotFound(message="Nenhum usuario encontrado!")

        formated_response = self.__format_response(response["data"])

        return formated_response

    def __format_response(self, response_method: list) -> HttpResponse:
        """Formatando a resposta"""

        full_response = []

        for user in response_method:

            full_response.append(
                {
                    "id": user.id,
                    "name": user.name,
                    "email": user.email,
                    "favorite starwars character": self.__character_characteristics(
                        user.character_id
                    ),
                    "password": "Não mostramos isso aqui!",
                }
            )

        response = {"message": "Usuarios encontrados!", "data": full_response}

        return HttpResponse(status_code=200, body=response)

    def __character_characteristics(self, character_id: int):
        """Realiza a busca das caracteristicas do personagem no banco de dados"""

        character = self.__character_repo.select_character(character_id=character_id)

        if not character:
            return None
        response = {
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

        return response
