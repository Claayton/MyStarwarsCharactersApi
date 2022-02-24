"""Testes para a classe StarWarsCharactersConsumer"""
from my_starwars import config
from my_starwars.errors import HttpRequestError
from . import StarWarsCharactersConsumer


def test_get_characters(requests_mock):
    """Testando o método get_characters"""

    url = config.SEARCH_URL

    requests_mock.get(
        url=url, status_code=200, json={"next": "foo", "results": [{"foo": "bar"}]}
    )

    starwars_characters_consumer = StarWarsCharactersConsumer(url=url)
    params = {"page": 1}
    get_characters_response = starwars_characters_consumer.get_characters(
        page=params["page"]
    )

    # Testando os requests:
    assert get_characters_response.request.method == "GET"
    assert get_characters_response.request.url == url
    assert get_characters_response.request.params == {"page": params["page"]}

    # Testando os responses:
    assert get_characters_response.status_code == 200
    assert isinstance(get_characters_response.response["results"], list)


def test_get_characters_error(requests_mock):
    """
    Testando o erro no metodo get_characters.
    Utilizando um valor invalido para o parametro 'page'.
    """

    url = config.SEARCH_URL

    requests_mock.get(url=url, status_code=404, json={"detail": "Not found"})

    starwars_characters_consumer = StarWarsCharactersConsumer(url=url)
    params = {"page": 777}

    try:

        starwars_characters_consumer.get_characters(page=params["page"])
        assert True is False

    except HttpRequestError as error:

        assert error.message is not None
        assert (error.status_code < 200) or (error.status_code > 299)
