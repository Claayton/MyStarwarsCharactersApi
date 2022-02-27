"""Arquivo de interface para Authorization"""
from abc import ABC, abstractmethod
from typing import Callable


class AuthorizationInterface(ABC):
    """Interface para a classe Authorization"""

    @abstractmethod
    def token_required(self, function: Callable):
        """Deve ser implementado"""

        raise Exception("Must implement token_required")
