from Initialization import constants as cs
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
        self.max_capacity = copy.copy(cs.max_inventory_capacity)
        self.current_capacity = copy.copy(cs.current_inventory_capacity)
        self.items = copy.copy(cs.inventory_items)

    def get_available_items(self):
        return self.available_items


