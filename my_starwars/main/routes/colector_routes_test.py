"""Testes para a rota get_starwars_characters"""
from fastapi.testclient import TestClient
from .colector_routes import colector

client = TestClient(colector)


def test_get_starwars_characters():
    """Testando a rota get_starwars_characters"""

    url = "api/colector/characters/"

    response = client.get(url=url)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert isinstance(response.json()["data"], list)
    assert isinstance(response.json()["data"][0], dict)
    assert "name" in response.json()["data"][0]
    assert "eye_color" in response.json()["data"][0]
