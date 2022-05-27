from hanged.settings.base import LIMIT, SEPARATED


class GenericAPI:
    def __init__(self, url, path) -> None:
        self.url = url
        self.path = path
        self.limit = LIMIT
        self.words_by_levels = dict()

    def process_list(self, response_list):
        temporal_list = sorted(response_list, key=len)

        self.words_by_levels["Beginner"] = temporal_list[:SEPARATED]
        self.words_by_levels["Intermediate"] = temporal_list[SEPARATED : SEPARATED * 2]
        self.words_by_levels["Expert"] = temporal_list[SEPARATED * 2 : self.limit]

        return self.words_by_levels

    def get_options_by_levels(self):
        pass
