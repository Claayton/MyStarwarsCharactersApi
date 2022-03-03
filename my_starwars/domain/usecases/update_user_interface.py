"""Arquivo de interface para UpdateUser"""
from abc import ABC, abstractmethod
from typing import Dict
from my_starwars.domain.models import User


class UpdateUserInterface(ABC):
    """Interface para a classe UpdateUser"""

    @abstractmethod
    def update(
        self, user_id: int, name: str, email: str, character_id: int
    ) -> Dict[bool, User]:
        """Deve ser implementado"""

        raise Exception("Must implement update")
