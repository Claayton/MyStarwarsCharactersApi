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

    body_params = Validator(
        {
            "name": {"type": "string", "required": True},
            "email": {"type": "string", "required": True},
            "password": {"type": ["string", "integer"], "required": True},
        }
    )

    response = body_params.validate(body)

    if response is False:

        raise HttpUnprocessableEntity(message=body_params.errors)
