"""Arquivo de rotas"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from my_starwars.config import CONNECTION_STRING_TEST
from my_starwars.infra.database.repo import CharacterRepo, UserRepo
from my_starwars.main.adapters import request_adapter
from my_starwars.presenters.errors import handler_errors
from my_starwars.main.composers import authentication_composer
from my_starwars.validators import authentication_validator
from my_starwars.main.routes.middleware import middleware_testing

auth = APIRouter(prefix="/api/auth", tags=["authentication"])


@auth.post("/")
async def authentication(request: RequestFastApi):
    """Rota para autenticar usuarios registrados no sistema."""

    response = None

    try:

        await authentication_validator(request)

        if middleware_testing(request):

            controller = authentication_composer(
                infra=UserRepo(CONNECTION_STRING_TEST),
                character_repo=CharacterRepo(CONNECTION_STRING_TEST),
            )
            response = await request_adapter(request, controller.handler)

        else:

            controller = authentication_composer()
            response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)
