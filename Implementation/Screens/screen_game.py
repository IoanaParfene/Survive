from Initialization import initialization as init
from Gameplay import game_play_functions as gpf
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from Initialization import constants as cs
from kivy.uix.screenmanager import Screen
from kivy.uix.modalview import ModalView
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.clock import Clock
import random


class ActionTime(ModalView):

    def __init__(self, text, **kwargs):
        super(ActionTime, self).__init__(**kwargs)

        # Set the specific text for the action
        self.ids.action_time_label.text = text
        # Call dismiss_view after one second
        Clock.schedule_once(self.dismiss_view, 1)

    def dismiss_view(self, dt):
        self.dismiss()


class GameWindow(Screen):


    class Background(Widget):
        """ Class for changing the background during the day """

        # The path to background image
        this_source = StringProperty("Images/night.png")

        def change_background(self, *args):
            """ Change background after the day period """
            # Total game hours that have passed
            game_hours = init.game_state.game_time / 60
            # The current day of the game
            init.game_state.current_game_day = int(game_hours / 24 + 1)
            # Game hours that have passed in the current day
            game_hours_today = game_hours % 24

            # Change background image path based on the time of the current day
            if game_hours_today < 2:
                self.this_source = "Images/dawn.png"
            if game_hours_today < 7:
                self.this_source = "Images/orange.png"
            elif game_hours_today < 10:
                self.this_source = "Images/purple.png"
            elif game_hours_today < 12:
                self.this_source = "Images/sunset.png"
            else:
                self.this_source = "Images/night.png"

    def on_enter(self):
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
        found_items = random.choices([1,2], weights=(70,30), k=1)[0]

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
            # Pass one game hour
            init.game_state.paused_time += 1
            init.game_state.skipped_time += 60
            # Decay 50 calories for the hour spent exploring
            gpf.immediate_status_bar_decay("Calories", 50)
        else:
            text = "There is nothing left to explore.."
        # Clean the text
        text = text[:-1]

        # Add a popup displaying the action result text
        view = ModalView(pos_hint={"x": 0.0,"y":0.0}, size_hint=(1.0, 1.0), background="Images/black.png")
        layout = FloatLayout(pos_hint={"x": 0.0,"y":0.0}, size_hint=(1.0, 1.0))
        layout.add_widget(Label(text=text, pos_hint={"x": 0.1,"y":0.4}, size_hint=(0.8, 0.5),
                              font_size=self.height*0.1, text_size=self.size, halign='center', valign='middle'))
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

        # Pass one game hour
        init.game_state.paused_time += 1
        init.game_state.skipped_time += 60
        # Decay 50 calories for the hour spent getting wood
        gpf.immediate_status_bar_decay("Calories", 50)

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
