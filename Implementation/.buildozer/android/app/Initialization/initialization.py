from Initialization import environment as env
from Initialization import status_bars as sb
from Initialization import inventory as inv
from Initialization import game_state as gs
from Initialization import constants as cs
import random
import time


def initialize_status_bars():
    """ Initialize the status bar objects into a list"""
    # StatusBar object + screen display location
    new_status_bars = {"Calories": sb.StatusBar("Calories", 3000, 1200),
                       "Condition": sb.StatusBar("Condition", 100, 100),
                       "Body Heat": sb.StatusBar("Body Heat", 100, 100),
                       "Hydration": sb.StatusBar("Hydration", 100, 100)}
    # Almost identical with the actual game_time
    game_time = time.time()
    # Add initial calorie and hydration decay
    new_status_bars["Hydration"].add_decay_factor(1, 25, game_time)
    new_status_bars["Calories"].add_decay_factor(1, 6, game_time)
    new_status_bars["Body Heat"].add_decay_factor(1, 30, game_time)
    new_status_bars["Condition"].add_decay_factor(1, 50, game_time)
    return new_status_bars


def initialize_inventory():
    """ Initialize the inventory items """
    # Inventory object
    inventory = inv.Inventory()

    # Add gameplay info
    for key, value in inventory.items.items():
        inventory.items[key]["InventorySpace"] = 0.0
        inventory.items[key]["Quantity"] = 0.0

    # Give starting items
    inventory.items["energy_bar"]["Quantity"] = 3.0
    inventory.items["smoked_jerky"]["Quantity"] = 1.0
    inventory.items["can_of_peas"]["Quantity"] = 1.0
    # Food and Water
    inventory.items["bottle_of_soda"]["Quantity"] = 1.0
    inventory.items["squirrel_juice"]["Quantity"] = 1.0
    # Water
    inventory.items["water_bottle_safe"]["Quantity"] = 1.0
    inventory.items["empty_bottle"]["Quantity"] = 1.0
    # Environmental Aids
    inventory.items["area_map"]["Quantity"] = 1.0 # Tell remaining Miles
    inventory.items["basic_clothes"]["Quantity"] = 1.0 # Keep Warm
    inventory.items["trash_bag"]["Quantity"] = 1.0 # Collect Water
    inventory.items["dry_sack"]["Quantity"] = 1.0 # Inventory
    inventory.items["utility_belt_bag"]["Quantity"] = 1.0  # Inventory 6
    inventory.items["knife"]["Quantity"] = 1.0 # Everything
    inventory.items["empty_can"]["Quantity"] = 1.0 # Cooking
    inventory.items["broken_cellphone"]["Quantity"] = 1.0 # Waste Space
    # Gear
    inventory.items["bait"]["Quantity"] = 4.0
    inventory.items["rope"]["Quantity"] = 2.0
    inventory.items["fishing_kit"]["Quantity"] = 1.0
    inventory.items["newspaper"]["Quantity"] = 1.0
    inventory.items["duct_tape"]["Quantity"] = 1.0
    inventory.items["piece_of_cloth"]["Quantity"] = 1.0
    # Fire
    inventory.items["matches"]["Quantity"] = 6.0

    return inventory


def initialize_game_state():
    """ Initialize the game_state items """

    # Initialize status_bars
    status_bars = initialize_status_bars()

    # Initialize inventory
    inventory = initialize_inventory()

    # Initialize first
    first_location = env.randomize_location_info("pike_lake")

    # Initialize next_locations
    first_travel_locations = [env.randomize_location_info(random.choice(list(cs.game_locations.keys())[1:])),
                              env.randomize_location_info(random.choice(list(cs.game_locations.keys())[1:]))]

    # Game_state object
    game_state = gs.GameState(status_bars, inventory, first_location, first_travel_locations)

    return game_state


game_state = initialize_game_state()