"""Testes para as rotas de users"""
from fastapi.testclient import TestClient
from faker import Faker
from my_starwars.infra.database.config import DataBaseConnectionHandler
from my_starwars.config import CONNECTION_STRING_TEST
from .users_routes import users

fake = Faker()
client = TestClient(users)
data_base_connection_handler = DataBaseConnectionHandler(CONNECTION_STRING_TEST)


def test_get_users():
    """Testando a rota get_users"""

    user_id = fake.random_number(digits=6)
    name = fake.name()
    email = f"{fake.word()}@test.com"
    password = fake.word()

    url = "/api/users/"
    headers = {
        "Authorization": "$2b$12$CZQnnbX2M6JBYofDYsu.0.Je9QgbkKpY0Jzr8HgqVzdLuUtz57sZK",
        "X-Test": "true",
    }

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO users (id, name, email, password_hash)\
            VALUES ('{user_id}', '{name}', '{email}', '{password}');"
    )

    response = client.get(url=url, headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert "id" in response.json()["data"][0]
    assert "name" in response.json()["data"][0]

    engine.execute(f"DELETE FROM users WHERE name='{name}';")
