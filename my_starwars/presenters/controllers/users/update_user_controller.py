"""Controllers para UpdateUser"""
from typing import Type
from my_starwars.errors.http_error422 import HttpUnprocessableEntity
from my_starwars.presenters.helpers import HttpRequest, HttpResponse
from my_starwars.domain.usecases import UpdateUserInterface as UpdateUser
from my_starwars.presenters.interfaces import ControllerInterface
from my_starwars.data.interfaces import CharacterRepoInterface
from my_starwars.domain.models import User


class UpdateUserController(ControllerInterface):
    """Controller para o caso de uso UpdateUser"""

    def __init__(
        self, usecase: Type[UpdateUser], character_repo: Type[CharacterRepoInterface]
    ) -> None:
        self.__usecase = usecase
        self.__character_repo = character_repo

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        response = None
        name = None
        email = None
        character_id = None

        if http_request.body:

            body_params = http_request.body.keys()

        if "user_id" in body_params and (
            "name" in body_params
            or "email" in body_params
            or "character_id" in body_params
        ):

            user_id = http_request.body["user_id"]

            if "name" in body_params:

                name = http_request.body["name"]

            if "email" in body_params:

                email = http_request.body["email"]

            if "character_id" in body_params:

                character_id = http_request.body["character_id"]

            response = self.__usecase.update(
                user_id=user_id, name=name, email=email, character_id=character_id
            )

            formated_response = self.__format_response(response["data"])

            return formated_response

        raise HttpUnprocessableEntity(
            message="Esta rota necessita do parametro 'user_id' + um dos seguintes:\
'name: str', 'email: str', 'password: str'"
        )

    def __format_response(self, response_method: Type[User]) -> HttpResponse:
        """Formatando a resposta"""

        response = {
            "message": "Dados do usuário atualizados com sucesso!",
            "data": {
                "id": response_method.id,
                "name": response_method.name,
                "email": response_method.email,
                "favorite starwars character": self.__character_characteristics(
                    response_method.character_id
                ),
                "password": "Não mostramos isso aqui!",
            },
        }

        return HttpResponse(status_code=201, body=response)

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
