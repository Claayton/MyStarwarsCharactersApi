"""Testes para a classe RegisterUser"""
from faker import Faker
from my_starwars.infra.database.repo import UserRepo
from my_starwars.config import CONNECTION_STRING
from .register_user import RegisterUser

fake = Faker()


def test_register():
    """Testando o metodo register"""

    user_repo = UserRepo(CONNECTION_STRING)
    register_user = RegisterUser(user_repo)

    name = fake.name()
    email = f"{name}@test.com"
    password_hash = fake.word()

    response = register_user.register(
        name=name, email=email, password_hash=password_hash
    )

    # Testando a entrada:
    # Implementar Spy para testar a entrada

    # Testando a saida:
    assert response["success"] is True
    assert response["data"] is not None
