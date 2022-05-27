from hanged.settings.base import URL_API_POKEMON
from hanged.utils import get_response
from models.generic_api import GenericAPI


class PokemonAPI(GenericAPI):
    def __init__(self) -> None:
        GenericAPI.__init__(self, url=URL_API_POKEMON, path="pokemon/?limit={}")

    def get_options_by_levels(self):
        response = get_response(self.url, self.path.format(self.limit))

        if response.status_code == 200:
            response_list = response.json().get("results")[: self.limit]
            response_list = [pokemon["name"] for pokemon in response_list]

        return self.process_list(response_list)
