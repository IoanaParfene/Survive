from PythonFiles.BackendFunctions import backend_inventory as bbi
from PythonFiles import initialization as init
import random


########################################################################################
# GAME LOOP UPDATING FUNCTIONS
########################################################################################

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
                bbi.add_item_spoil_rate(inventory_hunt_item, 1)
                init.game_state.last_hour_trapped_animals.append(info["Prey"])