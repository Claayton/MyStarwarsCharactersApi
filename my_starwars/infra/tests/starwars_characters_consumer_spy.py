"""Arquivo de spy da classe StarWarsCharactersConsumer"""
from typing import Type, Tuple, Dict
from collections import namedtuple
from requests import Request
from faker import Faker


class StarWarsCharactersConsumerSpy:
    """Spy para StarWarsCharactersConsumer"""

    def __init__(self) -> None:
        self.get_characters_attributes = {"page": []}
        self.__get_characters_response = namedtuple(
            "GET_Characters", "status_code request response"
        )

    def get_characters(self, page: int) -> Tuple[int, Type[Request], Dict]:
        """Mock para get_characters"""

        self.get_characters_attributes["page"].append(page)

        fake = Faker()
        mock_characters = {
            "count": fake.random_number(digits=1),
            "next": fake.word(),
            "previous": fake.word(),
            "results": [
                {
                    "name": fake.name(),
                    "height": fake.random_number(digits=3),
                    "mass": fake.random_number(digits=2),
                    "hair_color": fake.color(),
                    "skin_color": fake.color(),
                    "eye_color": fake.color(),
                    "birth_year": f"{fake.random_number(digits=4)}BBY",
                    "gender": fake.word(),
                }
            ],
        }

        return self.__get_characters_response(
            status_code=200, request=None, response=mock_characters
        )
