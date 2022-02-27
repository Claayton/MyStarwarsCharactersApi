"""Arquivo de interface para RegisterUser"""
from abc import ABC, abstractmethod


class HashPasswordInterface(ABC):
    """Interface para a classe HashPassword"""

    @classmethod
    @abstractmethod
    def hash_password(cls, password: str) -> str:
        """Deve ser implementado"""

        raise Exception("Must implement hash_password")

    @classmethod
    @abstractmethod
    def verify_password(cls, password: str, password_hashed: str) -> bool:
        """Deve ser implementado"""

        raise Exception("Must implement verify_password")
