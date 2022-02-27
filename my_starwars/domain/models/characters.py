"""Interface ara a tupla nomeada Characters"""
from collections import namedtuple

Character = namedtuple(
    "Character", "id name heigth mass hair_color skin_color eye_color birth_year gender"
)
