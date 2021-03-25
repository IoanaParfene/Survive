import Survive.variable_initialization as var_init
import Survive.status_bars as sb
import time


def initialize_status_bars():
    """ Initialize the status bar objects into a list"""
    # StatusBar object + screen display location
    status_bars = {"Calories": sb.StatusBar("Calories", 3000, 1200),
                   "Condition": sb.StatusBar("Condition", 100, 100),
                   "Body Heat": sb.StatusBar("Body Heat", 100, 100),
                   "Hydration": sb.StatusBar("Hydration", 100, 100)}
    return status_bars


def initialize_game():
    """ Initialize game """
    # Create inventory
    #inventory = Inventory.Inventory(20)
    ##Inventory.get_items_from_json(inventory)
    ##Inventory.add_items_to_json(inventory)

    # Create status bars
    status_bars = initialize_status_bars()
    # Almost identical with the actual game_time
    game_time = time.time()
    # Add initial calorie and hydration decay
    status_bars["Hydration"].add_decay_factor(1, 25, game_time)
    status_bars["Calories"].add_decay_factor(1, 6, game_time)
    status_bars["Body Heat"].add_decay_factor(1, 30, game_time)
    status_bars["Condition"].add_decay_factor(1, 50, game_time)

    return status_bars