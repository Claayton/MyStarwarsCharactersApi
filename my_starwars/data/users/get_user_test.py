"""Testes para a classe GetUser"""
from faker import Faker
from my_starwars.infra.tests import UserRepoSpy
from .get_user import GetUser

fake = Faker()


def test_get_user_by_id():
    """Testando o metodo get_user_by_id"""

    user_repo = UserRepoSpy()
    get_user = GetUser(user_repo)

    user_id = fake.random_number()

    response = get_user.get_user_by_id(user_id=user_id)

    # Testando a entrada:
    assert user_repo.insert_user_params["user_id"] == user_id

    # Testando a saida:
    assert response["success"] is True
    assert response["data"] is not None


def test_get_user_by_id_error():
    """
    Testando o erro no metodo get_user_by_id.
    Utilizando um valor invalido para o parametro user_id
    """

    user_repo = UserRepoSpy()
    get_user = GetUser(user_repo)

    user_id = fake.name()

    response = get_user.get_user_by_id(user_id=user_id)

    # Testando a entrada:
    assert not user_repo.insert_user_params

    # Testando a saida:
    assert response["success"] is False
    assert response["data"] is None


def test_get_user_by_name():
    """Testando o metodo get_user_by_name"""

    user_repo = UserRepoSpy()
    get_user = GetUser(user_repo)

    name = fake.name()

    response = get_user.get_user_by_name(name=name)

    # Testando a entrada:
    assert user_repo.insert_user_params["name"] == name

    # Testando a saida:
    assert response["success"] is True
    assert response["data"] is not None


def test_get_user_by_name_error():
    """
    Testando o erro no metodo get_user_by_name.
    Utilizando um valor invalido para o parametro name
    """

    user_repo = UserRepoSpy()
    get_user = GetUser(user_repo)

    name = fake.random_number()

    response = get_user.get_user_by_name(name=name)

    # Testando a entrada:
    assert not user_repo.insert_user_params

    # Testando a saida:
    assert response["success"] is False
    assert response["data"] is None


def test_get_user_by_email():
    """Testando o metodo get_user_by_email"""

    user_repo = UserRepoSpy()
    get_user = GetUser(user_repo)

    email = f"{fake.name()}@test.com"

    response = get_user.get_user_by_email(email=email)

    # Testando a entrada:
    assert user_repo.insert_user_params["email"] == email

    # Testando a saida:
    assert response["success"] is True
    assert response["data"] is not None


def test_get_user_by_email_error():
    """
    Testando o erro no metodo get_user_by_email.
    Utilizando um valor invalido para o parametro email
    """

    user_repo = UserRepoSpy()
    get_user = GetUser(user_repo)

    email = fake.random_number()

    response = get_user.get_user_by_email(email=email)

    # Testando a entrada:
    assert not user_repo.insert_user_params

    # Testando a saida:
    assert response["success"] is False
    assert response["data"] is None
