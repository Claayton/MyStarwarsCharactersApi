"""Testes para a classe CharacterRepo"""
from faker import Faker
from my_starwars.infra.database.config import DataBaseConnectionHandler
from my_starwars.infra.database.entities import Character as CharacterModel
from my_starwars.domain.models import Character
from my_starwars import config
from . import CharacterRepo

fake = Faker()
character_repo = CharacterRepo(config.CONNECTION_STRING)
data_base_connection_handler = DataBaseConnectionHandler(config.CONNECTION_STRING)


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
    heigth = fake.random_number()
    mass = fake.random_number()
    hair_color = fake.word()
    skin_color = fake.word()
    eye_color = fake.word()
    birth_year = str(fake.random_number())
    gender = fake.word()

    data = Character(
        id=character_id,
        name=name,
        heigth=heigth,
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
            id, name, heigth, mass, hair_color, skin_color, eye_color, birth_year, gender\
        ) VALUES (\
            '{character_id}', '{name}', '{heigth}', '{mass}', '{hair_color}',\
                '{skin_color}', '{eye_color}', '{birth_year}', '{gender}'\
        );"
    )

    select_character = character_repo.select_character(character_id=character_id)

    # Testando se as informaçoes enviadas pelo metodo podem ser encontradas no db.
    assert isinstance(select_character, CharacterModel)
    assert select_character.name == data.name
    assert select_character.id == data.id
    engine.execute(f"DELETE FROM characters WHERE name='{name}';")


def test_select_character_by_name():
    """
    Testando o metodo select_character, buscando usuario pelo nome.
    Utilizando um valor valido para o parametro name.
    """

    character_id = fake.random_number(digits=3)
    name = fake.name()
    heigth = fake.random_number()
    mass = fake.random_number()
    hair_color = fake.word()
    skin_color = fake.word()
    eye_color = fake.word()
    birth_year = str(fake.random_number())
    gender = fake.word()

    data = Character(
        id=character_id,
        name=name,
        heigth=heigth,
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
            id, name, heigth, mass, hair_color, skin_color, eye_color, birth_year, gender\
        ) VALUES (\
            '{character_id}', '{name}', '{heigth}', '{mass}', '{hair_color}',\
                '{skin_color}', '{eye_color}', '{birth_year}', '{gender}'\
        );"
    )

    select_character = character_repo.select_character(name=name)

    # Testando se as informaçoes enviadas pelo metodo podem ser encontradas no db.
    assert isinstance(select_character, CharacterModel)
    assert select_character.name == data.name
    assert select_character.id == data.id
    engine.execute(f"DELETE FROM characters WHERE name='{name}';")


def test_select_character_by_name_and_by_id():
    """
    Testando o metodo select_character, buscando usuario pelo id e pelo nome.
    Utilizando valores validos para os parametros character_id e name.
    """

    character_id = fake.random_number(digits=3)
    name = fake.name()
    heigth = fake.random_number()
    mass = fake.random_number()
    hair_color = fake.word()
    skin_color = fake.word()
    eye_color = fake.word()
    birth_year = str(fake.random_number())
    gender = fake.word()

    data = Character(
        id=character_id,
        name=name,
        heigth=heigth,
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
            id, name, heigth, mass, hair_color, skin_color, eye_color, birth_year, gender\
        ) VALUES (\
            '{character_id}', '{name}', '{heigth}', '{mass}', '{hair_color}',\
                '{skin_color}', '{eye_color}', '{birth_year}', '{gender}'\
        );"
    )

    select_character = character_repo.select_character(
        character_id=character_id, name=name
    )

    # Testando se as informaçoes enviadas pelo metodo podem ser encontradas no db.
    assert isinstance(select_character, CharacterModel)
    assert select_character.name == data.name
    assert select_character.id == data.id
    engine.execute(f"DELETE FROM characters WHERE name='{name}';")


def test_select_all_characters():
    """Testando o metodo select_characters, buscando todos os personagens cadastrados."""

    character_id = fake.random_number(digits=3)
    name = fake.name()
    heigth = fake.random_number()
    mass = fake.random_number()
    hair_color = fake.word()
    skin_color = fake.word()
    eye_color = fake.word()
    birth_year = str(fake.random_number())
    gender = fake.word()

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO characters (\
            id, name, heigth, mass, hair_color, skin_color, eye_color, birth_year, gender\
        ) VALUES (\
            '{character_id}', '{name}', '{heigth}', '{mass}', '{hair_color}',\
                '{skin_color}', '{eye_color}', '{birth_year}', '{gender}'\
        );"
    )

    select_character = character_repo.select_character(all_characters=True)

    # Testando se as informaçoes enviadas pelo metodo podem ser encontradas no db.
    assert isinstance(select_character, list)
    assert select_character is not None
    engine.execute(f"DELETE FROM users WHERE name='{name}';")
