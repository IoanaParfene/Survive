from PythonFiles.BackendFunctions import backend_inventory as bbi
from PythonFiles import constants as cs, initialization as init
import random


########################################################################################
# FUNCTIONS USED DURING GAME LOOP UPDATES
########################################################################################

def start_fire(tool, *args):
    """ Start a fire """

    # Randomize whether the fire will start or not
    fire_starts_weights = [cs.fire_tool_info[tool]["SuccessRate"] * 100, 100 - cs.fire_tool_info[tool]["SuccessRate"] * 100]
    fire_starts = random.choices([True, False], weights=fire_starts_weights, k=1)

    # Randomize whether the fire tool will break or not
    tool_breaks_weights = [cs.fire_tool_info[tool]["DestroyRate"] * 100, 100 - cs.fire_tool_info[tool]["DestroyRate"] * 100]
    tool_breaks = random.choices([True, False], weights=tool_breaks_weights, k=1)

    fire_starting_text = ""
    if fire_starts[0]:
        fire_starting_text = "I started the fire."
        # Add fire duration
        init.game_state.fire_duration = 20
        # Save the fire start time
        init.game_state.start_fire_time = init.game_state.game_time
        # Start the fire
        init.game_state.fire_on = True
    else:
        fire_starting_text = "I couldn't start the fire."

    # Remove the tool if it breaks and display the message
    if tool_breaks[0]:
        init.game_state.inventory.items[tool]["Quantity"] -= 1
        if cs.fire_tool_info[tool]["ShowDestructionMessage"]:
            fire_starting_text += " My " + cs.fire_tool_info[tool]["Name"].lower() + " broke."

    init.game_state.fire_starting_message = fire_starting_text


def add_fuel(fuel_type, *args):
    """ Add fuel to the fire """
    # If the fire is burning
    if init.game_state.fire_on:
        # Make a list of all the extra fire minutes added by each type of fuel
        minute_list = [("tinder", 15), ("wood", 90), ("hardwood", 180)]
        # Add the fuel type
        for fuel in minute_list:
            if fuel_type == fuel[0]:
                # Remove one unit of fuel from the inventory
                init.game_state.inventory.items[fuel_type]["Quantity"] -= 1
                # Add the extra minutes to the fire
                init.game_state.fire_duration += fuel[1]


def boil_water(*args):
    """ Turn the dirty water bottles into clean water bottles """
    init.game_state.inventory.items["water_bottle_safe"]["Quantity"] += \
    init.game_state.inventory.items["water_bottle_unsafe"]["Quantity"]
    init.game_state.inventory.items["water_bottle_unsafe"]["Quantity"] = 0


def smoke_meat(*args):
    """ Turn a piece of meat into smoked jerky """
    init.game_state.inventory.items["raw_meat"]["Quantity"] -= 1
    init.game_state.inventory.items["smoked_jerky"]["Quantity"] += 1
    init.game_state.spoiling_rates["raw_meat"].pop()


def cook_meat(*args):
    """ Cook a piece of raw meat """
    init.game_state.inventory.items["raw_meat"]["Quantity"] -= 1
    init.game_state.inventory.items["cooked_meat"]["Quantity"] += 1
    bbi.add_item_spoil_rate("cooked_meat", 1)
    init.game_state.spoiling_rates["raw_meat"].pop()


########################################################################################
# GAME LOOP UPDATING FUNCTIONS
########################################################################################

def update_fire():
    """ Update fire begin/end/duration """
    # If the fire is burning
    if init.game_state.fire_on:
        # Get how many minutes the fire has been burning for
        fire_burning_minutes = init.game_state.game_time - init.game_state.start_fire_time
        # If the fire has been on for more than the set fire duration
        if init.game_state.fire_duration < fire_burning_minutes:
            # Stop the fire
            init.game_state.fire_on = False
            # Reset fire duration
            init.game_state.fire_duration = 0