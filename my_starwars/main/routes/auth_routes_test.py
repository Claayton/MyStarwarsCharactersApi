"""Testes para as rotas de auth"""
from fastapi.testclient import TestClient
from faker import Faker
from my_starwars.infra.database.config import DataBaseConnectionHandler
from my_starwars.config import CONNECTION_STRING
from my_starwars.data.users import HashPassword
from . import auth

fake = Faker()
hash_password = HashPassword()
client = TestClient(auth)
data_base_connection_handler = DataBaseConnectionHandler(CONNECTION_STRING)


def test_authentication():
    """Testando a rota authentication"""

    url = "/api/auth/"
    data = {"email": f"{fake.word()}@test.com", "password": fake.word()}

    user_id = fake.random_number(digits=3)
    name = fake.name()
    email = data["email"]
    password_hash = hash_password.hash_password(data["password"])
    character_id = fake.random_number(digits=1)

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO users (id, name, email, password_hash, character_id)\
            VALUES ('{user_id}', '{name}', '{email}', '{password_hash.decode()}', '{character_id}');"
    )

    response = client.post(url=url, json=data)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["message"] is not None
    assert isinstance(response.json()["data"], dict)
    assert "Authorization" in response.json()["data"]
    assert "exp" in response.json()["data"]
    assert "user" in response.json()["data"]

    engine.execute(f"DELETE FROM users WHERE name='{name}';")
