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

    users = relationship("User")

    def __repr__(self) -> str:
        return f"StarwarsCharacter: {self.name}"

    def __eq__(self, other):

        if (
            self.id == other.id
            and self.name == other.name
            and self.heigth == other.heigth
            and self.mass == other.mass
            and self.hair_color == other.hair_color
            and self.skin_color == other.skin_color
            and self.eye_color == other.eye_color
            and self.birth_year == other.eye_color
            and self.gender == other.gender
        ):
            return True
        return False
