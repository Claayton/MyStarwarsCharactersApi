"""Arquivo de spy da classe UserRepo"""
from faker import Faker
from my_starwars.data.interfaces import UserRepoInterface
from my_starwars.domain.models import User

fake = Faker()


class UserRepoSpy(UserRepoInterface):
    """Spy para UserRepo"""

    def __init__(self) -> None:
        self.insert_user_params = {}
        self.select_user_params = {}

    def insert_user(self, name: str, email: str, password_hash: str) -> User:
        """
        Realiza a inserçao de um novo usuario na tabela User.
        :param name: Nome do usuario.
        :param email: Email do usuario.
        :param password_hash: Hash da senha do usuario.
        :return: Uma tupla nomeada com todos os dados do usuario cadastrado.
        """

        self.insert_user_params["name"] = name
        self.insert_user_params["email"] = email
        self.insert_user_params["password_hash"] = password_hash

        return User(
            id=fake.random_number(digits=3),
            name=fake.name,
            email=f"{name}@mock.com",
            password_hash=fake.word(),
        )

    def select_user(
        self,
        name: str = None,
        user_id: int = None,
        email: str = None,
        all_users: bool = False,
    ) -> User:
        """
        Realiza a busca de um usuário cadastrado no banco de dados.
        Os dados podem ser especificados pelo nome ou pelo id do usuario.
        :param name: Nome do usuario.
        :param user_id: ID do usuario.
        :param email: Email do usuario cadastrado.
        :param all_users: Caso seja verdadeiro retorna todos os usuarios cadastrados.
        :return: Uma tupla nomeada com todos os dados do usuario.
        """

        self.insert_user_params["name"] = name
        self.insert_user_params["user_id"] = user_id
        self.insert_user_params["email"] = email

        if all_users:

            return [
                User(
                    id=fake.random_number(digits=3),
                    name=fake.name,
                    email=f"{name}@mock.com",
                    password_hash=fake.word(),
                )
            ]

        return User(
            id=fake.random_number(digits=3),
            name=fake.name,
            email=f"{name}@mock.com",
            password_hash=fake.word(),
        )
