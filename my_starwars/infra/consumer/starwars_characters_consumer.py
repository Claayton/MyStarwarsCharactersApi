"""Arquivo responsavel por consumir a API externa de personages StarWars"""
from typing import Type, Tuple, Dict
from collections import namedtuple
from requests import Request, Session
from my_starwars.errors import HttpRequestError
from my_starwars.data.interfaces import StarWarsCharactersConsumerInterface


class StarWarsCharactersConsumer(StarWarsCharactersConsumerInterface):
    """
    Classe responsavel pelo consumo da API externa de personagens StarWars
    """

    def __init__(self, url: str) -> None:
        self.__url = url
        self.__get_characters_response = namedtuple(
            "GET_Characters", "status_code request response"
        )

    def get_characters(self, page: int) -> Tuple[int, Type[Request], Dict]:
        """
        Realiza a requisicao para a API do starwars.
        :return: Uma tupla nomeada com os atributos:
            status_code: O status da resposta,
            request: A requisição http enviada,
            response: Uma lista com todos os países encontrados na resposta da API.
        """

        request = Request(method="GET", url=self.__url, params={"page": page})
        request_prepared = request.prepare()

        response = self.__send_http_request(request_prepared)
        status_code = response.status_code

        if (status_code < 200) or (status_code > 299):
            raise HttpRequestError(message=response, status_code=status_code)

        return self.__get_characters_response(
            status_code=status_code, request=request, response=response.json()
        )

    @classmethod
    def __send_http_request(cls, request_prepared: Type[Request]) -> any:
        """
        Prepara a secao e envia a requisicao http.
        :param request_prepared: Objeto de requisição com todos os parametros.
        :return: A resposta da requisicao http.
        """

        http_session = Session()
        response = http_session.send(request_prepared)

        return response
