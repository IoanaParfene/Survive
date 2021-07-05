from PythonFiles.BackendFunctions import backend_miscellaneous as bbm
from PythonFiles import constants as cs, initialization as init
from PythonFiles.Widgets import widget_customs as wwc
from kivy.properties import StringProperty
from kivy.uix.widget import Widget


class CraftingScreen(wwc.BaseGameplayScreen):
    """ Screen for the crafting menu """

    class Craftable(Widget):
        """ The container of the inventory slots """
        # The background image of the inventory container
        this_source = StringProperty("GraphicFiles/night.png")
    pass

    def scroll_craftables(self, direction):
        """ Go up or down in the current inventory category page"""
        if direction == "left":
            # If the inventory page is 0 stay there
            if cs.craftable_scroll_page > 0:
                cs.craftable_scroll_page -= 1
        else:
            cs.craftable_scroll_page += 1

    def craft(self):
        """ Craft the chosen item and remove used materials """
        item_name = ""
        counter = 0
        for key, value in cs.craftable_items.items():
            if cs.craftable_scroll_page == counter:
                item_name = key
            counter += 1

        # Add the lost second for the loading screen
        init.game_state.paused_time += 1
        # Update the status bars during the special action
        bbm.update_bars_during_action(cs.craftable_items[item_name]["Duration"]/60, [])

        for material_name, material_quantity in cs.craftable_items[item_name]["Needed"]:
            init.game_state.inventory.items[material_name]["Quantity"] -= material_quantity

        init.game_state.inventory.items[item_name]["Quantity"] += 1