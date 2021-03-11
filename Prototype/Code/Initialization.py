import Prototype.Code.StatusBars as StatusBars
import Prototype.Code.Inventory as Inventory
import Prototype.Code.Buttons as Buttons
import Prototype.Code.Actions as Actions
import Prototype.Code.Config as Config


def initialize_buttons():
    buttons = {"Shelter": Buttons.Button('Shelter', 'Shelter', (400, 110), (220, 100)),
               "Fire": Buttons.Button('Fire', 'Fire', (650, 110), (220, 100)),
               "Crafting": Buttons.Button('Crafting', 'Crafting', (650, 290), (220, 100)),
               "Inventory": Buttons.Button('Inventory', 'Inventory', (900, 290), (220, 100)),
               "Traps/Hunt": Buttons.Button('TrapsHunt', 'Traps/Hunt', (650, 450), (220, 100)),
               "Travel": Buttons.Button('Travel', 'Travel', (900, 450), (220, 100)),
               "Pause": Buttons.Button('Pause', 'll', (1100, 10), (40, 60)),
               "Main": Buttons.Button('Back', 'Back', (1020, 520), (110, 60))}
    return buttons


def initialize_actions():
    actions = {"GetWater": Actions.Action('GetWater', 'Get Water', (900, 110), (220, 100)),
               "Explore": Actions.Action('Explore', 'Explore', (400, 450), (220, 100)),
               "Sleep1": Actions.Action('Sleep1', 'Sleep 1h', (400, 150), (220, 100)),
               "Sleep4": Actions.Action('Sleep4', 'Sleep 4h', (650, 150), (220, 100)),
               "Travel1": Actions.Action('Travel1', 'Travel1', (400, 120), (700, 180)),
               "Travel2": Actions.Action('Travel2', 'Travel2', (400, 320), (700, 180)),
               "Item0": Actions.Action('Item0', 'Item0', (1050, 370), (100, 40)),
               "Item1": Actions.Action('Item1', 'Item1', (1050, 435), (70, 40)),
               "MakeFire": Actions.Action('MakeFire', 'Make Fire (1 wood)', (400, 150), (350, 100))
               }
    return actions


def initialize_status_bars():
    """ Initialize the status bar objects into a list"""
    # StatusBar object + screen display location
    status_bars = {"Calories": (StatusBars.StatusBar("Calories", 3000, 1200), (20, 370)),
                   "Condition": (StatusBars.StatusBar("Condition", 100, 100), (20, 420)),
                   "Body Heat": (StatusBars.StatusBar("Body Heat", 100, 100), (20, 470)),
                   "Hydration": (StatusBars.StatusBar("Hydration", 100, 100), (20, 520))}
    return status_bars


def initialize_game():
    """ Initialize game """
    # Create inventory
    inventory = Inventory.Inventory(20)
    ##Inventory.get_items_from_json(inventory)
    ##Inventory.add_items_to_json(inventory)

    # Create status bars
    status_bars = initialize_status_bars()
    # Add initial calorie and hydration decay
    status_bars["Hydration"][0].add_decay_factor(1, 25, Config.game_time)
    status_bars["Calories"][0].add_decay_factor(1, 6, Config.game_time)
    status_bars["Body Heat"][0].add_decay_factor(1, 30, Config.game_time)
    status_bars["Condition"][0].add_decay_factor(1, 50, Config.game_time)

    # Create buttons
    buttons = initialize_buttons()

    # Create actions
    actions = initialize_actions()

    # Create inventory actions


    return inventory, status_bars, buttons, actions
