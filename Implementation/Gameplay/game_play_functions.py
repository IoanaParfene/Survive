from Initialization import initialization as init
from Initialization import constants as cs
import random
import time


def get_game_time():
    """ Calculate in game passed minutes """
    return init.game_state.skipped_time + ((time.time() - init.game_state.start_time - init.game_state.paused_time) / 3) * init.game_state.game_speed


def get_current_game_day_hours():
    """ Calculate how many hours have passed in he current game day"""
    game_hours = init.game_state.game_time / 60
    init.game_state.current_game_day = int(game_hours / 24 + 1)
    game_hours_today = game_hours % 24
    return game_hours_today


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


def activate_game_time():
    """ Activate and update game time if it is paused """
    if init.game_state.time_is_stopped:
        update_paused_time()


def pause_game_time():
    """ Pause game time if it is running """
    if not init.game_state.time_is_stopped:
        init.game_state.time_is_stopped = True
        init.game_state.start_paused_time = time.time()


def gradual_status_bar_fluctuation(status_bar_name):
    """ Apply value change factors of current bar for each of their time intervals """
    status_bars = init.game_state.status_bars
    if status_bars[status_bar_name].fluctuation is not None:
        item = status_bars[status_bar_name].fluctuation
        # Fluctuation supposed to happen based on passed game time
        fluctuation_counter = init.game_state.game_time // item[1]
        if abs(fluctuation_counter - item[2]) > 0:
            if status_bar_name == "Body Heat":
                pass
            if not int(status_bars[status_bar_name].current_value - abs(fluctuation_counter - item[2]) * item[0]) < (-status_bars[status_bar_name].max_value / 10):
                status_bars[status_bar_name].current_value = min(status_bars[status_bar_name].current_value - abs(fluctuation_counter - item[2]) * item[0], status_bars[status_bar_name].max_value)
                #status_bars[status_bar_name].current_value = status_bars[status_bar_name].current_value - abs(fluctuation_counter - item[2]) * item[0]
                if (-status_bars[status_bar_name].max_value / 7) < status_bars[status_bar_name].current_value < (-status_bars[status_bar_name].max_value / 15):
                    if status_bar_name != "Calories":
                        init.game_state.game_over = "Lost"
            # Last fluctuation that happened based on passed game time
            item[2] = fluctuation_counter


def update_status_bars():
    """ Update status bars value each frame """
    for status_bar_name in init.game_state.status_bars.keys():
        gradual_status_bar_fluctuation(status_bar_name)


def immediate_status_bar_decay(status_bar_name, damage):
    """ Take immediate decay based on damage of a certain action"""
    status_bars = init.game_state.status_bars
    status_bars[status_bar_name].current_value -= damage
    if status_bars[status_bar_name].current_value - damage < (-status_bars[status_bar_name].max_value / 20):
        if status_bar_name != "Calories":
            init.game_state.game_over = "Lost"


def immediate_status_bar_increase(status_bar_name, increase):
    """ Immediate increase in value based on certain action """
    status_bars = init.game_state.status_bars
    if min(status_bars[status_bar_name].max_value, status_bars[status_bar_name].current_value + increase) == status_bars[status_bar_name].max_value:
        status_bars[status_bar_name].current_value = status_bars[status_bar_name].max_value
    elif status_bars[status_bar_name].current_value <= 0:
        status_bars[status_bar_name].current_value = int(increase)
    else:
        status_bars[status_bar_name].current_value = int(increase + status_bars[status_bar_name].current_value)


def update_inventory():
    """ Update Inventory capacity and item weights """
    # The current inventory space of the player
    inventory_capacity = cs.base_inventory_capacity
    for item in cs.space_boosters:
        if init.game_state.inventory.items[item[0]]["Quantity"]>0:
            inventory_capacity += item[1] * int(init.game_state.inventory.items[item[0]]["Quantity"])
    init.game_state.inventory.max_capacity = inventory_capacity
    # The items in the inventory
    total_weight = 0
    for key, value in init.game_state.inventory.items.items():
        init.game_state.inventory.items[key]["InventorySpace"] = float(int(init.game_state.inventory.items[key]["Quantity"] * init.game_state.inventory.items[key]["Weight"]))
        total_weight += init.game_state.inventory.items[key]["InventorySpace"]
    init.game_state.inventory.current_capacity = total_weight


def check_game_over_condition():
    """ Check to see if the game is over"""
    if init.game_state.game_time // 60 > 1 or init.game_state.current_game_day > 1:
        # If game is lost or won
        if init.game_state.game_over != "No":
            return True
    return False


def get_fluctuation_code():
    """ Get fluctuation code """
    # Get the heat factor data to obtain the fluctuation code
    fluctuation_code = ""
    # Check the factor booleans
    for name in cs.heat_factor_names:
        # Get the complete boolean variable names
        complete_name = "init.game_state." + name
        # Add an "n" in front of the current factor character if False
        if not eval(complete_name):
            fluctuation_code += "n"
        # Get the current factor character
        fluctuation_code += name.lower()[0]
    return fluctuation_code


def update_heat_fluctuation_factor(fluctuation_code):
    print(fluctuation_code, init.game_state.status_bars["Body Heat"].fluctuation)
    """ Update heat fluctuation factor based on location, day time, fire, weather """
    # Modify the Body Heat fluctuation factor if the environmental factors change
    if fluctuation_code != init.game_state.current_heat_factor_code:
        # Save the current environmental factor code
        init.game_state.current_heat_factor_code = fluctuation_code
        # If the status bar should stay stagnant, delete fluctuation factor
        if cs.heat_factor_fluctuation[fluctuation_code] == 0.0:
            init.game_state.status_bars["Body Heat"].remove_fluctuation_factor()
        else:
            # Time interval between two concurrent fluctuations with the factor value
            value = (cs.heat_factor_fluctuation[fluctuation_code] / 60) * (-1.0)
            # Modify the fluctuation factor
            init.game_state.status_bars["Body Heat"].add_fluctuation_factor(value, 1, init.game_state.game_time)


def update_rain():
    """ Update rain begin/end/duration """
    # If it is raining
    if init.game_state.raining_now:
        # Get how many hours it has been raining for
        rained_game_hours = (init.game_state.game_time - init.game_state.start_rain_related_time)/60
        # If is has been raining for more than the set raining duration
        if init.game_state.rain_related_duration < rained_game_hours:
            # Stop the rain
            init.game_state.raining_now = False
            # Save the time it stopped raining
            init.game_state.start_rain_related_time = init.game_state.game_time
            # Randomize the duration of the up-coming no-rain period
            init.game_state.rain_related_duration = random.randint(8, 72)
    else:
        not_rained_game_hours = (init.game_state.game_time - init.game_state.start_rain_related_time)/60
        # If the no-rain time is over
        if init.game_state.rain_related_duration < not_rained_game_hours:
            # Start the rain
            init.game_state.raining_now = True
            # Save the time it started raining
            init.game_state.start_rain_related_time = init.game_state.game_time
            # Randomize the duration of the up-coming rain period
            init.game_state.rain_related_duration = random.randint(5, 24)


def update_bars_during_action(hours, irrelevant_factors):
    """ Update status bars during fast-forwarding actions like sleep, travel, explore, etc """
    # Update bars each minute during the action
    for index in range(0, int(hours * 60)):
        # Add the passed minute
        init.game_state.skipped_time += 1
        # Update the time
        update_game_time()
        # Update rain
        update_rain()
        # Get the heat factor code
        fluctuation_code = get_fluctuation_code()
        # Update the code with the action specific factors
        if fluctuation_code is not None:
            for factor in irrelevant_factors:
                # If the action cancels any factors, add "n" in front of their character in the code
                if fluctuation_code.count("n" + factor) == 0:
                    fluctuation_code = fluctuation_code.split(factor)[0] + "n" + factor + \
                                       fluctuation_code.split(factor)[1]
        # Update the body heat factor
        update_heat_fluctuation_factor(fluctuation_code)
        # Update the status bars
        update_status_bars()


def start_fire(tool, *args):
    """ Start a fire """
    # Remove tool from inventory
    init.game_state.inventory.items[tool]["Quantity"] -= 1
    # Add fire duration
    init.game_state.fire_duration = 20
    # Save the fire start time
    init.game_state.start_fire_time = init.game_state.game_time
    # Start the fire
    init.game_state.fire_on = True


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


def cook_meat(*args):
    """ Cook a piece of raw meat """
    init.game_state.inventory.items["raw_meat"]["Quantity"] -= 1
    init.game_state.inventory.items["cooked_meat"]["Quantity"] += 1
    add_item_spoil_rate("cooked_meat", 1)


def update_traps():
    """ Make traps catch something each hour with a specific chance """
    # Catch prey
    init.game_state.last_hour_trapped_animals = []
    for trap_type, info in init.game_state.traps.items():
        for counter in range(0, int(info["Quantity"])):
            weights = [info["HourlyTrapChance"] * 100, 100 - info["HourlyTrapChance"] * 100]
            caught_something = random.choices([True, False], weights=weights, k=1)
            if caught_something[0] is True:
                inventory_hunt_item = "dead_" + info["Prey"]
                init.game_state.inventory.items[inventory_hunt_item]["Quantity"] += 1
                add_item_spoil_rate(inventory_hunt_item, 1)
                init.game_state.last_hour_trapped_animals.append(info["Prey"])


def add_item_spoil_rate(item, quantity):
    """ Add the spoil rate of the item if it has one """
    if item in cs.spoil_items.keys():
        for counter in range(0, quantity):
            passed_game_hours = init.game_state.game_time / 60
            hours_until_spoilage = cs.spoil_items[item]["FreshTime"]
            init.game_state.spoiling_rates[item].append((passed_game_hours, hours_until_spoilage))


def remove_item_spoil_rate(item, quantity):
    """ Remove the spoil rate of the item if it has one """
    if item in cs.spoil_items.keys():
        for counter in range(0, quantity):
            init.game_state.spoiling_rates[item].pop()


def update_spoiled_items():
    """ Turn spoiled items into spoiled meat """
    # Game passed hours
    game_passed_hours = init.game_state.game_time // 60
    for key, value in cs.spoil_items.items():
        for rate in init.game_state.spoiling_rates[key]:
            if game_passed_hours - rate[0] > rate[1]:
                init.game_state.inventory.items[key]["Quantity"] -= 1
                for item in cs.spoil_items[key]["SpoilItems"]:
                    init.game_state.inventory.items[item]["Quantity"] += 1
                init.game_state.spoiling_rates[key].pop()


