"""Arquivo de interface para a CharacterRepo"""
from abc import ABC, abstractmethod
from my_starwars.domain.models import Character


class CharacterRepoInterface(ABC):
    """Interface para a classe CharacterRepo"""

    @abstractmethod
    def insert_character(
        self,
        name: str,
        height: str,
        mass: str,
        hair_color: str,
        skin_color: str,
        eye_color: str,
        birth_year: str,
        gender: str,
    ) -> Character:
        """Deve ser implementado"""

        raise Exception("Must implement insert_characters")

    @abstractmethod
    def select_character(
        self,
        name: str = None,
        character_id: int = None,
        all_characters: bool = False,
    ) -> Character:
        """Deve ser implementado"""

        raise Exception("Must implement select_character")
