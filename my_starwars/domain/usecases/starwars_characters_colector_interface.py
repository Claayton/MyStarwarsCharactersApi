"""Arquivo de interface para a StarwarsCharactersColector"""
from abc import ABC, abstractmethod
from typing import Dict, List


class StarwarsCharactersColectorInterface(ABC):
    """Interface para a classe StarwarsCharactersColector"""

    @abstractmethod
    def starwars_characters_colector(self) -> Dict[bool, List[Dict]]:
        """Deve ser implementado"""

        raise Exception("Must implement starwars_characters_colector")
