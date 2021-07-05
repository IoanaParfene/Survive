from PythonFiles import constants as cs, initialization as init
from PythonFiles.BackendFunctions import backend_time as bbt
from PythonFiles.Screens import screens as sc


########################################################################################
# FUNCTIONS USED DURING GAME LOOP UPDATES
########################################################################################

def game_time_description_text():
    """ Get current player time on label text"""
    # Get remaining hours in time of day
    game_hours_today = bbt.get_current_game_day_hours()
    if game_hours_today < 12:
        day_period = "DAYLIGHT"
    else:
        day_period = "DARKNESS"
    time_information = str(
        int(12 - game_hours_today % 12) + 1) + " HOURS OF " + day_period + " REMAINING"
    return time_information


def get_progress_description_text():
    """ Get current location, day and miles left label text"""

    game_progress = init.game_state.current_location["Name"].upper() + " | DAY " + \
                    str(init.game_state.current_game_day).upper() + " | "

    if init.game_state.inventory.items["area_map"]["Quantity"] > 0:
        game_progress += str(init.game_state.remaining_miles).upper() + " MILES LEFT"
    else:
        game_progress += str(cs.initial_miles - init.game_state.remaining_miles).upper() + " MILES WALKED"
    return game_progress


########################################################################################
# GAME LOOP UPDATING FUNCTIONS
########################################################################################

def update_progress_labels(screen_type):
    """ Update the location, day time and remaining miles labels"""
    # Update time label
    sc.sm.get_screen(screen_type).ids.time_label.text = game_time_description_text()
    # Update location label
    sc.sm.get_screen(screen_type).ids.location_label.text = get_progress_description_text()


def update_background_widget(screen_type):
    """ Change background after the time of day """
    sc.sm.get_screen(screen_type).ids.background.change_background()


def update_rain_widget(screen_type):
    """ Change rain animation position """
    sc.sm.get_screen(screen_type).rain.show_rain()