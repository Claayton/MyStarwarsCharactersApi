"""Arquivo de rotas"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse
from my_starwars.main.adapters import request_adapter
from my_starwars.presenters.errors import handler_errors
from my_starwars.main.composers import (
    register_user_composer,
    get_user_composer,
    get_users_composer,
)
from my_starwars.validators import register_user_validator, get_user_validator

users = APIRouter(prefix="/api/users")


@users.get("/all/")
async def get_users(request: RequestFastApi):
    """Rota para buscar todos os usuarios registrados no sistema"""

    response = None

    try:
        controller = get_users_composer()
        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)


@users.get("/")
async def get_user(request: RequestFastApi):
    """Rota para buscar usuarios registrados no sistema"""

    response = None

    try:
        await get_user_validator(request)
        controller = get_user_composer()
        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)


@users.post("/")
async def register_user(request: RequestFastApi):
    """Rota para registrar usuarios no sistema"""

    response = None

    try:
        await register_user_validator(request)
        controller = register_user_composer()
        response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)
