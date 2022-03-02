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
    def select_user(
        self,
        name: str = None,
        user_id: int = None,
        email: str = None,
        all_users: bool = False,
    ) -> User:
        """Deve ser implementado"""

        raise Exception("Must implement select_user")

    @abstractmethod
    def update_user(
        self,
        user_id: int,
        name: str = None,
        email: str = None,
        character_id: int = None,
    ) -> User:
        """Deve ser implementado"""

        raise Exception("Must implement update_user")
