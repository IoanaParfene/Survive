from PythonFiles import constants as cs, initialization as init
from PythonFiles.Screens import screens as sc


########################################################################################
# FUNCTIONS USED DURING GAME LOOP UPDATES
########################################################################################

def get_next_travel_location_text(location_index):
    """ Get text for a next travelling location option"""
    # Get the location name and the minimum miles to reach it
    name, miles = init.game_state.travel_next[location_index]["Name"], init.game_state.travel_next[location_index]["Miles"]
    # Get the minimum hours needed to travel to that location
    hours = cs.game_location_info[init.game_state.travel_next[location_index]["Key"]]["Duration"]
    # If the calories are below 400, add 2 hours to the travel time
    if init.game_state.status_bars["Calories"].current_value < 400:
        text = name.upper() + " | " + str(miles) + " MILES | " + str(hours + 2) + "-" + str(
            hours + 2 + 1) + " HOURS"
    else:
        text = name.upper() + " | " + str(miles) + " MILES | " + str(hours) + "-" + str(hours + 1) + " HOURS"
    # If it is dark outside adn there is no flashlight, hide the next location info
    if not init.game_state.daylight_now:
        if not init.game_state.inventory.items["flashlight"]["Quantity"] > 0:
            text = "???"
    return text


########################################################################################
# GAME LOOP UPDATING FUNCTIONS
########################################################################################

def update_next_travel_locations():
    """ Update next travel location buttons """
    sc.sm.get_screen("travel").ids.travel_1.text = get_next_travel_location_text(0)
    sc.sm.get_screen("travel").ids.travel_2.text = get_next_travel_location_text(1)
