"""Arquivo de spy da classe HashPassword"""
import bcrypt
from my_starwars.domain.usecases import HashPasswordInterface


class HashPasswordSpy(HashPasswordInterface):
    """Spy para HashPassword"""

    def __init__(self) -> None:
        self.hash_password_params = {}
        self.verify_password_params = {}

    def hash_password(self, password: str) -> str:
        """Realiza o procesos de hash da senha"""

        self.hash_password_params["password"] = password

        hashed = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())

        return hashed

    def verify_password(self, password: str, password_hashed: str) -> bool:
        """Realiza a verificaçao se a senha passada é a mesma da senha cadastrada"""

        self.verify_password_params["password"] = password
        self.verify_password_params["password_hashed"] = password_hashed

        is_hashed = (
            bcrypt.hashpw(password.encode("utf8"), password_hashed) == password_hashed
        )
        is_hashed = True

        return is_hashed
