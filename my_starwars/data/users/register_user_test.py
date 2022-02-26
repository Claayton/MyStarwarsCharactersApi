"""Testes para a classe RegisterUser"""
from faker import Faker
from my_starwars.infra.tests import UserRepoSpy
from .register_user import RegisterUser

fake = Faker()


def test_register():
    """Testando o metodo register"""

    user_repo = UserRepoSpy()
    register_user = RegisterUser(user_repo)

    name = fake.name()
    email = f"{name}@test.com"
    password_hash = fake.word()

    response = register_user.register(
        name=name, email=email, password_hash=password_hash
    )

    # Testando a entrada:
    assert user_repo.insert_user_params["name"] == name
    assert user_repo.insert_user_params["email"] == email
    assert user_repo.insert_user_params["password_hash"] == password_hash

    # Testando a saida:
    assert response["success"] is True
    assert response["data"] is not None
