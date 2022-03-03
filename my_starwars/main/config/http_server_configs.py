"""Arquivo de instancia do app"""
from fastapi import FastAPI
from docs.tags import tags_metadata
from my_starwars.main.routes import characters, users, auth, user


def create_app() -> FastAPI:
    """Funcao de criaçao do app"""

    app = FastAPI(
        title="MyStarwarsCharacterApi",
        version="0.0.1",
        description="""
        Api de request que consome uma dados de uma API externa.

        Realiza registro e autenticaçao de usuarios com token.

        Permite que o usuário escolha seus personagens preferidos de starwars.
        """,
        openapi_tags=tags_metadata,
    )

    app.include_router(characters)
    app.include_router(users)
    app.include_router(user)
    app.include_router(auth)

    return app
