"""Arquivo de interface para UserAuth"""
from abc import ABC, abstractmethod


class UserAuthInterface(ABC):
    """Interface para a classe UserAuth"""

    @abstractmethod
    def authentication(self, email: str, password: str):
        """Deve ser implementado"""

        raise Exception("Must implement authentication")
