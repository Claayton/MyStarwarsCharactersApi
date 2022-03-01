"""Arquivo de rotas de personagens de starwars"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from my_starwars.main.adapters import request_adapter
from my_starwars.presenters.errors import handler_errors
from my_starwars.main.composers import (
    starwars_characters_colector_composer,
    register_character_composer,
    get_character_composer,
)

characters = APIRouter(prefix="/api/characters", tags=["characters"])


@characters.get("/external/")
async def get_starwars_characters_external(request: RequestFastApi):
    """
    Rota para buscar os personagens de starwars,
    atravez de uma requisiçao em API externa.
    """

    response = None

    try:

        controller = starwars_characters_colector_composer()
        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703

        response = handler_errors(error)

    return JSONResponse(
        status_code=response.status_code, content={"data": response.body}
    )


@characters.get("/")
async def get_starwars_characters(request: RequestFastApi):
    """
    Rota para buscar os personagens de starwars,
    que ja estao cadastrados no banco de dados.
    """

    response = None

    try:

        controller = get_character_composer()
        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)


@characters.post("/")
async def register_starwars_characters(request: RequestFastApi):
    """
    Rota para registrar os personagens de starwars,
    realiza uma requisiçao externa, coleta os dados e registra no banco de dados,
    caso ainda nao esteja registrado.
    """

    response = None

    try:

        controller = register_character_composer()
        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(
        status_code=response.status_code, content={"data": response.body}
    )
