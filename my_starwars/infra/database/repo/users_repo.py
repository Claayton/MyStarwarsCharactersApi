"""Diretorio de manipulaçao de dados para a tabela User"""
from sqlalchemy.orm.exc import NoResultFound
from my_starwars.data.interfaces.users_repo_interface import UserRepoInterface
from my_starwars.domain.models import User
from my_starwars.infra.database.config import DataBaseConnectionHandler
from my_starwars.infra.database.entities import User as UserModel


class UserRepo(UserRepoInterface):
    """Manipulaçao de dados da tabela User"""

    def __init__(self, connection_string: str) -> None:
        self.__connection_string = connection_string

    def insert_user(self, name: str, email: str, password_hash: str) -> User:
        """
        Realiza a inserçao de um novo usuario na tabela User.
        :param name: Nome do usuario.
        :param email: Email do usuario.
        :param password_hash: Hash da senha do usuario.
        :return: Uma tupla nomeada com todos os dados do usuario cadastrado.
        """

        with DataBaseConnectionHandler(self.__connection_string) as data_base:

            try:
                new_user = UserModel(
                    name=name, email=email, password_hash=password_hash
                )
                data_base.session.add(new_user)
                data_base.session.commit()

                return User(
                    id=new_user.id,
                    name=new_user.name,
                    email=new_user.email,
                    password_hash=new_user.password_hash,
                    character_id=new_user.character_id,
                )
            except:
                data_base.session.rollback()
                raise
            finally:
                data_base.session.close()

    def select_user(
        self,
        name: str = None,
        user_id: int = None,
        email: str = None,
        all_users: bool = False,
    ) -> User:
        """
        Realiza a busca de um usuário cadastrado no banco de dados.
        Os dados podem ser especificados pelo nome ou pelo id do usuario.
        :param name: Nome do usuario.
        :param user_id: ID do usuario.
        :param email: Email do usuario cadastrado.
        :param all_users: Caso seja verdadeiro retorna todos os usuarios cadastrados.
        :return: Uma tupla nomeada com todos os dados do usuario.
        """

        try:
            query_data = None

            if all_users:

                with DataBaseConnectionHandler(self.__connection_string) as data_base:

                    query_data = data_base.session.query(UserModel).all()

            elif name:

                with DataBaseConnectionHandler(self.__connection_string) as data_base:

                    query_data = (
                        data_base.session.query(UserModel).filter_by(name=name).one()
                    )

            elif user_id:

                with DataBaseConnectionHandler(self.__connection_string) as data_base:

                    query_data = (
                        data_base.session.query(UserModel).filter_by(id=user_id).one()
                    )

            elif email:

                with DataBaseConnectionHandler(self.__connection_string) as data_base:

                    query_data = (
                        data_base.session.query(UserModel).filter_by(email=email).one()
                    )

            return query_data

        except NoResultFound:
            return []
        except Exception as error:
            data_base.session.rollback()
            raise error
        finally:
            data_base.session.close()

    def update_user(
        self,
        user_id: int,
        name: str = None,
        email: str = None,
        character_id: int = None,
    ) -> User:
        """
        Realiza a atualização de dados de um usuario cadastrado na tabela User.
        :param user_id: ID do usuario.
        :param name: Nome do usuario.
        :param email: Email do usuario.
        :param character_id: ID do personagem favorito di usuario.
        """

        with DataBaseConnectionHandler(self.__connection_string) as data_base:

            try:
                try:
                    user = (
                        data_base.session.query(UserModel).filter_by(id=user_id).one()
                    )

                    if not user:
                        raise Exception("usuario nao existe")

                    name_exit = (
                        data_base.session.query(UserModel).filter_by(name=name).one()
                    )

                    if name_exit and user.name != name:
                        raise Exception("nome nao disponivel")

                    email_exit = (
                        data_base.session.query(UserModel).filter_by(email=email).one()
                    )

                    if email_exit and user.email != email:
                        raise Exception("email nao disponivel")

                except NoResultFound:
                    pass
                except Exception as error:
                    raise error

                if name:
                    user.name = name

                if email:
                    user.email = email

                if character_id:
                    user.character_id = character_id

                data_base.session.commit()

                return User(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    password_hash=user.character_id,
                    character_id=user.character_id,
                )
            except:
                data_base.session.rollback()
                raise
            finally:
                data_base.session.close()
