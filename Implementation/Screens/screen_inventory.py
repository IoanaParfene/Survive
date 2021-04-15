from kivy.properties import StringProperty, NumericProperty
from Initialization import initialization as init
from Gameplay import game_play_functions as gpf
from kivy.uix.floatlayout import FloatLayout
from Initialization import constants as cs
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivymd.app import MDApp


class InventoryScreen(Screen):

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

    class Inventory(Widget):
        this_source = StringProperty("Images/night.png")

    def access_screen(self, *args):
        MDApp.get_running_app().root.current = "inventory"

    def return_game_window(self, *args):
        MDApp.get_running_app().root.current = "game"

    def change_window(self, new_current_window):
        MDApp.get_running_app().root.current = new_current_window

    def scroll_inventory(self, direction):
        if direction == "up":
            if cs.inventory_display_page > 0:
                cs.inventory_display_page -= 1
        else:
            cs.inventory_display_page += 1

    def change_inventory_category(self, category):
        cs.inventory_display_category = category
        cs.inventory_display_page = 0

    class ItemDescription(FloatLayout):
        my_throw_y = NumericProperty(-5000)
        my_bar_y = NumericProperty(-5000)
        my_get_label_y = NumericProperty(-5000)
        my_get_button_y = NumericProperty(-5000)

        def change_throw_y(self, value):
            self.my_throw_y = MDApp.get_running_app().root.get_center_y() - MDApp.get_running_app().root.get_center_y() + value

        def change_bar_y(self, value):
            self.my_bar_y = MDApp.get_running_app().root.get_center_y() - MDApp.get_running_app().root.get_center_y() + value

        def change_get_button_y(self, value):
            self.my_get_button_y = MDApp.get_running_app().root.get_center_y() - MDApp.get_running_app().root.get_center_y() + value

        def change_get_label_y(self, value):
            self.my_get_label_y = MDApp.get_running_app().root.get_center_y() - MDApp.get_running_app().root.get_center_y() + value

        def dismiss_popup(self):
            MDApp.get_running_app().root.get_screen("inventory").item_popup.dismiss()

        def throw(self, text):
            for key, value in init.game_state.inventory.items.items():
                if init.game_state.inventory.items[key]["Name"] == text:
                    item = init.game_state.inventory.items[key]
            if item["Quantity"] > 0:
                item["Quantity"] -= 1
                item["InventorySpace"] = float(int(item["Quantity"] * item["Weight"]))
                self.ids.item_quantity.text = str(int(item["Quantity"])) + " remaining"
                self.ids.item_space.text = "Space: " + str(int(item["InventorySpace"]))
                if item["Quantity"] == 0:
                    MDApp.get_running_app().root.get_screen("inventory").item_popup.dismiss()

        def bar_action(self, text):
            for key, value in init.game_state.inventory.items.items():
                if init.game_state.inventory.items[key]["Name"] == text:
                    item = init.game_state.inventory.items[key]

            if item["Quantity"] > 0:
                item["Quantity"] -= 1
                item["InventorySpace"] = float(int(item["Quantity"] * item["Weight"]))
                self.ids.item_quantity.text = str(int(item["Quantity"])) + " remaining"
                self.ids.item_space.text = "Space: " + str(int(item["InventorySpace"]))
                for key, value in item["BarActions"].items():
                    for change in item["BarActions"][key]:
                        gpf.immediate_status_bar_increase(change[0], change[1])
                if item["Quantity"] == 0:
                    MDApp.get_running_app().root.get_screen("inventory").item_popup.dismiss()

        def get_action(self, text):
            for key, value in init.game_state.inventory.items.items():
                if init.game_state.inventory.items[key]["Name"] == text:
                    item = init.game_state.inventory.items[key]

            if item["Quantity"] > 0:
                item["Quantity"] -= 1
                item["InventorySpace"] = float(int(item["Quantity"] * item["Weight"]))
                self.ids.item_quantity.text = str(int(item["Quantity"])) + " remaining"
                self.ids.item_space.text = "Space: " + str(int(item["InventorySpace"]))
                for key, value in item["GetActions"].items():
                    received_dict = {}
                    for received_item in item["GetActions"][key]:
                        if received_item not in received_dict.keys():
                            received_dict[received_item] = 1
                        else:
                            received_dict[received_item] += 1
                    for key, value in received_dict.items():
                        init.game_state.inventory.items[key]["Quantity"] += value
                if item["Quantity"] == 0:
                    MDApp.get_running_app().root.get_screen("inventory").item_popup.dismiss()

    def show_popup(self, text):
        show = self.ItemDescription()
        for key, value in init.game_state.inventory.items.items():
            if init.game_state.inventory.items[key]["Name"] == text:
                item = init.game_state.inventory.items[key]

        show.ids.item_quantity.text = str(int(item["Quantity"])) + " remaining"
        show.ids.item_description.text = "      " + item["Description"]
        show.ids.item_name.text = item["Name"]
        show.ids.item_space.text = "Space: " + str(int(item["InventorySpace"]))

        if item["BarActions"] is not None:
            for key, value in item["BarActions"].items():
                show.ids.item_bar_action.text = key
                show.change_bar_y(0.1)
        else:
            show.change_bar_y(5000)

        if item["GetActions"] is not None:
            for key, value in item["GetActions"].items():
                show.ids.item_get_button.text = key

                # received materials dictionary
                received_dict = {}
                for received_item in item["GetActions"][key]:
                    if received_item not in received_dict.keys():
                        received_dict[received_item] = 1
                    else:
                        received_dict[received_item] += 1
                receive_text = "GET: "
                for key, value in received_dict.items():
                    receive_text += str(int(value)) + " " + init.game_state.inventory.items[key]["Name"] + ", "
                receive_text = receive_text[:-2]
                show.ids.item_get_label.text = receive_text

                show.change_get_label_y(0.3)
                show.change_get_button_y(0.4)
        else:
            show.change_get_label_y(5000)
            show.change_get_button_y(5000)

        if item["Throw"]:
            show.change_throw_y(0.1)
        else:
            show.change_throw_y(5000)

        self.item_popup = Popup(title="", separator_height= 0, content=show, pos_hint={"x": 0.35, "y": 0.15},
                           size_hint=(0.62, 0.8), background="Images/black.png")
        self.item_popup.open()
