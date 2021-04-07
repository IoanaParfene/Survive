import variable_initialization as var_init
import copy


class ItemType:
    def __init__(self, name, categories, quantity, individual_weight, maximum_capacity, throwable, actions):
        self.name = name
        self.categories = categories
        self.quantity = quantity
        self.individual_weight = individual_weight
        self.maximum_capacity = maximum_capacity
        self.throwable = throwable
        self.actions = actions


class Inventory:
    def __init__(self):
        self.max_capacity = copy.copy(var_init.max_inventory_capacity)
        self.current_capacity = copy.copy(var_init.current_inventory_capacity)
        self.items = copy.copy(var_init.inventory_items)

    def get_available_items(self):
        return self.available_items


def initialize_inventory():
    """ Initialize the inventory items """
    # Inventory object
    inventory = Inventory()

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


# Initialize inventory
inventory = initialize_inventory()