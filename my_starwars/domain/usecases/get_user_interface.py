"""Arquivo de interface para GetUser"""
from abc import ABC, abstractmethod
from typing import Dict
from my_starwars.domain.models import User


class GetUserInterface(ABC):
    """Interface para a classe GetUser"""

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Dict[bool, User]:
        """Deve ser implementado"""

        raise Exception("Must implement get_user_by_id")

    @abstractmethod
    def get_user_by_name(self, name: str) -> Dict[bool, User]:
        """Deve ser implementado"""

        raise Exception("Must implement get_user_by_name")

    @abstractmethod
    def get_user_by_email(self, email: str) -> Dict[bool, User]:
        """Deve ser implementado"""

        raise Exception("Must implement get_user_by_email")
