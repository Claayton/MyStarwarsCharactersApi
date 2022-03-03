"""Arquivo de manipulaçao de variaveis de ambiente"""
import os
from dotenv import load_dotenv

load_dotenv()

VARS = {
    "search_url": os.getenv("SEARCH_URL"),
    "connection_string": os.getenv("CONNECTION_STRING"),
    "connection_string_test": os.getenv("CONNECTION_STRING_TEST"),
    "secret_key": os.getenv("SECRET_KEY"),
}
