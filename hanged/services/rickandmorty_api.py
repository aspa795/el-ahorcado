from hanged.settings.base import URL_API_RICKY
from hanged.utils import get_response
from models.generic_api import GenericAPI


class RickyAPI(GenericAPI):
    def __init__(self) -> None:
        GenericAPI.__init__(self, url=URL_API_RICKY, path="character/{}")

    def get_options_by_levels(self):
        response_list = []
        for i in range(2):
            response = get_response(self.url, self.path.format("?page=") + str(i + 1))

            if response.status_code == 200:
                result = [
                    character["name"] for character in response.json().get("results")
                ]
                response_list += result

        return self.process_list(response_list)
