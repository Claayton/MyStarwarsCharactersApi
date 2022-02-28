"""Arquivo de interface para RegisterCharacter"""
from abc import ABC, abstractmethod
from typing import Dict, List


class RegisterCharacterInterface(ABC):
    """Interface para a classe RegisterCharacter"""

    @abstractmethod
    def register_characters(self) -> Dict[bool, List[Dict]]:
        """Deve ser implementado"""

        raise Exception("Must implement register_characters")
