"""Testes para a classe UserAuth"""
from faker import Faker
from my_starwars.infra.tests import UserRepoSpy
from my_starwars.data.users import GetUser, HashPassword
from .user_auth import UserAuth

fake = Faker()


def test_authentication():
    """Testando o metodo authentication"""

    infra = UserRepoSpy()
    get_user = GetUser(infra)
    hash_password = HashPassword()
    user_auth = UserAuth(get_user, hash_password)

    email = f"{fake.word()}@test.com"
    password = "estaeumasenhadeteste@123"

    response = user_auth.authentication(email, password)

    # Testando a entrada:
    # Implementar spy para hash_password

    # Testando a saida:
    assert isinstance(response, dict)
    assert "exp" in response
    assert "Authorization" in response
    assert "user" in response
