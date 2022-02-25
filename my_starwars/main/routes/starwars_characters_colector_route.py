"""Arquivo de rotas"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from my_starwars.main.adapters import request_adapter
from my_starwars.presenters.errors import handler_errors
from my_starwars.main.composers import starwars_characters_colector_composer

colector = APIRouter(prefix="/api/colector")


@colector.get("/characters/")
async def get_starwars_characters(request: RequestFastApi):
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
