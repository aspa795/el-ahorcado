import random as rd

from hanged.services.countries_api import CountriesAPI
from hanged.services.dog_api import DogsAPI
from hanged.services.pokemon_api import PokemonAPI
from hanged.services.rickandmorty_api import RickyAPI
from hanged.settings.base import CATEGORIES, LEVELS


class Game:
    API_SERVICES = {
        "countries": CountriesAPI(),
        "dogs": DogsAPI(),
        "pokemon": PokemonAPI(),
        "ricky": RickyAPI(),
    }

    def __init__(self, user=None) -> None:
        self.user = user
        self.attempts = 0
        self.lives = 0
        self.options = None
        self.selected_category = None
        self.selected_level = None
        self.word = None
        self.hidden_word = None
        self.categories = CATEGORIES
        self.levels = LEVELS
        self.win = False
        self.lose = False

    def subtract_attempt(self):
        self.attempts -= 1

    def get_word_len(self):
        return len(self.word)

    def assign_attempts(self):
        number_of_letters_to_display = int(self.get_word_len() * 0.30)
        self.attempts = self.get_word_len() - number_of_letters_to_display
        self.lives = self.attempts

    def show_hidden_word(self):
        print(" ".join(list(self.hidden_word)).capitalize())

    def setup_hidden_word(self):
        number_of_letters_to_display = int(self.get_word_len() * 0.30)
        index_list_to_display = rd.sample(
            range(self.get_word_len()), number_of_letters_to_display
        )
        hidden_word_list = []
        for i, letter in enumerate(self.word):
            if i not in index_list_to_display:
                hidden_word_list.append("_")
            else:
                hidden_word_list.append("{}".format(letter))

        self.hidden_word = "".join(hidden_word_list)
        return self.hidden_word.capitalize()

    def launch_attempt(self, letter):
        if letter.lower() in self.word.lower():
            for i, letter_word in enumerate(self.word.lower()):
                if letter in letter_word:
                    temporal_list = list(self.hidden_word)
                    temporal_list[i] = letter
                    self.hidden_word = "".join(temporal_list).capitalize()
        else:
            self.subtract_attempt()

    def verify_game(self):
        return self.attempts > 0 and self.word.lower() != self.hidden_word.lower()

    def get_evaluation(self):
        if "_" not in self.hidden_word:
            return True
        else:
            return False

    def get_word(self):
        print("Please wait, choosing random word...")
        self.word = rd.choice(self.options)
        return self.word

    def charge_data_by_category(self):
        print("Please wait, data loading...")
        service = self.API_SERVICES[self.selected_category["slug"]]
        self.options = service.get_options_by_levels()[self.selected_level["level"]]

    def select_level(self, tag):
        self.selected_level = next(
            level for level in self.levels if level["tag"] == tag
        )
        return self.selected_level

    def show_levels(self):
        is_correct = True

        while is_correct:
            print("--- SELECT YOUR LEVEL ---")
            for i, level in enumerate(self.levels):
                print("{}.- {}".format(i + 1, level["level"]))
            print("{}.- {}".format(len(self.levels) + 1, "Exit"))

            option = input("Choose your option: ")

            if option.isdigit() and 0 < int(option) <= len(self.levels) + 1:
                if int(option) != len(self.levels) + 1:
                    return self.select_level(self.levels[int(option) - 1]["tag"])

                return None
            else:
                print("*** WRONG OPTION ***")

    def select_category(self, slug):
        self.selected_category = next(
            category for category in self.categories if category["slug"] == slug
        )
        return self.selected_category

    def show_categories(self):
        is_correct = True

        while is_correct:
            print("--- SELECT YOUR FAVORITE CATEGORY ---")
            for i, category in enumerate(self.categories):
                print("{}.- {}".format(i + 1, category["name"]))
            print("{}.- {}".format(len(self.categories) + 1, "Exit"))

            option = input("Choose your option: ")

            if option.isdigit() and 0 < int(option) <= len(self.categories) + 1:
                if int(option) != len(self.categories) + 1:
                    return self.select_category(
                        self.categories[int(option) - 1].get("slug")
                    )

                return None
            else:
                print("*** WRONG OPTION ***")
