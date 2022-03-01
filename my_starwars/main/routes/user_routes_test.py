"""Testes para as rotas de user"""
from fastapi.testclient import TestClient
from faker import Faker
from my_starwars.infra.database.config import DataBaseConnectionHandler
from my_starwars.config import CONNECTION_STRING
from .user_routes import user

fake = Faker()
client = TestClient(user)
data_base_connection_handler = DataBaseConnectionHandler(CONNECTION_STRING)


def test_get_user_with_name_param():
    """
    Testando a rota get_users.
    Utilizando um valor valido como parametro para name.
    """

    user_id = fake.random_number(digits=6)
    name = fake.name()
    email = f"{fake.word()}@test.com"
    password = fake.word()

    url = "/api/user/"
    params = {"name": name}
    header = {
        "Authorization": "$2b$12$CZQnnbX2M6JBYofDYsu.0.Je9QgbkKpY0Jzr8HgqVzdLuUtz57sZK"
    }

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO users (id, name, email, password_hash)\
            VALUES ('{user_id}', '{name}', '{email}', '{password}');"
    )

    response = client.get(url=url, params=params, headers=header)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], dict)
    assert "id" in response.json()["data"]
    assert "name" in response.json()["data"]

    engine.execute(f"DELETE FROM users WHERE name='{name}';")


def test_get_user_with_email_param():
    """
    Testando a rota get_users.
    Utilizando um valor valido como parametro para email.
    """

    user_id = fake.random_number(digits=6)
    name = fake.name()
    email = f"{fake.word()}@test.com"
    password = fake.word()

    url = "/api/user/"
    params = {"email": email}
    header = {
        "Authorization": "$2b$12$CZQnnbX2M6JBYofDYsu.0.Je9QgbkKpY0Jzr8HgqVzdLuUtz57sZK"
    }

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO users (id, name, email, password_hash)\
            VALUES ('{user_id}', '{name}', '{email}', '{password}');"
    )

    response = client.get(url=url, params=params, headers=header)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], dict)
    assert "id" in response.json()["data"]
    assert "name" in response.json()["data"]

    engine.execute(f"DELETE FROM users WHERE email='{email}';")


def test_get_user_with_user_id_param():
    """
    Testando a rota get_users.
    Utilizando um valor valido como parametro para user_id.
    """

    user_id = fake.random_number(digits=6)
    name = fake.name()
    email = f"{fake.word()}@test.com"
    password = fake.word()

    url = "/api/user/"
    params = {"user_id": user_id}
    header = {
        "Authorization": "$2b$12$CZQnnbX2M6JBYofDYsu.0.Je9QgbkKpY0Jzr8HgqVzdLuUtz57sZK"
    }

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO users (id, name, email, password_hash)\
            VALUES ('{user_id}', '{name}', '{email}', '{password}');"
    )

    response = client.get(url=url, params=params, headers=header)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], dict)
    assert "id" in response.json()["data"]
    assert "name" in response.json()["data"]

    engine.execute(f"DELETE FROM users WHERE id='{user_id}';")


def test_get_user_error400_without_query_params():
    """
    Testando o erro 400 na rota get_users.
    Sem utilizar nenhum parametro.
    """

    user_id = fake.random_number(digits=6)
    name = fake.name()
    email = f"{fake.word()}@test.com"
    password = fake.word()

    url = "/api/user/"
    params = {}
    header = {
        "Authorization": "$2b$12$CZQnnbX2M6JBYofDYsu.0.Je9QgbkKpY0Jzr8HgqVzdLuUtz57sZK"
    }

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO users (id, name, email, password_hash)\
            VALUES ('{user_id}', '{name}', '{email}', '{password}');"
    )

    response = client.get(url=url, params=params, headers=header)

    assert response.status_code == 400
    assert "error" in response.json()

    engine.execute(f"DELETE FROM users WHERE id='{user_id}';")


def test_register_user():
    """Testando a rota register_user"""

    url = "/api/user/"
    data = {
        "name": fake.name(),
        "email": f"{fake.word()}@test.com",
        "password": fake.word(),
    }

    engine = data_base_connection_handler.get_engine()

    response = client.post(url=url, json=data)

    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert response.json()["message"] is not None
    assert isinstance(response.json()["data"], dict)
    assert "name" in response.json()["data"]
    assert "email" in response.json()["data"]
    assert "password" in response.json()["data"]

    name = data["name"]
    engine.execute(f"DELETE FROM users WHERE name='{name}';")


def test_register_user_error422_with_invalid_name_param():
    """
    Testando o erro 422 - Unprocessable Entity na rota register_user.
    Utilizando um valor invalido para o parametro 'name'.
    """

    url = "/api/user/"
    data = {
        "name": fake.random_number(),
        "email": f"{fake.word()}@test.com",
        "password": fake.word(),
    }

    response = client.post(url=url, json=data)

    assert response.status_code == 422
    assert "error" in response.json()


def test_register_user_error422_with_invalid_email_param():
    """
    Testando o erro 422 - Unprocessable Entity na rota register_user.
    Utilizando um valor invalido para o parametro 'email'.
    """

    url = "/api/user/"
    data = {"name": fake.name(), "email": fake.random_number(), "password": fake.word()}

    response = client.post(url=url, json=data)

    assert response.status_code == 422
    assert "error" in response.json()


def test_register_user_error400_without_body_params():
    """
    Testando o erro 400 - Bad Request na rota register_user.
    Utilizando um valor invalido para o parametro 'name'.
    """

    url = "/api/user/"

    response = client.post(url=url)

    assert response.status_code == 400
    assert "error" in response.json()
