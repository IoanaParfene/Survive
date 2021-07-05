from PythonFiles import initialization as init
import time


########################################################################################
# FUNCTIONS USED DURING GAME LOOP UPDATES
########################################################################################

def get_game_time():
    """ Calculate in game passed minutes """
    return ((time.time() - init.game_state.start_time - init.game_state.paused_time) / 3) * init.game_state.game_speed \
            + init.game_state.skipped_time


def get_current_game_day_hours():
    """ Calculate how many hours have passed in he current game day"""
    game_hours = init.game_state.game_time / 60
    init.game_state.current_game_day = int(game_hours / 24 + 1)
    game_hours_today = game_hours % 24
    return game_hours_today


########################################################################################
# GAME LOOP UPDATING FUNCTIONS
########################################################################################

def activate_game_time():
    """ Activate and update game time if it is paused """
    if init.game_state.time_is_stopped:
        update_paused_time()


def pause_game_time():
    """ Pause game time if it is running """
    if not init.game_state.time_is_stopped:
        init.game_state.time_is_stopped = True
        init.game_state.start_paused_time = time.time()


def update_game_time():
    """ Update game time once per frame in gameplay screens """
    # Update passed in-game time
    init.game_state.game_time = get_game_time()
    # Get remaining hours in time of day
    game_hours_today = get_current_game_day_hours()
    # Update game day period
    if game_hours_today < 12:
        init.game_state.daylight_now = True
    else:
        init.game_state.daylight_now = False


def update_paused_time():
    """ Add time spent in the pause menu to the paused_time variable """
    last_paused_time = time.time() - init.game_state.start_paused_time
    init.game_state.start_paused_time = 0
    init.game_state.time_is_stopped = False
    init.game_state.paused_time += last_paused_time

