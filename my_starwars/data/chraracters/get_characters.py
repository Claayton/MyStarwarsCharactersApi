"""Caso de uso: GetCharacter"""
from typing import Type, Dict, List
from my_starwars.data.interfaces import CharacterRepoInterface
from my_starwars.domain.usecases import GetCharacterInterface
from my_starwars.domain.models import Character


class GetCharacter(GetCharacterInterface):
    """
    Classe responsavel por buscar personagens de starwars no banco de dados.
    """

    def __init__(
        self,
        character_repo: Type[CharacterRepoInterface],
    ) -> None:
        self.__character_repo = character_repo

    def by_id(self, character_id: int) -> Dict[bool, Character]:
        """
        Realiza a busca dos dados de personagens starwars no banco de dados.
        :param character_id: ID do personagem.
        :return: Personagens de starswars e suas principais caracteristicas.
        """

        response = []
        validate_entry = isinstance(character_id, int)

        if validate_entry:
            response = self.__character_repo.select_character(character_id=character_id)

        return {"success": validate_entry, "data": response}

    def by_name(self, name: str) -> Dict[bool, Character]:
        """
        Realiza a busca dos dados de personagens starwars no banco de dados.
        :param name: nome do personagem.
        :return: Personagens de starswars e suas principais caracteristicas.
        """

        response = None
        validate_entry = isinstance(name, str)

        if validate_entry:
            response = self.__character_repo.select_character(name=name)

        return {"success": validate_entry, "data": response}

    def all_characters(self) -> Dict[bool, List[Character]]:
        """
        Realiza a busca dos dados de personagens starwars no banco de dados.
        :return: Personagens de starswars e suas principais caracteristicas.
        """

        response = None
        validate_entry = True

        if validate_entry:
            response = self.__character_repo.select_character(all_characters=True)

        return {"success": validate_entry, "data": response}
