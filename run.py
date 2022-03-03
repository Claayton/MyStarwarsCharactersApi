"""Script para rodar o programa"""
import uvicorn
from my_starwars.infra.database.config.create_databases import create_database
from my_starwars.config import CONNECTION_STRING, CONNECTION_STRING_TEST

if __name__ == "__main__":

    create_database(CONNECTION_STRING)
    create_database(CONNECTION_STRING_TEST)

    uvicorn.run(
        app="my_starwars.main.config.http_server_configs:create_app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        debug=True,
        factory=True,
    )
