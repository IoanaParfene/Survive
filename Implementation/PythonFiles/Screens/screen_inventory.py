from PythonFiles.BackendFunctions import backend_stats as bbs, backend_inventory as bbi
from PythonFiles import constants as cs, initialization as init
from kivy.properties import StringProperty, NumericProperty
from PythonFiles.Widgets import widget_customs as wwc
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivymd.app import MDApp
import random


class InventoryScreen(wwc.BaseGameplayScreen):
    """ Screen for the inventory menu """

    class Inventory(Widget):
        """ The container of the inventory slots """
        # The background image of the inventory container
        this_source = StringProperty("GraphicFiles/night.png")

    def scroll_inventory(self, direction):
        """ Go up or down in the current inventory category page"""
        if direction == "up":
            # If the inventory page is 0 stay there
            if cs.inventory_display_page > 0:
                cs.inventory_display_page -= 1
        else:
            cs.inventory_display_page += 1

    def change_inventory_category(self, category):
        """ Change the inventory category based on player press down input"""
        cs.inventory_display_category = category
        cs.inventory_display_page = 0

    class ItemDescription(FloatLayout):
        """ Class for the GUI close-up item description """
        # Throw away button "y" coordinate value for current item
        my_throw_y = NumericProperty(-5000)
        # Bar modifying action button  "y" coordinate value(Eat,Drink,Bandage)
        my_bar_y = NumericProperty(-5000)
        # Item recycling/using action label "y" coordinate value(Wrap, Slice, Open)
        my_get_label_y = NumericProperty(-5000)
        # Item recycling/using action button"y" coordinate value(Wrap, Slice, Open)
        my_get_button_y = NumericProperty(-5000)

        def change_throw_y(self, value):
            """ Show/hide the position of the throw away button """
            self.my_throw_y = MDApp.get_running_app().root.get_center_y() - MDApp.get_running_app().root.get_center_y() + value

        def change_bar_y(self, value):
            """ Show/hide the position of the bar modifying action button """
            self.my_bar_y = MDApp.get_running_app().root.get_center_y() - MDApp.get_running_app().root.get_center_y() + value

        def change_get_button_y(self, value):
            """ Show/hide the position of the item recycling/using action button """
            self.my_get_button_y = MDApp.get_running_app().root.get_center_y() - MDApp.get_running_app().root.get_center_y() + value

        def change_get_label_y(self, value):
            """ Show/hide the position of the item recycling/using action label """
            self.my_get_label_y = MDApp.get_running_app().root.get_center_y() - MDApp.get_running_app().root.get_center_y() + value

        def dismiss_popup(self):
            """ Hide the item close-up description popup"""
            MDApp.get_running_app().root.get_screen("inventory").item_popup.dismiss()

        def show_popup(self, text):
            """ Show a pop-up with a given text """
            view = ModalView(pos_hint={"x": 0.0, "y": 0.0}, size_hint=(1.0, 1.0), background="GraphicFiles/black.png")
            layout = FloatLayout(pos_hint={"x": 0.0, "y": 0.0}, size_hint=(1.0, 1.0))
            layout.add_widget(Label(text=text, pos_hint={"x": 0.1, "y": 0.4}, size_hint=(0.8, 0.5),
                                    font_size=self.height * 0.1, text_size=self.size, halign='center', valign='middle'))
            layout.add_widget(
                Button(pos_hint={"x": 0.44, "y": 0.3}, size_hint=(0.12, 0.1), font_size=self.height * 0.05,
                       background_color=(2.5, 2.5, 2.5, 1.0), on_release=view.dismiss,
                       color=(0.0, 0.0, 0.0, 1.0), text="OKAY", bold=True))
            view.add_widget(layout)
            view.open()

        def complete_item_specific_action(self, text, action_type):
            """ Throw away, item consuming or recycling action implementation"""
            # Get the item information in the inventory dictionary
            for key, value in init.game_state.inventory.items.items():
                if init.game_state.inventory.items[key]["Name"] == text:
                    item = init.game_state.inventory.items[key]
                    item_key = key
            # If the item exists
            if item["Quantity"] > 0:
                # Remove one unit of the item from the inventory
                item["Quantity"] -= 1
                # Remove the spoil rate of that item
                bbi.remove_item_spoil_rate(item_key, 1)
                # Modify the space occupied by all the item units in the inventory
                item["InventorySpace"] = float(int(item["Quantity"] * item["Weight"]))
                # Modify the GUI item quantity label text
                self.ids.item_quantity.text = str(int(item["Quantity"])) + " remaining"
                # Modify the GUI item occupied space label text
                self.ids.item_space.text = "Space: " + str(int(item["InventorySpace"]))
                # Bar modifying action implementation
                if action_type == "bar":
                    # Modify the status bars affected by the usage of the current item
                    for key, value in item["BarActions"].items():
                        for change in item["BarActions"][key]:
                            bbs.immediate_status_bar_increase(change[0], change[1])
                    # Special situation for the water bottle
                    if item["Name"] == "Safe Water Bottle" or item["Name"] == "Unsafe Water Bottle" or item["Name"] == "Squirrel Juice" or item["Name"] == "Soda Bottle":
                        # Add an empty water bottle
                        init.game_state.inventory.items["empty_bottle"]["Quantity"] += 1
                        # Manage condition damaging consumables
                    if item_key in cs.damaging_consumables.keys():
                        damage = random.randint(cs.damaging_consumables[item_key]["DamageInterval"][0],
                                                cs.damaging_consumables[item_key]["DamageInterval"][1])
                        bbs.immediate_status_bar_decay("Condition", damage)
                        if init.game_state.game_over == "No":
                            self.show_popup("This was not a good idea. I feel really sick.")
                # Item recycling/using action implementation
                if action_type == "get":
                    for key, value in item["GetActions"].items():
                        # Make a dictionary of the items meant to be received after the action
                        received_dict = {}
                        for received_item in item["GetActions"][key]:
                            if received_item not in received_dict.keys():
                                received_dict[received_item] = 1
                            else:
                                received_dict[received_item] += 1
                        # Add the items received by recycling/using the current item to the inventory
                        for key, value in received_dict.items():
                            init.game_state.inventory.items[key]["Quantity"] += value
                            bbi.add_item_spoil_rate(key, value)
                # If there are no more units of a certain item close the close-up popup
                if item["Quantity"] == 0:
                    MDApp.get_running_app().root.get_screen("inventory").item_popup.dismiss()

    def show_popup(self, text):
        """ Show item close-up popup """
        # Get the close-up widget
        show = self.ItemDescription()
        # Get the item information in the inventory dictionary
        for key, value in init.game_state.inventory.items.items():
            if init.game_state.inventory.items[key]["Name"] == text:
                item = init.game_state.inventory.items[key]
        # Update item quantity label text
        show.ids.item_quantity.text = str(int(item["Quantity"])) + " remaining"
        # Update item description label text
        show.ids.item_description.text = "      " + item["Description"]
        # Update item name label text
        show.ids.item_name.text = item["Name"]
        # Update item occupied inventory space label text
        show.ids.item_space.text = "Space: " + str(int(item["InventorySpace"]))

        # Display the bar action button if the item has one
        if item["BarActions"] is not None:
            for key, value in item["BarActions"].items():
                show.ids.item_bar_action.text = key
                # Show the button
                show.change_bar_y(0.1)
        else:
            # Hide the button
            show.change_bar_y(5000)

        # Display the get action button if the item has one
        if item["GetActions"] is not None:
            for key, value in item["GetActions"].items():
                show.ids.item_get_button.text = key
                # Received materials dictionary
                received_dict = {}
                for received_item in item["GetActions"][key]:
                    if received_item not in received_dict.keys():
                        received_dict[received_item] = 1
                    else:
                        received_dict[received_item] += 1
                # Text to show the received resources after the action
                receive_text = "GET: "
                for key, value in received_dict.items():
                    receive_text += str(int(value)) + " " + init.game_state.inventory.items[key]["Name"] + ", "
                receive_text = receive_text[:-2]
                # Updat the label that shows the resources offered for the action
                show.ids.item_get_label.text = receive_text
                # Show the button and the label
                show.change_get_label_y(0.3)
                show.change_get_button_y(0.4)
        else:
            # Hide the button and the label
            show.change_get_label_y(5000)
            show.change_get_button_y(5000)

        # Display the throw away button if the item has one
        if item["Throw"]:
            # Show the button
            show.change_throw_y(0.1)
        else:
            # Hide the button
            show.change_throw_y(5000)

        # Display the item close-up popup
        self.item_popup = Popup(title="", separator_height= 0, content=show, pos_hint={"x": 0.35, "y": 0.15},
                           size_hint=(0.62, 0.8), background="GraphicFiles/black.png")
        self.item_popup.open()
