import game_state as gs


def get_path(file):
    """ Get absolute path to a game file """
    import os
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, file)
    return my_file


def game_time_description():
    """ Display player time on screen """
    # Get remaining hours in time of day
    game_hours = gs.game_state.game_time / 60
    gs.game_state.current_game_day = int(game_hours / 24 + 1)
    game_hours_today = game_hours % 24
    if game_hours_today < 12:
        gs.game_state.current_day_period = "DAYLIGHT"
    else:
        gs.game_state.current_day_period = "DARKNESS"
    time_information = str(int(12-game_hours_today % 12) + 1) + " HOURS OF " + gs.game_state.current_day_period + " REMAINING"
    return time_information


def get_progress_description():
    """ Display location, day and miles left """
    game_progress = gs.game_state.game_location_info[gs.game_state.current_location]["Name"].upper() + " | DAY " + \
                    str(gs.game_state.current_game_day).upper() + " | " + \
                    str(gs.game_state.remaining_miles).upper() + " MILES LEFT"
    return game_progress


