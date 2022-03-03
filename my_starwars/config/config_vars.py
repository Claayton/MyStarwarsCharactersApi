"""Arquivo de manipulaçao de variaveis de ambiente"""
import os
from dotenv import load_dotenv

load_dotenv()

VARS = {
    "search_url": os.getenv("SEARCH_URL"),
    "connection_string": os.getenv("CONNECTION_STRING"),
    "secret_key": os.getenv("SECRET_KEY"),
}
