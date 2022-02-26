"""Arquivo de interface para a UserRepo"""
from abc import ABC, abstractmethod
from my_starwars.domain.models import User


class UserRepoInterface(ABC):
    """Interface para a classe UserRepo"""

    @abstractmethod
    def insert_user(self, name: str, email: str, password_hash: str) -> User:
        """Deve ser implementado"""

        raise Exception("Must implement insert_user")

    @abstractmethod
    def select_user(self, name: str, user_id) -> User:
        """Deve ser implementado"""

        raise Exception("Must implement select_user")
