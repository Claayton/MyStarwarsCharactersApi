"""Arquivo de rotas"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from my_starwars.main.adapters import request_adapter
from my_starwars.presenters.errors import handler_errors
from my_starwars.main.composers import (
    starwars_characters_colector_composer,
    register_character_composer,
    get_character_composer,
)

characters = APIRouter(prefix="/api/characters")


@characters.get("/")
async def get_starwars_characters(request: RequestFastApi):
    """Rota para buscar os personagens de starwars e seus dados"""

    response = None

    try:

        controller = get_character_composer()
        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)


@characters.get("/direct/")
async def get_starwars_characters_direct(request: RequestFastApi):
    """Rota para buscar os principais dados dos personagens de starwars"""

    response = None

    try:

        controller = starwars_characters_colector_composer()
        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703

        response = handler_errors(error)

    return JSONResponse(
        status_code=response.status_code, content={"data": response.body}
    )


@characters.get("/register/")
async def register_starwars_characters(request: RequestFastApi):
    """Rota para registrar os principais dados de todos os personagens de starwars"""

    response = None

    try:

        controller = register_character_composer()
        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(
        status_code=response.status_code, content={"data": response.body}
    )
