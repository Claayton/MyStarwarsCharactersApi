"""Arquivo de spy da classe CharacterRepo"""
from faker import Faker
from my_starwars.data.interfaces import CharacterRepoInterface
from my_starwars.domain.models import Character

fake = Faker()


class CharacterRepoSpy(CharacterRepoInterface):
    """Spy para RegisterCharacters"""

    def __init__(self) -> None:
        self.insert_character_params = {}
        self.select_character_params = {}

    def insert_character(
        self,
        name: str,
        height: float,
        mass: float,
        hair_color: str,
        skin_color: str,
        eye_color: str,
        birth_year: str,
        gender: str,
    ) -> Character:
        """
        Realiza o cadastro de personagens no banco de dados.
        :param name: Nome do personagem.
        :param height: Altura do personagem.
        :param mass: Peso do personagem.
        :param hair_color: Cor do cabelo do personagem.
        :param skin_color: Cor da pele do personagem.
        :param eye_color: Cor dos olhos do personagem.
        :param birth_year: Ano de nascimento do personagem.
        "param gender: Genero do personagem.
        :return: Uma tupla nomeada com todos os dados do usuario cadastrado.
        """

        self.insert_character_params["name"] = name
        self.insert_character_params["height"] = height
        self.insert_character_params["mass"] = mass
        self.insert_character_params["hair_color"] = hair_color
        self.insert_character_params["skin_color"] = skin_color
        self.insert_character_params["eye_color"] = eye_color
        self.insert_character_params["birth_year"] = birth_year
        self.insert_character_params["namgendere"] = gender

        return Character(
            id=fake.random_number(),
            name=fake.name(),
            height=fake.random_number(),
            mass=fake.random_number(),
            hair_color=fake.word(),
            skin_color=fake.word(),
            eye_color=fake.word(),
            birth_year=fake.word(),
            gender=fake.word(),
        )

    def select_character(
        self,
        name: str = None,
        character_id: int = None,
        all_characters: bool = False,
    ) -> Character:
        """
        Realiza o registro dos dados recebidos da API de starwars.
        :return: Todos os personagens de starswars e suas principais caracteristicas.
        """

        self.select_character_params["name"] = name
        self.select_character_params["character_id"] = character_id
        self.select_character_params["all_characters"] = all_characters

        return [
            Character(
                id=fake.random_number(),
                name=fake.name(),
                height=fake.random_number(),
                mass=fake.random_number(),
                hair_color=fake.word(),
                skin_color=fake.word(),
                eye_color=fake.word(),
                birth_year=fake.word(),
                gender=fake.word(),
            )
        ]
