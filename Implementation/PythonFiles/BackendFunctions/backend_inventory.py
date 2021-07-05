from PythonFiles import constants as cs, initialization as init


########################################################################################
# FUNCTIONS USED DURING GAME LOOP UPDATES
########################################################################################

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


########################################################################################
# GAME LOOP UPDATING FUNCTIONS
########################################################################################

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