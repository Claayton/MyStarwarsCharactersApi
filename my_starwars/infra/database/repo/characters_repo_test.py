"""Testes para a classe CharacterRepo"""
from faker import Faker
from my_starwars.infra.database.config import DataBaseConnectionHandler
from my_starwars.domain.models import Character
from my_starwars.config import CONNECTION_STRING_TEST
from my_starwars.infra.tests import CharacterRepoSpy

fake = Faker()
character_repo = CharacterRepoSpy()
data_base_connection_handler = DataBaseConnectionHandler(CONNECTION_STRING_TEST)


def insert_characters():
    """Testando o metodo insert_user"""

    name = fake.name()
    height = fake.random_number()
    mass = fake.random_number()
    hair_color = fake.word()
    skin_color = fake.word()
    eye_color = fake.word()
    birth_year = str(fake.random_number())
    gender = fake.word()

    engine = data_base_connection_handler.get_engine()

    new_character = character_repo.insert_character(
        name=name,
        height=height,
        mass=mass,
        hair_color=hair_color,
        skin_color=skin_color,
        eye_color=eye_color,
        birth_year=birth_year,
        gender=gender,
    )

    query_character = engine.execute(
        f"SELECT * FROM users WHERE id='{new_character.id}';"
    ).fetchone()

    # Testando se as informaçoes enviadas pelo metodo podem ser encontradas no db.
    assert new_character.id == query_character.id
    assert new_character.name == query_character.name

    engine.execute(f"DELETE FROM users WHERE id='{query_character.id}';")


def test_select_character_by_id():
    """
    Testando o metodo select_character, buscando usuario pelo id.
    Utilizando um valor valido para o parametro character_id.
    """

    character_id = fake.random_number(digits=3)
    name = fake.name()
    height = str(fake.random_number())
    mass = str(fake.random_number())
    hair_color = fake.word()
    skin_color = fake.word()
    eye_color = fake.word()
    birth_year = str(fake.random_number())
    gender = fake.word()

    data = Character(
        id=character_id,
        name=name,
        height=height,
        mass=mass,
        hair_color=hair_color,
        skin_color=skin_color,
        eye_color=eye_color,
        birth_year=birth_year,
        gender=gender,
    )

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO characters (\
            id, name, height, mass, hair_color, skin_color, eye_color, birth_year, gender\
        ) VALUES (\
            '{character_id}', '{name}', '{height}', '{mass}', '{hair_color}',\
                '{skin_color}', '{eye_color}', '{birth_year}', '{gender}'\
        );"
    )

    select_character = character_repo.select_character(character_id=character_id)

    # Testando as entradas.
    assert character_repo.select_character_params["character_id"] == data.id

    # Testando as saidas
    assert isinstance(select_character, Character)
    assert select_character.name
    assert select_character.height
    engine.execute(f"DELETE FROM characters WHERE name='{name}';")


def test_select_character_by_name():
    """
    Testando o metodo select_character, buscando usuario pelo nome.
    Utilizando um valor valido para o parametro name.
    """

    character_id = fake.random_number(digits=3)
    name = fake.name()
    height = str(fake.random_number())
    mass = str(fake.random_number())
    hair_color = fake.word()
    skin_color = fake.word()
    eye_color = fake.word()
    birth_year = str(fake.random_number())
    gender = fake.word()

    data = Character(
        id=character_id,
        name=name,
        height=height,
        mass=mass,
        hair_color=hair_color,
        skin_color=skin_color,
        eye_color=eye_color,
        birth_year=birth_year,
        gender=gender,
    )

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO characters (\
            id, name, height, mass, hair_color, skin_color, eye_color, birth_year, gender\
        ) VALUES (\
            '{character_id}', '{name}', '{height}', '{mass}', '{hair_color}',\
                '{skin_color}', '{eye_color}', '{birth_year}', '{gender}'\
        );"
    )

    select_character = character_repo.select_character(name=name)

    # Testando as entradas.
    assert character_repo.select_character_params["name"] == data.name

    # Testando as saidas
    assert isinstance(select_character, Character)
    assert select_character.name
    assert select_character.height
    engine.execute(f"DELETE FROM characters WHERE name='{name}';")


def test_select_character_by_name_and_by_id():
    """
    Testando o metodo select_character, buscando usuario pelo id e pelo nome.
    Utilizando valores validos para os parametros character_id e name.
    """

    character_id = fake.random_number(digits=3)
    name = fake.name()
    height = str(fake.random_number())
    mass = str(fake.random_number())
    hair_color = fake.word()
    skin_color = fake.word()
    eye_color = fake.word()
    birth_year = str(fake.random_number())
    gender = fake.word()

    data = Character(
        id=character_id,
        name=name,
        height=height,
        mass=mass,
        hair_color=hair_color,
        skin_color=skin_color,
        eye_color=eye_color,
        birth_year=birth_year,
        gender=gender,
    )

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO characters (\
            id, name, height, mass, hair_color, skin_color, eye_color, birth_year, gender\
        ) VALUES (\
            '{character_id}', '{name}', '{height}', '{mass}', '{hair_color}',\
                '{skin_color}', '{eye_color}', '{birth_year}', '{gender}'\
        );"
    )

    select_character = character_repo.select_character(
        character_id=character_id, name=name
    )

    # Testando as entradas.
    assert character_repo.select_character_params["character_id"] == data.id
    assert character_repo.select_character_params["name"] == data.name

    # Testando as saidas
    assert isinstance(select_character, Character)
    assert select_character.name
    assert select_character.height
    engine.execute(f"DELETE FROM characters WHERE name='{name}';")


def test_select_all_characters():
    """Testando o metodo select_characters, buscando todos os personagens cadastrados."""

    character_id = fake.random_number(digits=3)
    name = fake.name()
    height = str(fake.random_number())
    mass = str(fake.random_number())
    hair_color = fake.word()
    skin_color = fake.word()
    eye_color = fake.word()
    birth_year = str(fake.random_number())
    gender = fake.word()

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO characters (\
            id, name, height, mass, hair_color, skin_color, eye_color, birth_year, gender\
        ) VALUES (\
            '{character_id}', '{name}', '{height}', '{mass}', '{hair_color}',\
                '{skin_color}', '{eye_color}', '{birth_year}', '{gender}'\
        );"
    )

    select_character = character_repo.select_character(all_characters=True)

    # Testando se as informaçoes enviadas pelo metodo podem ser encontradas no db.
    assert isinstance(select_character, list)
    assert select_character[0].name
    assert select_character[0].hair_color
    engine.execute(f"DELETE FROM characters WHERE name='{name}';")
