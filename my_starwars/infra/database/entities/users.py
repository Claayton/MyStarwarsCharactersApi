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

    starwars_character_id = Column(Integer, ForeignKey("starwars_characters.id"))
    starwars_character = relationship("StarwarsCharacter", back_populates="users")

    def __init__(self, name: str, email: str, password_hash: str) -> None:
        self.name = name
        self.email = email
        self.password_hash = password_hash

    def __repr__(self) -> str:
        return f"User: {self.name}"
