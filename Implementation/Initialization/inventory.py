from Initialization import constants as cs
import copy


class Inventory:
    def __init__(self):
        # The maximum spacial capacity of the inventory
        self.max_capacity = copy.copy(cs.max_inventory_capacity)
        # The current space occupied in the inventory
        self.current_capacity = copy.copy(cs.current_inventory_capacity)
        # All the possible items of the inventory
        self.items = copy.copy(cs.inventory_items)


