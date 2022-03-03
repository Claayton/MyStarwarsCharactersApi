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
        self.before_update_user_params = {}
        self.updated_user_params = {}

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
            name=fake.name(),
            email=f"{name}@mock.com",
            password_hash="$2b$12$CZQnnbX2M6JBYofDYsu.0.Je9QgbkKpY0Jzr8HgqVzdLuUtz57sZK",
            character_id=fake.random_number(digits=3),
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
                    name=fake.name(),
                    email=f"{name}@mock.com",
                    password_hash="$2b$12$CZQnnbX2M6JBYofDYsu.0.Je9QgbkKpY0Jzr8HgqVzdLuUtz57sZK",
                    character_id=fake.random_number(digits=3),
                )
            ]

        return User(
            id=fake.random_number(digits=3),
            name=fake.name(),
            email=f"{name}@mock.com",
            password_hash="$2b$12$CZQnnbX2M6JBYofDYsu.0.Je9QgbkKpY0Jzr8HgqVzdLuUtz57sZK",
            character_id=fake.random_number(digits=3),
        )

    def update_user(
        self,
        user_id: int,
        name: str = None,
        email: str = None,
        character_id: int = None,
    ) -> User:
        """
        Classe responsavel por realizar a atualização dos dados de um usuário cadastrado no sistema.
        :param user_id: ID do usuario.
        :param name: Nome do usuario.
        :param email: Email do usuario.
        :param character_id: ID do personagem favorito do usuário.
        :return: Uma mensagem de sucesso e um usuario.
        """

        self.updated_user_params["user_id"] = user_id
        self.updated_user_params["name"] = name
        self.updated_user_params["email"] = email
        self.updated_user_params["character_id"] = character_id

        self.before_update_user_params["user_id"] = fake.random_number(digits=3)
        self.before_update_user_params["name"] = fake.name()
        self.before_update_user_params["email"] = f"{fake.word()}@mock.com"
        self.before_update_user_params["character_id"] = fake.random_number(digits=3)

        return User(
            id=self.before_update_user_params["user_id"],
            name=self.before_update_user_params["name"],
            email=self.before_update_user_params["email"],
            password_hash="$2b$12$CZQnnbX2M6JBYofDYsu.0.Je9QgbkKpY0Jzr8HgqVzdLuUtz57sZK",
            character_id=self.before_update_user_params["character_id"],
        )
