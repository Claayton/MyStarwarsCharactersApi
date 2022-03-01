"""Arquivo de interface para GetCharacter"""
from abc import ABC, abstractmethod
from typing import Dict, List
from my_starwars.domain.models import Character


class GetCharacterInterface(ABC):
    """Interface para a classe GetCharacter"""

    @abstractmethod
    def by_id(self, character_id: int) -> Dict[bool, Character]:
        """Deve ser implementado"""

        raise Exception("Must implement by_id")

    @abstractmethod
    def by_name(self, name: str) -> Dict[bool, Character]:
        """Deve ser implementado"""

        raise Exception("Must implement by_name")

    @abstractmethod
    def all_characters(self) -> Dict[bool, List[Character]]:
        """Deve ser implementado"""

        raise Exception("Must implement all_characters")
