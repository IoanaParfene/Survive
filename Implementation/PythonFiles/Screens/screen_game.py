from PythonFiles.BackendFunctions import backend_miscellaneous as bbm
from PythonFiles import constants as cs, initialization as init
from PythonFiles.BackendFunctions import backend_stats as bbs
from PythonFiles.Widgets import widget_customs as wwc
from kivymd.app import MDApp
import random


class GameWindow(wwc.BaseGameplayScreen):
    """ Screen for the gameplay menu """

    def __init__(self,**kwargs):
        super(GameWindow, self).__init__(**kwargs)

    def on_enter(self):
        """ Called when entering the screen """
        # Don't allow getting wood at Pike Lake
        if init.game_state.current_location["Name"] == "Pike Lake":
            MDApp.get_running_app().root.get_screen("game").ids.wood_button.disabled = True
        else:
            MDApp.get_running_app().root.get_screen("game").ids.wood_button.disabled = False
        pass

    def change_window(self, new_current_window, *args):
        """ Change game screen based on a button press """
        # If entering the inventor from the game menu, display the first page of the first item category
        if new_current_window == "inventory":
            cs.inventory_display_category = "A"
            cs.inventory_display_page = 0
        # Change the screen
        MDApp.get_running_app().root.current = new_current_window

    def explore(self):
        """ Explore action implementation"""

        # Flag for passing one game hour, if there are items left
        pass_one_hour = False

        # Check if there is enough visibility for the foraging actions
        too_dark, has_flashlight, night_text = self.check_night_action()

        # If there are items left to find
        if not init.game_state.current_location["Explorables"]:
            text = "There is nothing left to explore.."
        # Randomize finding something at all if it is dark
        else:
            # Spend one hour trying to forage
            pass_one_hour = True
            text = night_text

            if has_flashlight or not too_dark:
                # Randomize a number of items to find during the current exploration
                found_items = random.choices([1, 2], weights=(70, 30), k=1)[0]
                text += "I explored for one hour.\nFOUND: "
                # Choose the item/items from the current location's available item list
                for index in range(0, found_items):
                    # If there are remaining items to find, randomly choose one
                    if init.game_state.current_location["Explorables"]:
                        # Pass one game hour for at least this item
                        pass_one_hour = True
                        # Choose one remaining item as a list index
                        item_position = random.randrange(len(init.game_state.current_location["Explorables"]))
                        # Get the code of the item
                        item_code = init.game_state.current_location["Explorables"][item_position]
                        # Remove the item from the list
                        init.game_state.current_location["Explorables"].pop(item_position)
                        # Update the item quantity in the inventory
                        init.game_state.inventory.items[item_code]["Quantity"] += 1
                        # Update the action result text
                        text += cs.inventory_items[item_code]["Name"] + ", "
                text = text[:-1]

        # Pass one game hour if there were items left and change the action result text
        if pass_one_hour:
            # Add the lost second for the loading screen
            init.game_state.paused_time += 1
            # Update the status bars during the special action
            bbm.update_bars_during_action(1, ["f", "s"])
        # Clean the text
        text = text[:-1]
        # Display the text in a popup
        self.show_popup(text)

    def get_wood(self):
        """ Get wood action implementation """

        # Check if there is enough visibility for the foraging actions
        too_dark, has_flashlight, text = self.check_night_action()

        if has_flashlight or not too_dark:
            # Randomize a number of wood logs to find during the current exploration
            found_wood_logs = random.choices([2, 3], weights=(70, 30), k=1)[0]
            # Boolean to see if there will be a hardwood log found as well
            found_hardwood_logs = random.choices([True, False], weights=(10, 90), k=1)[0]

            # Prepare action result text
            text += "\nI searched for one hour.\nFOUND: Wood(" + str(found_wood_logs) + "),"
            # Add the hardwood to the text
            if found_hardwood_logs:
                text += " Hardwood(1),"
            # Clean the text
            text = text[:-1]

            # Add the wood to the inventory
            init.game_state.inventory.items["wood"]["Quantity"] += found_wood_logs
            # Add the hardwood to the inventory
            if found_hardwood_logs:
                init.game_state.inventory.items["hardwood"]["Quantity"] += 1

        # Add the lost second for the loading screen
        init.game_state.paused_time += 1
        # Update the status bars during the special action
        bbm.update_bars_during_action(1, ["f", "s"])
        # Decay 50 calories for the hour spent getting wood
        bbs.immediate_status_bar_decay("Calories", 60)
        # Decay 7 hydration for the hour spent getting wood
        bbs.immediate_status_bar_decay("Hydration", 7)

        # Display the text in a popup
        self.show_popup(text)

    def get_water(self):
        """ Collect dirty or clean water in water bottles """
        # If there are remaining uses of clean water
        if init.game_state.inventory.items["empty_bottle"]["Quantity"] > 0:
            if init.game_state.rain_water_uses > 0:
                init.game_state.inventory.items["water_bottle_safe"]["Quantity"] += init.game_state.inventory.items["empty_bottle"]["Quantity"]
                init.game_state.inventory.items["empty_bottle"]["Quantity"] = 0
                init.game_state.rain_water_uses -= 1
                self.show_popup("My empty bottles were filled with clean water from the rain catcher.")
            # If the location has dirty water
            elif init.game_state.current_location["Key"] in cs.water_locations:
                init.game_state.inventory.items["water_bottle_unsafe"]["Quantity"] += \
                init.game_state.inventory.items["empty_bottle"]["Quantity"]
                init.game_state.inventory.items["empty_bottle"]["Quantity"] = 0
                self.show_popup("My empty bottles were filled with dirty water from a puddle.")
        else:
            self.show_popup("All my bottles are full.")