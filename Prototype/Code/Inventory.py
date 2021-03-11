import Prototype.Code.Config as Config
import Prototype.Code.Config as buttons

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
    def __init__(self, max_capacity):
        self.available_items = {}
        self.unavailable_items = {}
        self.max_capacity = max_capacity
        self.items = Config.inventory_items

    def get_available_items(self):
        return self.available_items


"""def get_items_from_json(inventory):
    with open(get_path("DataFiles/copy.json"), "r", encoding="utf-8") as jsonObject:
        inventory_json = json.load(jsonObject)
        for key, value in inventory_json.items():
            inventory.get_available_items()[key] = ItemType(key, *value)"""


"""def add_items_to_json(inventory):
    inventoryJSON = jsonpickle.encode(inventory, unpicklable=False)
    with open(get_path("DataFiles/items.json"), "w+", encoding="utf-8") as jsonObject:
        json.dump(inventoryJSON, jsonObject, sort_keys=True, ensure_ascii=False)"""
