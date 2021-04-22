from Initialization import initialization as init
from Gameplay import game_play_functions as gpf
from kivy.uix.floatlayout import FloatLayout
from Initialization import constants as cs
from kivy.uix.modalview import ModalView
from Screens import GUI_classes as gui
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.app import MDApp
import random


class GameWindow(gui.BaseGameplayScreen):
    """ Screen for the gameplay menu """

    def on_enter(self):
        """ Called when entering the screen """
        # Don't allow getting wood at Pike Lake
        if init.game_state.current_location["Name"] == "Pike Lake":
            MDApp.get_running_app().root.get_screen("game").ids.wood_button.disabled = True
        else:
            MDApp.get_running_app().root.get_screen("game").ids.wood_button.disabled = False
        pass

    def change_window(self, new_current_window):
        """ Change game screen based on a button press """
        # If entering the inventor from the game menu, display the first page of the first item category
        if new_current_window == "inventory":
            cs.inventory_display_category = "A"
            cs.inventory_display_page = 0
        # Change the screen
        MDApp.get_running_app().root.current = new_current_window

    def explore(self):
        """ Explore action implementation"""

        # Randomize a number of items to find during the current exploration
        found_items = random.choices([1, 2], weights=(70, 30), k=1)[0]

        # Prepare action result text
        text = "You explored for one hour and found:"

        # Flag for passing one game hour, if at least one item was found
        items_were_found = False
        # Choose the item/items from the current location's available item list
        for index in range(0, found_items):
            # If there are remaining items to find, randomly choose one
            if init.game_state.current_location["Explorables"]:
                # Pass one game hour for at least this item
                items_were_found = True
                # Choose one remaining item as a list index
                item_position = random.randrange(len(init.game_state.current_location["Explorables"]))
                # Get the code of the item
                item_code = init.game_state.current_location["Explorables"][item_position]
                # Remove the item from the list
                init.game_state.current_location["Explorables"].pop(item_position)
                # Update the item quantity in the inventory
                init.game_state.inventory.items[item_code]["Quantity"] += 1
                # Update the action result text
                text += " " + cs.inventory_items[item_code]["Name"] + ","

        # Pass one game hour if any items were found and change the action result text
        if items_were_found:
            # Add the lost second for the loading screen
            init.game_state.paused_time += 1
            # Update the status bars during the special action
            gpf.update_bars_during_action(1, ["f", "s"])
        else:
            text = "There is nothing left to explore.."
        # Clean the text
        text = text[:-1]

        # Add a popup displaying the action result text
        view = ModalView(pos_hint={"x": 0.0, "y": 0.0}, size_hint=(1.0, 1.0), background="Images/black.png")
        layout = FloatLayout(pos_hint={"x": 0.0, "y": 0.0}, size_hint=(1.0, 1.0))
        layout.add_widget(Label(text=text, pos_hint={"x": 0.1, "y": 0.4}, size_hint=(0.8, 0.5),
                                font_size=self.height * 0.1, text_size=self.size, halign='center', valign='middle'))
        layout.add_widget(Button(pos_hint={"x": 0.44, "y": 0.3}, size_hint=(0.12, 0.1), font_size=self.height * 0.05,
                                 background_color=(2.5, 2.5, 2.5, 1.0), on_release=view.dismiss,
                                 color=(0.0, 0.0, 0.0, 1.0), text="OKAY", bold=True))
        view.add_widget(layout)
        view.open()

    def get_wood(self):
        """ Get wood action implementation """

        # Randomize a number of wood logs to find during the current exploration
        found_wood_logs = random.choices([2, 3], weights=(70, 30), k=1)[0]
        # Boolean to see if there will be a hardwood log found as well
        found_hardwood_logs = random.choices([True, False], weights=(10, 90), k=1)[0]

        # Prepare action result text
        text = "You found: Wood(" + str(found_wood_logs) + "),"
        # Add the hardwood to the text
        if found_hardwood_logs:
            text += " Hardwood(1),"
        # Clean the text
        text = text[:-1]

        # Add the lost second for the loading screen
        init.game_state.paused_time += 1
        # Update the status bars during the special action
        gpf.update_bars_during_action(1, ["f", "s"])

        # Decay 50 calories for the hour spent getting wood
        gpf.immediate_status_bar_decay("Calories", 60)
        # Decay 7 hydration for the hour spent getting wood
        gpf.immediate_status_bar_decay("Hydration", 7)

        # Add the wood to the inventory
        init.game_state.inventory.items["wood"]["Quantity"] += found_wood_logs
        # Add the hardwood to the inventory
        if found_hardwood_logs:
            init.game_state.inventory.items["hardwood"]["Quantity"] += 1

        # Add a popup displaying the action result text
        view = ModalView(pos_hint={"x": 0.0, "y": 0.0}, size_hint=(1.0, 1.0), background="Images/black.png")
        layout = FloatLayout(pos_hint={"x": 0.0, "y": 0.0}, size_hint=(1.0, 1.0))
        layout.add_widget(Label(text=text, pos_hint={"x": 0.1, "y": 0.4}, size_hint=(0.8, 0.5),
                                font_size=self.height * 0.1, text_size=self.size, halign='center', valign='middle'))
        layout.add_widget(Button(pos_hint={"x": 0.44, "y": 0.3}, size_hint=(0.12, 0.1), font_size=self.height * 0.05,
                                 background_color=(2.5, 2.5, 2.5, 1.0), on_release=view.dismiss,
                                 color=(0.0, 0.0, 0.0, 1.0), text="OKAY", bold=True))
        view.add_widget(layout)
        view.open()

    def get_water(self):
        """ Collect dirty or clean water in water bottles """
        if init.game_state.rain_water_uses > 0:
            init.game_state.inventory.items["water_bottle_safe"]["Quantity"] += init.game_state.inventory.items["empty_bottle"]["Quantity"]
            init.game_state.inventory.items["empty_bottle"]["Quantity"] = 0
            init.game_state.inventory.items["empty_bottle"]["Quantity"] = 0
            init.game_state.rain_water_uses -= 1
