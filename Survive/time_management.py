
def display_game_time(game_state):
    """ Display player time on screen """
    # Get remaining hours in time of day
    game_hours = game_state.game_time / 60
    game_state.current_game_day = int(game_hours / 24 + 1)
    game_hours_today = game_hours % 24
    if game_hours_today < 12:
        game_state.current_day_period = "DAYLIGHT"
    else:
        game_state.current_day_period = "DARKNESS"
    time_information = str(int(12-game_hours_today % 12) + 1) + " HOURS OF " + game_state.current_day_period + " REMAINING"
    return time_information


def display_game_progress(game_state):
    """ Display location, day and miles left """
    # Get day
    game_progress = game_state.game_location_info[game_state.current_location]["Name"].upper() + " | DAY " + \
                    str(game_state.current_game_day).upper() + " | " + \
                    str(game_state.remaining_miles).upper() + " MILES LEFT"
    return game_progress


def update_status_bars(game_state):
    for status_bar in game_state.status_bars.values():
        status_bar.gradual_decay(game_state)
