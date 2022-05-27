from hanged.services.countries_api import CountriesAPI
from hanged.services.dog_api import DogsAPI
from hanged.services.pokemon_api import PokemonAPI
from hanged.services.rickandmorty_api import RickyAPI
from hanged.settings.base import SEPARATED


def test_countries_api():
    countries_api = CountriesAPI()
    result = countries_api.get_options_by_levels()

    assert len(result["Beginner"]) == SEPARATED
    assert len(result["Intermediate"]) == SEPARATED
    assert len(result["Expert"]) == SEPARATED


def test_dogs_api():
    dogs_api = DogsAPI()
    result = dogs_api.get_options_by_levels()

    assert len(result["Beginner"]) == SEPARATED
    assert len(result["Intermediate"]) == SEPARATED
    assert len(result["Expert"]) == SEPARATED


def test_pokemon_api():
    pokemon_api = PokemonAPI()
    result = pokemon_api.get_options_by_levels()

    assert len(result["Beginner"]) == SEPARATED
    assert len(result["Intermediate"]) == SEPARATED
    assert len(result["Expert"]) == SEPARATED


def test_ricky_api():
    ricky_api = RickyAPI()
    result = ricky_api.get_options_by_levels()

    assert len(result["Beginner"]) == SEPARATED
    assert len(result["Intermediate"]) == SEPARATED
    assert len(result["Expert"]) == SEPARATED
