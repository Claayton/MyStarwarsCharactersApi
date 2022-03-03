"""Controllers para UpdateUser"""
from typing import Type
from my_starwars.errors.http_error422 import HttpUnprocessableEntity
from my_starwars.presenters.helpers import HttpRequest, HttpResponse
from my_starwars.domain.usecases import UpdateUserInterface as UpdateUser
from my_starwars.presenters.interfaces import ControllerInterface
from my_starwars.errors import HttpBadRequestError
from my_starwars.domain.models import User


class UpdateUserController(ControllerInterface):
    """Controller para o caso de uso UpdateUser"""

    def __init__(self, usecase: Type[UpdateUser]) -> None:
        self.__usecase = usecase

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

    @classmethod
    def __format_response(cls, response_method: Type[User]) -> HttpResponse:
        """Formatando a resposta"""

        response = {
            "message": "Dados do usuário atualizados com sucesso!",
            "data": {
                "id": response_method.id,
                "name": response_method.name,
                "email": response_method.email,
                "character_id": response_method.character_id,
                "password": "Não mostramos isso aqui!",
            },
        }

        return HttpResponse(status_code=201, body=response)
