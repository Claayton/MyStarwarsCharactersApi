"""Controllers para GetUser"""
from typing import Type
from my_starwars.domain.models import User
from my_starwars.errors import HttpBadRequestError
from my_starwars.presenters.helpers import HttpRequest, HttpResponse
from my_starwars.domain.usecases import GetUserInterface
from my_starwars.presenters.interfaces import ControllerInterface


class GetUserController(ControllerInterface):
    """Controller para o caso de uso GetUser"""

    def __init__(self, usecase: Type[GetUserInterface]) -> None:
        self.__usecase = usecase

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Metodo para chamar o caso de uso"""

        response = None

        if http_request.query:

            query_string_params = http_request.query.keys()

            if "user_id" in query_string_params:

                user_id = int(http_request.query["user_id"])
                response = self.__usecase.get_user_by_id(user_id=user_id)

            elif "name" in query_string_params:

                name = http_request.query["name"]
                response = self.__usecase.get_user_by_name(name=name)

            elif "email" in query_string_params:

                email = http_request.query["email"]
                response = self.__usecase.get_user_by_email(email=email)

            else:

                response = {"success": False, "data": None}

            if not response["data"]:

                raise HttpBadRequestError(
                    message="Essa requisiçao exige um dos seguintes parametros:\
                    'user_id: int', 'name: str', 'email: str'"
                )

            formated_response = self.__format_response(response["data"])

            return formated_response

        raise HttpBadRequestError(
            message="Essa requisiçao exige um dos seguintes parametros:\
            'user_id: int', 'name: str', 'email: str'"
        )

    @classmethod
    def __format_response(cls, response_method: Type[User]) -> HttpResponse:
        """Formatando a resposta"""

        response = {
            "message": "Usuario encontrado!",
            "data": {
                "id": response_method.id,
                "name": response_method.name,
                "email": response_method.email,
                "password": "Não mostramos isso aqui!",
            },
        }

        return HttpResponse(status_code=200, body=response)
