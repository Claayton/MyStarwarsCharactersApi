"""Controllers para GetCharacter"""
from typing import Type, List
from my_starwars.errors import HttpUnprocessableEntity, HttpBadRequestError
from my_starwars.presenters.helpers import HttpRequest, HttpResponse
from my_starwars.presenters.interfaces import ControllerInterface
from my_starwars.domain.usecases import (
    GetCharacterInterface as GetCharacter,
)


class GetCharacterController(ControllerInterface):
    """Controller para o caso de uso GetCharacter"""

    def __init__(self, usecase: Type[GetCharacter]) -> None:
        self.__usecase = usecase

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        response = None

        if http_request.query:

            query_string_params = http_request.query.keys()

            if "id" in query_string_params:

                character_id = http_request.query["id"]
                response = self.__usecase.by_id(character_id=character_id)

            elif "name" in query_string_params:

                name = http_request.query["name"]
                response = self.__usecase.by_name(name=name)

            if response["success"] is False:
                raise HttpUnprocessableEntity(
                    message="Essa requisiçao necessita de um do query_parametros:\
                    ('id': int, 'name': str)"
                )

            formated_response = self.__format_response(response)
            return formated_response

        raise HttpBadRequestError(
            message="Essa requisiçao necessita de um do query_parametros:\
            ('id': int, 'name': str)"
        )

    @classmethod
    def __format_response(cls, method_response: List) -> HttpResponse:

        response = method_response

        return HttpResponse(status_code=200, body=response["data"])
