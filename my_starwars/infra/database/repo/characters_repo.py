"""Diretorio de manipulaçao de dados para a tabela Character"""
from sqlalchemy.orm.exc import NoResultFound
from my_starwars.data.interfaces import CharacterRepoInterface
from my_starwars.domain.models import Character
from my_starwars.infra.database.config import DataBaseConnectionHandler
from my_starwars.infra.database.entities import Character as CharacterModel


class CharacterRepo(CharacterRepoInterface):
    """Manipulaçao de dados da tabela Character"""

    def __init__(self, connection_string: str) -> None:
        self.__connection_string = connection_string

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

        with DataBaseConnectionHandler(self.__connection_string) as data_base:

            try:
                new_character = CharacterModel(
                    name=name,
                    height=height,
                    mass=mass,
                    hair_color=hair_color,
                    skin_color=skin_color,
                    eye_color=eye_color,
                    birth_year=birth_year,
                    gender=gender,
                )
                data_base.session.add(new_character)
                data_base.session.commit()

                return Character(
                    id=new_character.id,
                    name=new_character.name,
                    height=new_character.height,
                    mass=new_character.mass,
                    hair_color=new_character.hair_color,
                    skin_color=new_character.skin_color,
                    eye_color=new_character.eye_color,
                    birth_year=new_character.birth_year,
                    gender=new_character.gender,
                )
            except:
                data_base.session.rollback()
                raise
            finally:
                data_base.session.close()

    def select_character(
        self,
        name: str = None,
        character_id: int = None,
        all_characters: bool = False,
    ) -> Character:
        """
        Realiza a busca de um usuário cadastrado no banco de dados.
        Os dados podem ser especificados pelo nome ou pelo id do usuario.
        :param name: Nome do personagem.
        :param character_id: ID do personagem.
        :param all_characters: Caso seja verdadeiro retorna todos os personagens cadastrados.
        :return: Uma tupla nomeada com todos os dados do personagem.
        """

        try:
            query_data = None

            if all_characters:

                with DataBaseConnectionHandler(self.__connection_string) as data_base:

                    query_data = data_base.session.query(CharacterModel).all()

            elif name:

                with DataBaseConnectionHandler(self.__connection_string) as data_base:

                    query_data = (
                        data_base.session.query(CharacterModel)
                        .filter_by(name=name)
                        .one()
                    )

            elif character_id:

                with DataBaseConnectionHandler(self.__connection_string) as data_base:

                    query_data = (
                        data_base.session.query(CharacterModel)
                        .filter_by(id=character_id)
                        .one()
                    )

            return query_data

        except NoResultFound:
            return []
        except Exception as error:
            data_base.session.rollback()
            raise error
        finally:
            data_base.session.close()
