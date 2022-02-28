"""Instancia da tabela User e seus metodos"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from my_starwars.infra.database.config import Base


class User(Base):
    """Tabela de usuarios"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password_hash = Column(String(256), nullable=False)

    character_id = Column(Integer, ForeignKey("characters.id"))

    def __repr__(self) -> str:
        return f"User: {self.name}"

    def __eq__(self, other):

        if (
            self.id == other.id
            and self.name == other.name
            and self.email == other.email
            and self.password_hash == other.password_hash
        ):
            return True
        return False
