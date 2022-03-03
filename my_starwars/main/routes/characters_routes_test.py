"""Testes para a rota get_starwars_characters"""
from fastapi.testclient import TestClient
from faker import Faker
from .characters_routes import characters

client = TestClient(characters)
fake = Faker()


def test_get_starwars_characters_external():
    """Testando a rota get_starwars_characters get_starwars_characters_external"""

    url = "api/characters/external/"
    header = {
        "Authorization": "$2b$12$CZQnnbX2M6JBYofDYsu.0.Je9QgbkKpY0Jzr8HgqVzdLuUtz57sZK"
    }

    response = client.get(url=url, headers=header)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert isinstance(response.json()["data"][0], dict)
    assert "name" in response.json()["data"][0]
    assert "eye_color" in response.json()["data"][0]


def test_get_starwars_characters():
    """Testando a rota _get_starwars_characters"""

    url = "api/characters/"
    header = {
        "Authorization": "$2b$12$CZQnnbX2M6JBYofDYsu.0.Je9QgbkKpY0Jzr8HgqVzdLuUtz57sZK"
    }

    response = client.get(url=url, headers=header)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)


def test_register_starwars_characters():
    """Testando a rota register starwars_characters"""

    url = "api/characters/"
    header = {
        "Authorization": "$2b$12$CZQnnbX2M6JBYofDYsu.0.Je9QgbkKpY0Jzr8HgqVzdLuUtz57sZK"
    }

    response = client.post(url=url, headers=header)

    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
