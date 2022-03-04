"""Arquivo de rotas de personagens de starwars"""
from fastapi import APIRouter, Request as RequestFastApi, Depends
from fastapi.responses import JSONResponse
from my_starwars.main.routes.middleware import middleware_testing
from my_starwars.infra.tests import StarWarsCharactersConsumerSpy, CharacterRepoSpy
from my_starwars.data.users import GetUser
from my_starwars.infra.database.repo import UserRepo
from my_starwars.data.auth import Authorization
from my_starwars.config import CONNECTION_STRING
from my_starwars.main.adapters import request_adapter
from my_starwars.presenters.errors import handler_errors
from my_starwars.main.composers import (
    starwars_characters_colector_composer,
    register_character_composer,
    get_character_composer,
)

auth = Authorization(GetUser(UserRepo(CONNECTION_STRING)))

characters = APIRouter(prefix="/api/characters", tags=["characters"])


@characters.get("/external/", dependencies=[Depends(auth.token_required)])
async def get_starwars_characters_external(request: RequestFastApi):
    """
    Rota para buscar os personagens de starwars,
    atravez de uma requisiçao em API externa.
    """

    response = None

    try:

        if middleware_testing(request):

            controller = starwars_characters_colector_composer(
                infra=StarWarsCharactersConsumerSpy()
            )
            response = await request_adapter(request, controller.handler)

        else:

            controller = starwars_characters_colector_composer()
            response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703

        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)


@characters.get("/", dependencies=[Depends(auth.token_required)])
async def get_starwars_characters(request: RequestFastApi):
    """
    Rota para buscar os personagens de starwars,
    que ja estao cadastrados no banco de dados.
    """

    response = None

    try:

        if middleware_testing(request):

            controller = get_character_composer(infra=CharacterRepoSpy())
            response = await request_adapter(request, controller.handler)

        else:

            controller = get_character_composer()
            response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)


@characters.post("/", dependencies=[Depends(auth.token_required)])
async def register_starwars_characters(request: RequestFastApi):
    """
    Rota para registrar os personagens de starwars,
    realiza uma requisiçao externa, coleta os dados e registra no banco de dados,
    caso ainda nao esteja registrado.
    """

    response = None

    try:

        if middleware_testing(request):

            controller = register_character_composer(
                infra_repo=CharacterRepoSpy(),
                infra_consumer=StarWarsCharactersConsumerSpy(),
            )
            response = await request_adapter(request, controller.handler)

        else:

            controller = register_character_composer()
            response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)
