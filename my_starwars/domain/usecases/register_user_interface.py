"""Arquivo de interface para RegisterUser"""
from abc import ABC, abstractmethod
from typing import Dict
from my_starwars.domain.models import User


class RegisterUserInterface(ABC):
    """Interface para a classe RegisterUser"""

    @abstractmethod
    def register(self, name: str, email: str, password: str) -> Dict[bool, User]:
        """Deve ser implementado"""

        raise Exception("Must implement register")
