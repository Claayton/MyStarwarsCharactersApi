"""Interface ara a tupla nomeada User"""
from collections import namedtuple

User = namedtuple("User", "id name email password_hash")
