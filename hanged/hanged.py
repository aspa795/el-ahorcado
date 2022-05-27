from hanged.settings.base import MENU
from models.game import Game
from models.user import User


def start_game():
    is_start = True

    while is_start:
        print(MENU)

        option = input("Choose your option: ")

        if option.isdigit() and 0 < int(option) < 3:
            if option == "1":
                name = input("Please, enter your name: ")
                user = User(name=name)
                game = Game(user=user)
                selected_category = game.show_categories()
                selected_level = game.show_levels()

                if selected_category and selected_level:
                    print(
                        "NAME: {} | CATEGORY: {} | LEVEL: {}".format(
                            game.user.name,
                            game.selected_category["name"],
                            game.selected_level["level"],
                        )
                    )
                    game.charge_data_by_category()
                    game.get_word()
                    game.setup_hidden_word()
                    game.assign_attempts()

                    while game.verify_game():
                        print(
                            "Lives: {} | Attempts: {}".format(game.lives, game.attempts)
                        )
                        game.show_hidden_word()
                        letter = input("Enter your letter: ")
                        game.launch_attempt(letter=letter)

                    print("The Word is: {}".format(game.word))

                    if game.get_evaluation():
                        print("You Win!!")
                    else:
                        print("You Lose...")

            elif option == "2":
                is_start = False
                print("*** THANK, COME BACK SOON ***")
        else:
            print("*** WRONG OPTION ***")
