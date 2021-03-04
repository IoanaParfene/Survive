from StatusBars import *
from Inventory import *
from Buttons import *


def initialize_buttons(screen):
    buttons = {}
    buttons["Shelter"] = Button('Shelter', (400, 110), (220, 100), screen)
    buttons["Fire"] = Button('Fire', (650, 110), (220, 100), screen)
    buttons["GetWater"] = Button('GetWater', (900, 110), (220, 100),  screen)
    buttons["Crafting"] = Button('Crafting', (650, 290), (220, 100),  screen)
    buttons["Inventory"] = Button('Inventory', (900, 290), (220, 100),  screen)
    buttons["Explore"] = Button('Explore', (400, 450), (220, 100), screen)
    buttons["Traps/Hunt"] = Button('TrapsHunt', (650, 450), (220, 100),  screen)
    buttons["Travel"] = Button('Travel', (900, 450), (220, 100),  screen)
    buttons["Pause"] = Button('ll', (1100, 10), (40, 60), screen)
    return buttons


def initialize_status_bars():
    """ Initialize the status bar objects into a list"""
    status_bars = {}
    # StatusBar object + screen display location
    status_bars["Calories"] = (StatusBar("Calories", 3000, 3000),(20, 370))
    status_bars["Condition"] = (StatusBar("Condition", 100, 100),(20, 420))
    status_bars["Body Heat"] = (StatusBar("Body Heat", 100, 100),(20, 470))
    status_bars["Hydration"] = (StatusBar("Hydration", 100, 100),(20, 520))
    return status_bars


def initialize_game(screen, game_time):
    """ Initialize game """
    # Create inventory
    inventory = Inventory(20)
    get_items_from_json(inventory)
    add_items_to_json(inventory)

    # Create status bars
    status_bars = initialize_status_bars()
    # Add initial calorie and hydration decay
    status_bars["Hydration"][0].add_decay_factor(1, 30, game_time)
    status_bars["Calories"][0].add_decay_factor(1, 3, game_time)

    # Create buttons
    buttons = initialize_buttons(screen)
    return inventory, status_bars, buttons
