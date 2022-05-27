from hanged.settings.base import URL_API_COUNTRIES
from hanged.utils import get_response
from models.generic_api import GenericAPI


class CountriesAPI(GenericAPI):
    def __init__(self) -> None:
        GenericAPI.__init__(self, url=URL_API_COUNTRIES, path="all/")

    def get_options_by_levels(self):
        response = get_response(self.url, self.path)

        if response.status_code == 200:
            response_list = [
                country["name"]["common"] for country in response.json()[: self.limit]
            ]

        return self.process_list(response_list)
