"""Testes para a classe getCharacter"""
from faker import Faker
from my_starwars.infra.tests import CharacterRepoSpy
from my_starwars.domain.models import Character
from .get_characters import GetCharacter

fake = Faker()


def test_by_id():
    """Testando o metodo by_id"""

    infra = CharacterRepoSpy()
    usecase = GetCharacter(infra)

    character_id = fake.random_number(digits=2)
    response = usecase.by_id(character_id=character_id)

    assert response["success"] is True
    assert isinstance(response["data"], Character)
    assert response["data"].name
    assert response["data"].eye_color


def test_by_id_error():
    """
    Testando o erro no metodo by_id.
    Utilizando um valor invalido para o parametro character_id.
    """

    infra = CharacterRepoSpy()
    usecase = GetCharacter(infra)

    character_id = fake.name()
    response = usecase.by_id(character_id=character_id)

    assert response["success"] is False
    assert not response["data"]


def test_by_name():
    """Testando o metodo by_name"""

    infra = CharacterRepoSpy()
    usecase = GetCharacter(infra)

    name = fake.name()
    response = usecase.by_name(name=name)

    assert response["success"] is True
    assert isinstance(response["data"], Character)
    assert response["data"].name
    assert response["data"].eye_color


def test_by_name_error():
    """
    Testando o erro no metodo by_name.
    Utilizando um valor invalido para o parametro name.
    """

    infra = CharacterRepoSpy()
    usecase = GetCharacter(infra)

    name = fake.random_number(digits=3)
    response = usecase.by_name(name=name)

    assert response["success"] is False
    assert not response["data"]


def test_all_characters():
    """Testando o metodo all_characters"""

    infra = CharacterRepoSpy()
    usecase = GetCharacter(infra)

    response = usecase.all_characters()

    assert response["success"] is True
    assert isinstance(response["data"], list)
    assert response["data"][0].name
    assert response["data"][0].eye_color
