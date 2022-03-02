"""Testes para a classe UpdateUser"""
from faker import Faker
from my_starwars.infra.tests import UserRepoSpy
from .update_user import UpdateUser

fake = Faker()


def test_update():
    """Testando o metodo register"""

    user_repo = UserRepoSpy()
    update_user = UpdateUser(user_repo)

    user_id = fake.random_number(digits=3)
    name = fake.name()
    email = f"{name}@test.com"
    character_id = fake.random_number(digits=1)

    response = update_user.update(
        user_id=user_id, name=name, email=email, character_id=character_id
    )

    # Testando se os parametros passados sao diferentes dos ja cadastrados:
    assert user_repo.updated_user_params["user_id"] == user_id
    assert user_repo.updated_user_params["name"] == name
    assert user_repo.updated_user_params["email"] == email
    assert user_repo.updated_user_params["character_id"] == character_id

    assert (
        user_repo.updated_user_params["user_id"]
        != user_repo.before_update_user_params["user_id"]
    )
    assert (
        user_repo.updated_user_params["name"]
        != user_repo.before_update_user_params["name"]
    )
    assert (
        user_repo.updated_user_params["email"]
        != user_repo.before_update_user_params["email"]
    )
    assert (
        user_repo.updated_user_params["character_id"]
        != user_repo.before_update_user_params["character_id"]
    )

    # Testando a saida:
    assert response["success"] is True
    assert response["data"] is not None
