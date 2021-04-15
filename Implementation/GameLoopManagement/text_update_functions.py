from Initialization import initialization as init
from Initialization import constants as cs


def game_time_description_update():
    """ Get current player time on label text"""
    # Get remaining hours in time of day
    game_hours = init.game_state.game_time / 60
    init.game_state.current_game_day = int(game_hours / 24 + 1)
    game_hours_today = game_hours % 24
    if game_hours_today < 12:
        init.game_state.current_day_period = "DAYLIGHT"
    else:
        init.game_state.current_day_period = "DARKNESS"
    time_information = str(
        int(12 - game_hours_today % 12) + 1) + " HOURS OF " + init.game_state.current_day_period + " REMAINING"
    return time_information


def get_progress_description_update():
    """ Get current location, day and miles left label text"""
    game_progress = init.game_state.current_location["Name"].upper() + " | DAY " + \
                    str(init.game_state.current_game_day).upper() + " | " + \
                    str(init.game_state.remaining_miles).upper() + " MILES LEFT"
    return game_progress


def status_bar_value_update(status_bar):
    """ Get the current selected status bar value """
    # Return the minimum, maximum or current value if in-between extremities
    new_status_bar_value = max(0, min(init.game_state.status_bars[status_bar].max_value,
                                      init.game_state.status_bars[status_bar].current_value))
    return new_status_bar_value


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
    # If it is dark outside, hide the next location info
    if init.game_state.current_day_period == "DARKNESS":
        text = "???"
    return text


def get_inventory_display_items():
    """ Return the first 5 item names to display for the current inventory page """
    display_dictionary = dict()
    for key, value in init.game_state.inventory.items.items():
        if cs.inventory_display_category in init.game_state.inventory.items[key]["Categories"]:
            if init.game_state.inventory.items[key]["Quantity"] > 0:
                display_dictionary[key] = init.game_state.inventory.items[key]
    # Sort item objects alphabetically
    display_dictionary = dict(sorted(display_dictionary.items(), key=lambda x: x[0].lower()))
    # Get the item names in a list
    display_list = []
    for key, value in display_dictionary.items():
        display_list.append((key, display_dictionary[key]))
    return display_list


def fire_label_description_update(resource):
    """ Return text with specific fire resource quantity """
    text = resource + ": " + str(int(init.game_state.inventory.items[resource]["Quantity"]))
    return text