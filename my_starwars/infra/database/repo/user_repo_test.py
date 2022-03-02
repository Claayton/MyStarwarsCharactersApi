"""Testes para a classe UserRepo"""
from string import digits
from faker import Faker
from my_starwars.infra.database.config import DataBaseConnectionHandler
from my_starwars.infra.database.entities import User as UserModel
from my_starwars.domain.models import User
from my_starwars import config
from . import UserRepo

fake = Faker()
user_repo = UserRepo(config.CONNECTION_STRING)
data_base_connection_handler = DataBaseConnectionHandler(config.CONNECTION_STRING)


def test_insert_user():
    """Testando o metodo insert_user"""

    name = fake.name()
    email = f"{fake.word()}@gmail.com"
    password_hash = fake.word()

    engine = data_base_connection_handler.get_engine()

    new_user = user_repo.insert_user(
        name=name, email=email, password_hash=password_hash
    )

    query_user = engine.execute(
        f"SELECT * FROM users WHERE id='{new_user.id}';"
    ).fetchone()

    # Testando se as informaçoes enviadas pelo metodo podem ser encontradas no db.
    assert new_user.id == query_user.id
    assert new_user.name == query_user.name
    assert new_user.email == query_user.email

    engine.execute(f"DELETE FROM users WHERE id='{new_user.id}';")


def test_select_user_by_id():
    """
    Testando o metodo select_user, buscando usuario pelo id.
    Utilizando um valor valido para o parametro user_id.
    """

    user_id = fake.random_number(digits=3)
    name = fake.name()
    email = f"{fake.word()}@gmail.com"
    password_hash = fake.word()

    data = User(id=user_id, name=name, email=email, password_hash=password_hash)

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO users (id, name, email, password_hash)\
            VALUES ('{user_id}', '{name}', '{email}', '{password_hash}');"
    )

    select_user = user_repo.select_user(user_id=user_id)

    # Testando se as informaçoes enviadas pelo metodo podem ser encontradas no db.
    assert isinstance(select_user, UserModel)
    assert select_user == data
    engine.execute(f"DELETE FROM users WHERE name='{name}';")


def test_select_user_by_name():
    """
    Testando o metodo select_user, buscando usuario pelo nome.
    Utilizando um valor valido para o parametro name.
    """

    user_id = fake.random_number(digits=3)
    name = fake.name()
    email = f"{fake.word()}@gmail.com"
    password_hash = fake.word()

    data = User(id=user_id, name=name, email=email, password_hash=password_hash)

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO users (id, name, email, password_hash)\
            VALUES ('{user_id}', '{name}', '{email}', '{password_hash}');"
    )

    select_user = user_repo.select_user(name=name)

    # Testando se as informaçoes enviadas pelo metodo podem ser encontradas no db.
    assert isinstance(select_user, UserModel)
    assert select_user == data
    engine.execute(f"DELETE FROM users WHERE name='{name}';")


def test_select_user_by_name_and_by_id():
    """
    Testando o metodo select_user, buscando usuario pelo nome e id.
    Utilizando valores validos para os parametros name e user_id.
    """

    user_id = fake.random_number(digits=3)
    name = fake.name()
    email = f"{fake.word()}@gmail.com"
    password_hash = fake.word()

    data = User(id=user_id, name=name, email=email, password_hash=password_hash)

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO users (id, name, email, password_hash)\
            VALUES ('{user_id}', '{name}', '{email}', '{password_hash}');"
    )

    select_user = user_repo.select_user(name=name, user_id=user_id)

    # Testando se as informaçoes enviadas pelo metodo podem ser encontradas no db.
    assert isinstance(select_user, UserModel)
    assert select_user == data
    engine.execute(f"DELETE FROM users WHERE name='{name}';")


def test_select_all_users():
    """Testando o metodo select_user, buscando todos os usuarios cadastrados."""

    user_id = fake.random_number(digits=3)
    name = fake.name()
    email = f"{fake.word()}@gmail.com"
    password_hash = fake.word()

    data = User(id=user_id, name=name, email=email, password_hash=password_hash)

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO users (id, name, email, password_hash)\
            VALUES ('{user_id}', '{name}', '{email}', '{password_hash}');"
    )

    select_user = user_repo.select_user(all_users=True)

    # Testando se as informaçoes enviadas pelo metodo podem ser encontradas no db.
    assert isinstance(select_user, list)
    assert data in select_user
    engine.execute(f"DELETE FROM users WHERE name='{name}';")


def test_update_user():
    """Testando o metodo update_user"""

    user_id = fake.random_number(digits=3)
    name = fake.name()
    email = f"{fake.word()}@gmail.com"
    password_hash = fake.word()
    character_id = fake.random_number(digits=1)

    engine = data_base_connection_handler.get_engine()
    engine.execute(
        f"INSERT INTO users (id, name, email, password_hash)\
            VALUES ('{user_id}', '{name}', '{email}', '{password_hash}');"
    )
    before_user = engine.execute(
        f"SELECT * FROM users WHERE id='{user_id}';"
    ).fetchone()

    update_user = user_repo.update_user(
        user_id=user_id,
        name="Neymar Sandy",
        email="neymarJR@gmail.com",
        character_id=character_id,
    )

    after_user = engine.execute(f"SELECT * FROM users WHERE id='{user_id}';").fetchone()

    # Testando se as informaçoes enviadas pelo metodo são as mesmas gravadas no banco.
    assert after_user.id == update_user.id
    assert after_user.name == update_user.name
    assert after_user.email == update_user.email

    # Testando se as informaçoes do banco mudaram apos a execuçao do metodo.
    assert after_user.id == before_user.id
    assert after_user.name != before_user.name
    assert after_user.email != before_user.email

    engine.execute(f"DELETE FROM users WHERE id='{update_user.id}';")
