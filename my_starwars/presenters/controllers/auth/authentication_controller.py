"""Controllers para Authentication"""
from typing import Type, Dict
from my_starwars.presenters.helpers import HttpRequest, HttpResponse
from my_starwars.errors import HttpBadRequestError, HttpUnprocessableEntity
from my_starwars.domain.usecases import AuthenticationInterface
from my_starwars.presenters.interfaces import ControllerInterface
from my_starwars.data.interfaces import CharacterRepoInterface


class AuthenticationController(ControllerInterface):
    """Controller para o caso de uso Authentication"""

    def __init__(
        self,
        usecase: Type[AuthenticationInterface],
        character_repo: Type[CharacterRepoInterface],
    ) -> None:
        self.__usecase = usecase
        self.__character_repo = character_repo

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        response = None

        if http_request.body:

            body_params = http_request.body.keys()

            if "email" in body_params and "password" in body_params:

                email = http_request.body["email"]
                password = str(http_request.body["password"])

                response = self.__usecase.authentication(email, password)

                formated_response = self.__format_response(response["data"])

                return formated_response

            raise HttpUnprocessableEntity(
                message="Talvez haja algo de errado com as informaçoes passadas."
            )

        raise HttpBadRequestError(
            message="Esta rota necessita dos seguintes parametros:\
            'email: str', 'password: str'"
        )

    def __format_response(self, response_method: Dict) -> HttpResponse:
        """Formatando a resposta"""

        response = {
            "message": "Login efetuado com successo!",
            "data": {
                "Authorization": response_method["Authorization"],
                "exp": str(response_method["exp"]),
                "id": response_method["id"],
                "user": {
                    "id": response_method["user"]["id"],
                    "name": response_method["user"]["name"],
                    "email": response_method["user"]["email"],
                    "favorite starwars character": self.__character_characteristics(
                        response_method["user"]["character_id"]
                    ),
                },
            },
        }

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
