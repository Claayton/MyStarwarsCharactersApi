"""Caso de uso: RegisterCharacters"""
from typing import Type, Dict, List
from my_starwars.domain.models import User
from my_starwars.data.interfaces import CharacterRepoInterface
from my_starwars.domain.usecases import (
    StarwarsCharactersColectorInterface,
    RegisterCharacterInterface,
    GetCharacterInterface,
)


class RegisterCharacter(RegisterCharacterInterface):
    """
    Classe responsavel por registrar todos os personagem vindos da API externa no banco de dados.
    """

    def __init__(
        self,
        colector: Type[StarwarsCharactersColectorInterface],
        character_repo: Type[CharacterRepoInterface],
        get_character: Type[GetCharacterInterface],
    ) -> None:
        self.__colector = colector
        self.__character_repo = character_repo
        self.__get_character = get_character

    def register_characters(self) -> Dict[bool, List[Dict]]:
        """
        Realiza o registro dos dados recebidos da API de starwars.
        :return: Todos os personagens de starswars e suas principais caracteristicas.
        """

        characters_colector_data = self.__colector.starwars_characters_colector()[
            "data"
        ]
        characters_database = self.__get_character.all_characters()["data"]

        if not characters_database:
            characters_database.append(
                User(
                    id=777,
                    name="Clayton",
                    email="clayton#tests.com",
                    password_hash="mudar321",
                )
            )

        response = []

        try:

            for character in characters_colector_data:

                if character["name"] in (
                    character_db.name for character_db in characters_database
                ):
                    continue

                insertion = self.__character_repo.insert_character(
                    character["name"],
                    character["height"],
                    character["mass"],
                    character["hair_color"],
                    character["skin_color"],
                    character["eye_color"],
                    character["birth_year"],
                    character["gender"],
                )
                characters_database.append(
                    User(
                        id=777,
                        name=character["name"],
                        email="clayton#tests.com",
                        password_hash="mudar321",
                    )
                )
                response.append(
                    {
                        "id": insertion.id,
                        "name": insertion.name,
                        "height": insertion.height,
                        "mass": insertion.mass,
                        "hair_color": insertion.hair_color,
                        "skin_color": insertion.skin_color,
                        "eye_color": insertion.eye_color,
                        "birth_year": insertion.birth_year,
                        "gender": insertion.gender,
                    }
                )

        except Exception as error:
            raise error

        return {"success": True, "data": response}
