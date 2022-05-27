from hanged.settings.base import URL_API_DOGS
from hanged.utils import get_response
from models.generic_api import GenericAPI


class DogsAPI(GenericAPI):
    def __init__(self) -> None:
        GenericAPI.__init__(self, url=URL_API_DOGS, path="breeds/list/all/")

    def get_options_by_levels(self):
        response = get_response(self.url, self.path)

        if response.status_code == 200:
            response_list = list(response.json().get("message").keys())[: self.limit]
            response_list = [breed for breed in response_list]

        return self.process_list(response_list)
