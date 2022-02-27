"""Testes para a classe Authentication"""
from faker import Faker
from my_starwars.infra.tests import UserRepoSpy
from my_starwars.data.users import GetUser, HashPassword
from .authentication import Authentication

fake = Faker()


def test_authentication():
    """Testando o metodo authentication"""

    infra = UserRepoSpy()
    get_user = GetUser(infra)
    hash_password = HashPassword()
    user_auth = Authentication(get_user, hash_password)

    email = f"{fake.word()}@test.com"
    password = "estaeumasenhadeteste@123"

    response = user_auth.authentication(email, password)

    # Testando a entrada:
    # Implementar spy para hash_password

    # Testando a saida:
    assert isinstance(response, dict)
    assert "exp" in response["data"]
    assert "Authorization" in response["data"]
    assert "user" in response["data"]
