"""Instancia da tabela StarwarsCharacter e seus metodos"""
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from my_starwars.infra.database.config import Base


class StarwarsCharacter(Base):
    """Tabela de personagens de starwars"""

    __tablename__ = "starwars_characters"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    heigth = Column(Float)
    mass = Column(Float)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(String)
    gender = Column(String)

    users = relationship("User", back_populates="starwars_characters")

    def __init__(
        self,
        name: str,
        height: float,
        mass: float,
        hair_color: str,
        skin_color: str,
        eye_color: str,
        birth_year: str,
        gender: str,
    ) -> None:
        self.name = name
        self.heigth = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.birth_year = birth_year
        self.gender = gender

    def __repr__(self) -> str:
        return f"StarwarsCharacter: {self.name}"
