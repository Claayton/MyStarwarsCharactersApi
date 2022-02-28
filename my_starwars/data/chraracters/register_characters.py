"""Caso de uso: RegisterCharacters"""
from typing import Type, Dict, List
from my_starwars.data.interfaces import CharacterRepoInterface
from my_starwars.domain.usecases import RegisterCharacterInterface
from my_starwars.domain.usecases import StarwarsCharactersColectorInterface


class RegisterCharacter(RegisterCharacterInterface):
    """
    Classe responsavel por registrar todos os personagem vindos da API externa no banco de dados.
    """

    def __init__(
        self,
        colector: Type[StarwarsCharactersColectorInterface],
        character_repo: Type[CharacterRepoInterface],
    ) -> None:
        self.__colector = colector
        self.__character_repo = character_repo

    def register_characters(self) -> Dict[bool, List[Dict]]:
        """
        Realiza o registro dos dados recebidos da API de starwars.
        :return: Todos os personagens de starswars e suas principais caracteristicas.
        """

        characters_data = self.__colector.starwars_characters_colector()["data"]

        response = []

        try:

            for character in characters_data:

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
