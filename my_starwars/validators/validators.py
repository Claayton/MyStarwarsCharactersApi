"""Validaçoes para User"""
from cerberus import Validator
from my_starwars.errors import HttpUnprocessableEntity, HttpBadRequestError


async def register_user_validator(request: any) -> bool:
    """Validador para RegisterUser"""

    try:
        body = await request.json()
    except Exception as error:
        raise HttpBadRequestError(
            message="Esta requisiçao necessita dos parametros:\
'name', 'email', 'password'"
        ) from error

    body_params_validator = Validator(
        {
            "name": {"type": "string", "required": True},
            "email": {"type": "string", "required": True},
            "password": {"type": ["string", "integer"], "required": True},
        }
    )

    response = body_params_validator.validate(body)

    if response is False:

        raise HttpUnprocessableEntity(message=body_params_validator.errors)


async def get_user_validator(request: any) -> bool:
    """Validador para GetUser"""

    query_params = dict(request.query_params)
    try:
        query_params["user_id"] = int(query_params["user_id"])
    except KeyError:
        pass
    except Exception as error:
        raise HttpUnprocessableEntity(message=str(error)) from error

    query_params_validator = Validator(
        {
            "user_id": {"type": "integer"},
            "name": {"type": "string"},
            "email": {"type": "string"},
        }
    )

    response = query_params_validator.validate(query_params)

    if response is False:

        raise HttpUnprocessableEntity(message=query_params_validator.errors)


async def update_user_validator(request: any) -> bool:
    """Validador para UpdateUser"""

    try:
        body = await request.json()
    except Exception as error:
        raise HttpBadRequestError(
            message="Esta requisiçao necessita dos parametros:\
'user_id' + um dos seguintes: 'name', 'email', 'character_id'"
        ) from error

    body_params_validator = Validator(
        {
            "user_id": {"type": "integer", "required": True},
            "name": {"type": "string", "required": False},
            "email": {"type": "string", "required": False},
            "character_id": {"type": "integer", "required": False},
        }
    )

    response = body_params_validator.validate(body)

    if response is False:

        raise HttpUnprocessableEntity(message=body_params_validator.errors)


async def authentication_validator(request: any) -> bool:
    """Validador para Authentication"""

    try:
        body = await request.json()
    except Exception as error:
        raise HttpBadRequestError(
            message="Esta requisiçao necessita dos parametros: 'email', 'password'"
        ) from error

    body_params_validator = Validator(
        {
            "email": {"type": "string", "required": True},
            "password": {"type": ["string", "integer"], "required": True},
        }
    )

    response = body_params_validator.validate(body)

    if response is False:

        raise HttpUnprocessableEntity(message=body_params_validator.errors)
