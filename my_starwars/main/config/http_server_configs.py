"""Arquivo de instancia do app"""
from fastapi import FastAPI
from my_starwars.main.routes import colector, users, auth


def create_app() -> FastAPI:
    """Funcao de criaçao do app"""

    app = FastAPI(
        title="MyStarwarsCharacterApi",
        version="0.0.1",
        description="Api que consome outra api externa do starwars,\
            realiza login de usuários\
            e permite que o usuário escolha seus personagens preferidos de starwars"
        # Possivelmente implementar tags
    )

    app.include_router(colector)
    app.include_router(users)
    app.include_router(auth)

    return app
