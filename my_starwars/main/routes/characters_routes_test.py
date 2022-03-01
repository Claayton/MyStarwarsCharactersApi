"""Testes para a rota get_starwars_characters"""
from fastapi.testclient import TestClient
from faker import Faker
from .characters_routes import characters

client = TestClient(characters)
fake = Faker()


def test_get_starwars_characters_external():
    """Testando a rota get_starwars_characters get_starwars_characters_external"""

    url = "api/characters/external/"

    response = client.get(url=url)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert isinstance(response.json()["data"][0], dict)
    assert "name" in response.json()["data"][0]
    assert "eye_color" in response.json()["data"][0]


def test_get_starwars_characters():
    """Testando a rota _get_starwars_characters"""

    url = "api/characters/"

    response = client.get(url=url)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert isinstance(response.json()["data"][0], dict)
    assert "name" in response.json()["data"][0]
    assert "eye_color" in response.json()["data"][0]


def test_register_starwars_characters():
    """Testando a rota register starwars_characters"""

    url = "api/characters/"

    response = client.post(url=url)

    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
