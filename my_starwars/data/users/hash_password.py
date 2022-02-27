"""Caso de uso: HashPassword"""
import bcrypt
from my_starwars.domain.usecases import HashPasswordInterface


class HashPassword(HashPasswordInterface):
    """Classe responsavel por realizar o hash de senhas de usuarios"""

    def __init__(self) -> None:
        pass

    @classmethod
    def hash_password(cls, password: str) -> str:
        """Realiza o procesos de hash da senha"""

        hashed = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())

        return hashed

    @classmethod
    def verify_password(cls, password: str, password_hashed: str) -> bool:
        """Realiza a verificaçao se a senha passada é a mesma da senha cadastrada"""

        is_hashed = (
            bcrypt.hashpw(password.encode("utf8"), password_hashed) == password_hashed
        )

        return is_hashed
