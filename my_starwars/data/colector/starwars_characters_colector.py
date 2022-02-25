"""Caso de uso: StarwarsCharactersColector"""
from typing import Type, Dict, List
from my_starwars.errors import HttpRequestError, HttpBadRequestError
from my_starwars.domain.usecases import StarwarsCharactersColectorInterface
from my_starwars.data.interfaces import (
    StarWarsCharactersConsumerInterface as StarWarsCharactersConsumer,
)


class StarwarsCharactersColector(StarwarsCharactersColectorInterface):
    """Classe responsavel por coletar e tratar os dados vindos da API externa"""

    def __init__(self, api_consumer: Type[StarWarsCharactersConsumer]) -> None:
        self.__api_counsumer = api_consumer

    def starwars_characters_colector(self) -> Dict[bool, List[Dict]]:
        """
        Realiza o tratamento dos dados recebidos da API de starwars.
        :return: Todos os personagens de starswars e suas principais caracteristicas.
        """

        people_list = []

        for index in range(1, 20):

            try:

                get_characters = self.__api_counsumer.get_characters(page=index)

            except HttpRequestError:

                break

            except Exception as error:

                raise HttpBadRequestError(message={"error": str(error)}) from error

            for character in get_characters.response["results"]:

                people_list.append(character)

        separete_data = self.__separete_data(people_list)

        return {"success": True, "data": separete_data}

    @classmethod
    def __separete_data(cls, characters_data: List[Dict]) -> List[Dict]:
        """
        Realiza a separação dos dados dos personagens de starwars.
        :param characters_data: Todos os dados coletados dos personagens de starwars.
        :return: Uma lista de dicionarios com apenas as caracteristicas principais dos personagens.
        """

        separete_data = []

        for index, character in enumerate(characters_data):

            try:

                separete_data.append(
                    {
                        "index": index,
                        "name": character["name"],
                        "height": character["height"],
                        "mass": character["mass"],
                        "hair_color": character["hair_color"],
                        "skin_color": character["skin_color"],
                        "eye_color": character["eye_color"],
                        "birth_year": character["birth_year"],
                        "gender": character["gender"],
                    }
                )

            except Exception as error:

                raise HttpBadRequestError(message={"error": str(error)}) from error

        return separete_data
