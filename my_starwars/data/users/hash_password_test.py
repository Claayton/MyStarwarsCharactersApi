"""Testes para a classe RegisterUser"""
from faker import Faker
from .hash_password import HashPassword

fake = Faker()


def test_hash_password():
    """Testando o metodo hash_password"""

    hash_password = HashPassword()

    password = "estaeumasenhadeteste@123"

    hashed_password = hash_password.hash_password(password)

    assert hashed_password != password


def test_verify_password():
    """Testando o metodo verify_password"""

    hash_password = HashPassword()

    password = "estaeumasenhadeteste@123"
    password_hashed = b"$2b$12$gS5XWVaQqbmIkWHeNTsIWO/qmQHMUeObOU8bT6nYjbi47NbCH2QG."

    is_hashed = hash_password.verify_password(password, password_hashed)

    assert is_hashed is True
