"""Testes para a classe Authorization"""
from faker import Faker
from my_starwars.domain.models import User
from my_starwars.infra.tests import UserRepoSpy
from my_starwars.data.users import GetUser, HashPassword
from . import Authorization, Authentication

fake = Faker()


def test_token_required():
    """Testando o metodo token_required"""

    infra = UserRepoSpy()
    get_user = GetUser(infra)
    hash_password = HashPassword()
    authorization = Authorization(get_user)

    authentication = Authentication(get_user, hash_password)

    email = f"{fake.word()}@test.com"
    password = "voumudaressasenhaumdia"

    authentication_response = authentication.authentication(email, password)
    token = authentication_response["data"]["Authorization"]

    @authorization.token_required
    def eu_tenho_um_token_guys(token):
        "Teste"
        return token

    response = eu_tenho_um_token_guys(token)

    # Testando a entrada:
    # Implementar spy para hash_password

    # Testando a saida:
    assert isinstance(response, dict)
    assert isinstance(response["data"], User)


def test_token_required_error401():
    """Testando o erro no metodo decorator token_required"""

    infra = UserRepoSpy()
    get_user = GetUser(infra)
    authorization = Authorization(get_user)

    @authorization.token_required
    def eu_tenho_um_token_guys(token):
        "Teste"
        return token

    response = eu_tenho_um_token_guys(token="margarina")
    print(response)

    # Testando a entrada:
    # Implementar spy para hash_password

    # Testando a saida:
    assert isinstance(response, dict)
    assert response["success"] is False  # pylint: disable=E1126
    assert "error" in response["data"]  # pylint: disable=E1126
