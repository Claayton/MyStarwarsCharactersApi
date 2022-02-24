"""Arquivo de interface para a StarWarsCharactersConsumer"""
from abc import ABC, abstractmethod
from typing import Type, Dict, Tuple
from requests import Request


class StarWarsCharactersConsumerInterface(ABC):
    """Interface para a classe StarWarsCharactersConsumer"""

    @abstractmethod
    def get_characters(self, page: int) -> Tuple[int, Type[Request], Dict]:
        """Deve ser implementado"""

        raise Exception("Must implement get_characters")
