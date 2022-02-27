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
