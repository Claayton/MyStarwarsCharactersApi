"""Arquivo de adaptaçao de requisiços para o FastAPI"""
from typing import Callable
from fastapi import Request as RequestFastApi
from my_starwars.presenters.helpers import HttpRequest


async def request_adapter(request: RequestFastApi, callback: Callable):
    """Adaptador de requisiçoes para FastApi"""

    body = None

    try:
        body = await request.json()
    except:  # pylint: disable=W0702
        pass

    http_request = HttpRequest(
        header=request.headers, body=body, query=request.query_params
    )

    http_response = callback(http_request)
    return http_response
