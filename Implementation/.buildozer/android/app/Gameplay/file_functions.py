import os


def get_path(file):
    """ Get absolute path to a game file """
    this_folder = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(this_folder, file)
    return my_file


def delete_save_file():
    """ Delete save file """
    if os.path.isfile(get_path('save_game.pkl')):
        os.remove(get_path("save_game.pkl"))


def save_file_exists():
    """ Check if there is a previously saved file """
    if not os.path.isfile(get_path('save_game.pkl')):
        return False
    return True