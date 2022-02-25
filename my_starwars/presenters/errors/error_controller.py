"""Lógica para tratamento de erros"""
from typing import Type, Dict
from my_starwars.presenters.helpers.http_models import HttpResponse
from my_starwars.errors import HttpRequestError, HttpBadRequestError


def handler_errors(error: Type[Exception]) -> Dict:
    """
    Handler para tratamentos de exeçoes.
    :param error: Tipo de error gerado.
    :return: Um dicionario com o status_code e uma mensagem para esse tipo de erro.
    """

    if isinstance(error, (HttpRequestError, HttpBadRequestError)):
        http_response = HttpResponse(
            status_code=error.status_code, body={"error": str(error)}
        )

    else:
        http_response = HttpResponse(status_code=50, body={"error": str(error)})

    return http_response
