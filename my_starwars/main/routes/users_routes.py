"""Arquivo de rotas de usuarios"""
from fastapi import APIRouter, Depends, Request as RequestFastApi
from fastapi.responses import JSONResponse
from my_starwars.main.routes.middleware import middleware_testing
from my_starwars.main.composers import get_users_composer
from my_starwars.presenters.errors import handler_errors
from my_starwars.main.adapters import request_adapter
from my_starwars.data.auth import Authorization
from my_starwars.data.users import GetUser
from my_starwars.infra.database.repo import UserRepo
from my_starwars.infra.tests import UserRepoSpy
from my_starwars.config import CONNECTION_STRING

auth = Authorization(GetUser(UserRepo(CONNECTION_STRING)))

users = APIRouter(prefix="/api/users", tags=["users"])


@users.get("/", dependencies=[Depends(auth.token_required)])
async def get_users(request: RequestFastApi):
    """
    Rota para buscar todos os usuarios registrados no sistema.

    Requer token de acesso!
    """

    response = None

    try:

        if middleware_testing(request):

            controller = get_users_composer(infra=UserRepoSpy())
            response = await request_adapter(request, controller.handler)

        else:
            controller = get_users_composer()
            response = await request_adapter(request, controller.handler)

    except Exception as error:  # pylint: disable=W0703
        response = handler_errors(error)

    return JSONResponse(status_code=response.status_code, content=response.body)
