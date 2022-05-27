import os

LIMIT = 30
SEPARATED = int(LIMIT / 3)

MENU = """
WELCOME TO THE HANGMAN'S GAME
1.- PLAY
2.- EXIT

"""

CATEGORIES = [
    {
        "name": "Dogs | Breeds",
        "slug": "dogs",
    },
    {
        "name": "Rick and Morty | Characters",
        "slug": "ricky",
    },
    {
        "name": "Pokemon | Name's",
        "slug": "pokemon",
    },
    {
        "name": "Countries | Name's",
        "slug": "countries",
    },
]


URL_API_DOGS = os.getenv("URL_API_DOGS", "https://dog.ceo/api/")
URL_API_RICKY = os.getenv("URL_API_RICKY", "https://rickandmortyapi.com/api/")
URL_API_POKEMON = os.getenv("URL_API_POKEMON", "https://pokeapi.co/api/v2/")
URL_API_COUNTRIES = os.getenv("URL_API_POKEMON", "https://restcountries.com/v3.1/")


LEVELS = [
    {"id": 1, "tag": "BGN", "level": "Beginner"},
    {"id": 2, "tag": "INT", "level": "Intermediate"},
    {"id": 3, "tag": "EXP", "level": "Expert"},
]
