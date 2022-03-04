"""Arquivo de rotas de usuario"""
from fastapi import APIRouter, Depends, Request as RequestFastApi
from fastapi.responses import JSONResponse
from my_starwars.validators import (
    register_user_validator,
    get_user_validator,
    update_user_validator,
)
from my_starwars.main.routes.middleware import middleware_testing
from my_starwars.main.adapters import request_adapter
from my_starwars.presenters.errors import handler_errors
from my_starwars.data.auth import Authorization
from my_starwars.data.users import GetUser
from my_starwars.infra.database.repo import UserRepo
from my_starwars.infra.tests import UserRepoSpy, CharacterRepoSpy
from my_starwars.config import CONNECTION_STRING
from my_starwars.main.composers import (
    register_user_composer,
    get_user_composer,
    update_user_composer,
)

auth = Authorization(GetUser(UserRepo(CONNECTION_STRING)))

user = APIRouter(prefix="/api/user", tags=["user"])


@user.get("/", dependencies=[Depends(auth.token_required)])
async def get_user(request: RequestFastApi):
    """
    Rota para buscar um usuario registrado no sistema.

    Deve receber um dos seguintes query-parameters:
    ('user_id: int', 'name: str', 'email: str'.)

    Requer token de acesso!
    """

    response = None

    try:
        await get_user_validator(request)

        if middleware_testing(request):

            controller = get_user_composer(infra=UserRepoSpy())
            response = await request_adapter(request, controller.handler)

        else:

            controller = get_user_composer()
            response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)


@user.post("/")
async def register_user(request: RequestFastApi):
    """
    Rota para registrar um novo usuario no sistema.

    Deve receber os seguintes body-parameters:
    ('name: str', 'email: str', 'password: any').
    """

    response = None

    try:
        await register_user_validator(request)

        if middleware_testing(request):

            controller = register_user_composer(
                infra=UserRepoSpy(), character_repo=CharacterRepoSpy()
            )
            response = await request_adapter(request, controller.handler)

        else:

            controller = register_user_composer()
            response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)


@user.put("/")
async def update_user(request: RequestFastApi):
    """
    Rota para dados de um usuario ja registrado no sistema.

    Deve receber os body-parameters 'user_id' + um dos seguintes:
    ('name: str', 'email: str', 'character_id: int').
    """

    response = None

    try:
        await update_user_validator(request)

        if middleware_testing(request):

            controller = update_user_composer(infra=UserRepoSpy())
            response = await request_adapter(request, controller.handler)

        else:
            controller = update_user_composer()
            response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)
