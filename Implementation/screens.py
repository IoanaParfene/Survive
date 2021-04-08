from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.floatlayout import FloatLayout
import variable_initialization as var_init
from kivy.uix.modalview import ModalView
from kivy.uix.widget import Widget
import game_play_functions as gpf
from  kivy.uix.label import Label
from kivy.uix.popup import Popup
import display_functions as df
from kivy.lang import Builder
from kivy.clock import Clock
import status_bars as sb
import game_state as gs
import inventory as inv
import pickle
import random
import time
import os

# Kivy style file
kv = Builder.load_file("survive.kv")

# Initialize Window Manager
sm = ScreenManager(transition=NoTransition())


class GameWindow(Screen):
    class Background(Widget):

        this_source = StringProperty("Images/night.png")

        def change_background(self, *args):
            # background = ObjectProperty()
            game_hours = gs.game_state.game_time / 60
            gs.game_state.current_game_day = int(game_hours / 24 + 1)
            game_hours_today = game_hours % 24
            # print("here",game_hours_today)
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

    def change_window(self, new_current_window):
        if new_current_window == "inventory":
            var_init.inventory_display_category = "A"
            var_init.inventory_display_page = 0
        sm.current = new_current_window

    def explore(self):
        found_items = random.choices([1,2], weights=(70,30), k=1)[0]
        text = "You explored for one hour and found:"
        for index in range(0, found_items):
            if not gs.game_state.current_location["Explorables"]:
                text = "There is nothing left to explore.."
            else:
                gs.game_state.paused_time += 1
                gs.game_state.skipped_time += 60
                gpf.immediate_status_bar_decay("Calories", 50)
                item_position = random.randrange(len(gs.game_state.current_location["Explorables"]))
                item_code = gs.game_state.current_location["Explorables"][item_position]
                print(item_code)
                gs.game_state.current_location["Explorables"].pop(item_position)
                text += " " + var_init.inventory_items[item_code]["Name"] + ","
                gs.game_state.inventory.items[item_code]["Quantity"] += 1
                gpf.immediate_status_bar_decay("Calories", 50)
        text = text[:-1]

        view = ModalView(pos_hint={"x": 0.0,"y":0.25}, size_hint=(1.0, 0.5), background="Images/black.png")
        view.add_widget(Label(text=text, pos_hint={"x": 0.1,"y":0.25}, size_hint=(0.8, 0.5),
                              font_size=self.height*0.05, text_size=self.size, halign='center', valign='middle'))
        view.open()
        print(text)


class StartMenu(Screen):
    class BackgroundStart(Widget):

        this_source = StringProperty(df.get_path("Images/start_screen.png"))

    def try_loading(self, *args):
        if os.path.isfile(df.get_path('save_game.pkl')):
            with open(df.get_path('save_game.pkl'), 'rb') as load_game:
                bob = pickle.load(load_game)
            for vari in vars(gs.game_state):
                setattr(gs.game_state, vari, getattr(bob, vari))
            gs.game_state.start_time += time.time() - gs.game_state.save_time
            gs.game_state.start_paused_time += time.time() - gs.game_state.save_time
            sm.current = "game"
        # pass

    def new_game(self, *args):
        sm.current = "game"
        # Initialize game elements
        status_bars = sb.initialize_status_bars()
        inventory = inv.initialize_inventory()
        gs.game_state = gs.GameState(status_bars, inventory)
        gs.game_state.start_time = time.time()
        gs.game_state.time_is_stopped = True
        gs.game_state.start_paused_time = time.time()


class GameOverScreen(Screen):
    class BackgroundOver(Widget):
        this_source = StringProperty(df.get_path("Images/lost_background.png"))

    def access_screen(self, *args):
        sm.current = "over"

    def return_main_menu(self, *args):
        status_bars = sb.initialize_status_bars()
        inventory = inv.initialize_inventory()
        gs.game_over = "No"
        gs.game_state = gs.GameState(status_bars, inventory)
        gs.game_state.start_time = time.time()
        gs.game_state.time_is_stopped = True
        gs.game_state.start_paused_time = time.time()

        sm.current = "start"


class PauseScreen(Screen):
    class BackgroundPause(Widget):
        this_source = StringProperty(df.get_path("Images/pause.jpg"))

    def access_screen(self, *args):
        sm.current = "pause"

    def return_game_window(self):
        # root.game_state.time_is_stopped = True
        # self.app.game_state.update_paused_time()
        sm.current = "game"

    def save_quit_window(self, *args):
        # pass
        with open(df.get_path('save_game.pkl'), 'wb') as save_game:
            gs.game_state.save_time = time.time()
            pickle.dump(gs.game_state, save_game)
        # print(gs.game_state.remaining_miles)
        sm.current = "start"


class ShelterScreen(Screen):
    class BackgroundShelter(Widget):
        this_source = StringProperty(df.get_path("Images/shelter_background.png"))

    def access_screen(self, *args):
        sm.current = "shelter"

    def return_game_window(self, *args):
        sm.current = "game"

    class ActionMessage(Widget):
        my_y = NumericProperty(sm.get_center_y() - 5000)

        def change_y(self, value):
            self.my_y = sm.get_center_y() - sm.get_center_y() - value

    def message_action(self, *args):
        time.sleep(1)
        self.ids.action_message.change_y(5000)

    def rest(self, hours):
        self.ids.action_message.change_y(0)
        Clock.schedule_once(self.message_action, 1 / 600)
        gs.game_state.paused_time += 1
        gs.game_state.skipped_time += hours * 60
        if min(100, gs.game_state.status_bars["Condition"].current_value + 3) == 100:
            gs.game_state.status_bars["Condition"].current_value = 100
        else:
            gs.game_state.status_bars["Condition"].current_value += hours * 4

    def change_window(self, new_current_window):
        sm.current = new_current_window


class FireScreen(Screen):

    def access_screen(self, *args):
        sm.current = "fire"

    def return_game_window(self, *args):
        sm.current = "game"

    def change_window(self, new_current_window):
        sm.current = new_current_window


class CraftingScreen(Screen):

    def access_screen(self, *args):
        sm.current = "crafting"

    def return_game_window(self, *args):
        sm.current = "game"

    def change_window(self, new_current_window):
        sm.current = new_current_window


class InventoryScreen(Screen):

    class Background(Widget):
        this_source = StringProperty("Images/night.png")

    class Inventory(Widget):
        this_source = StringProperty("Images/night.png")

    def access_screen(self, *args):
        sm.current = "inventory"

    def return_game_window(self, *args):
        sm.current = "game"

    def change_window(self, new_current_window):
        sm.current = new_current_window

    def scroll_inventory(self, direction):
        if direction == "up":
            if var_init.inventory_display_page > 0:
                var_init.inventory_display_page -= 1
        else:
            var_init.inventory_display_page += 1

    def change_inventory_category(self, category):
        var_init.inventory_display_category = category
        var_init.inventory_display_page = 0

    class ItemDescription(FloatLayout):
        my_throw_y = NumericProperty(sm.get_center_y() - 5000)
        my_bar_y = NumericProperty(sm.get_center_y() - 5000)
        my_get_label_y = NumericProperty(sm.get_center_y() - 5000)
        my_get_button_y = NumericProperty(sm.get_center_y() - 5000)

        def change_throw_y(self, value):
            self.my_throw_y = sm.get_center_y() - sm.get_center_y() + value

        def change_bar_y(self, value):
            self.my_bar_y = sm.get_center_y() - sm.get_center_y() + value

        def change_get_button_y(self, value):
            self.my_get_button_y = sm.get_center_y() - sm.get_center_y() + value

        def change_get_label_y(self, value):
            self.my_get_label_y = sm.get_center_y() - sm.get_center_y() + value

        def dismiss_popup(self):
            sm.get_screen("inventory").item_popup.dismiss()

        def throw(self, text):
            for key, value in gs.game_state.inventory.items.items():
                if gs.game_state.inventory.items[key]["Name"] == text:
                    item = gs.game_state.inventory.items[key]
            if item["Quantity"] > 0:
                item["Quantity"] -= 1
                item["InventorySpace"] = float(int(item["Quantity"] * item["Weight"]))
                self.ids.item_quantity.text = str(int(item["Quantity"])) + " remaining"
                self.ids.item_weight.text = "Weight: " + str(int(item["InventorySpace"]))
                if item["Quantity"] == 0:
                    sm.get_screen("inventory").item_popup.dismiss()

        def bar_action(self, text):
            for key, value in gs.game_state.inventory.items.items():
                if gs.game_state.inventory.items[key]["Name"] == text:
                    item = gs.game_state.inventory.items[key]

            if item["Quantity"] > 0:
                item["Quantity"] -= 1
                item["InventorySpace"] = float(int(item["Quantity"] * item["Weight"]))
                self.ids.item_quantity.text = str(int(item["Quantity"])) + " remaining"
                self.ids.item_weight.text = "Weight: " + str(int(item["InventorySpace"]))
                for key, value in item["BarActions"].items():
                    for change in item["BarActions"][key]:
                        gpf.immediate_status_bar_increase(change[0], change[1])
                if item["Quantity"] == 0:
                    sm.get_screen("inventory").item_popup.dismiss()

        def get_action(self, text):
            for key, value in gs.game_state.inventory.items.items():
                if gs.game_state.inventory.items[key]["Name"] == text:
                    item = gs.game_state.inventory.items[key]

            if item["Quantity"] > 0:
                item["Quantity"] -= 1
                item["InventorySpace"] = float(int(item["Quantity"] * item["Weight"]))
                self.ids.item_quantity.text = str(int(item["Quantity"])) + " remaining"
                self.ids.item_weight.text = "Weight: " + str(int(item["InventorySpace"]))
                for key, value in item["GetActions"].items():
                    received_dict = {}
                    for received_item in item["GetActions"][key]:
                        if received_item not in received_dict.keys():
                            received_dict[received_item] = 1
                        else:
                            received_dict[received_item] += 1
                    for key, value in received_dict.items():
                        gs.game_state.inventory.items[key]["Quantity"] += value
                if item["Quantity"] == 0:
                    sm.get_screen("inventory").item_popup.dismiss()

    def show_popup(self, text):
        show = self.ItemDescription()
        for key, value in gs.game_state.inventory.items.items():
            if gs.game_state.inventory.items[key]["Name"] == text:
                item = gs.game_state.inventory.items[key]
        show.ids.item_quantity.text = str(int(item["Quantity"])) + " remaining"
        show.ids.item_description.text = "      " + item["Description"]
        show.ids.item_name.text = item["Name"]
        show.ids.item_weight.text = "Weight: " + str(int(item["InventorySpace"]))

        if item["BarActions"] is not None:
            print(item["BarActions"])
            for key, value in item["BarActions"].items():
                show.ids.item_bar_action.text = key
                show.change_bar_y(0.1)
        else:
            show.change_bar_y(5000)

        if item["GetActions"] is not None:
            print(item["GetActions"])
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
                    receive_text += str(int(value)) + " " + gs.game_state.inventory.items[key]["Name"] + ", "
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



class HuntingScreen(Screen):

    def access_screen(self, *args):
        sm.current = "hunting"

    def return_game_window(self, *args):
        sm.current = "game"

    def change_window(self, new_current_window):
        sm.current = new_current_window


class TravelScreen(Screen):

    class BackgroundTravel(Widget):
        this_source = StringProperty(df.get_path("Images/shelter_background.png"))


    class ActionMessageTravel(Widget):
        my_y = NumericProperty(sm.get_center_y() - 5000)

        def change_y(self, value):
            self.my_y = sm.get_center_y() - sm.get_center_y() - value

    def message_action(self, *args):
        time.sleep(1)
        self.ids.action_message_travel.change_y(5000)

    def travel(self, travel_path):
        """ Travel to a new chosen location"""
        self.ids.action_message_travel.change_y(0)
        Clock.schedule_once(self.message_action, 1)
        name, miles, duration = gs.game_state.travel_next[travel_path]["Name"], gs.game_state.travel_next[travel_path]["Miles"], \
                                gs.game_state.travel_next[travel_path]["Duration"]
        if gs.game_state.status_bars["Calories"].current_value < 400:
            duration += 2

        gs.game_state.paused_time += 1
        gs.game_state.skipped_time += duration * 60
        if gs.game_state.remaining_miles - miles <= 0:
            gs.game_state.game_over = "Won"
        else:
            gs.game_state.remaining_miles -= miles

        gpf.immediate_status_bar_decay("Calories", duration*50)
        gs.game_state.current_location = gs.game_state.travel_next[travel_path]
        gs.game_state.travel_next = [gs.randomize_location_info(random.choice(list(gs.game_state.game_locations.keys())[1:])),
                                    gs.randomize_location_info(random.choice(list(gs.game_state.game_locations.keys())[1:]))]

    def return_game_window(self, *args):
        sm.current = "game"

    def change_window(self, new_current_window):
        sm.current = new_current_window


# Game screens/windows/menus
screens = [StartMenu(name="start"), GameWindow(name="game"), GameOverScreen(name="over"), PauseScreen(name="pause"),
           ShelterScreen(name="shelter"), FireScreen(name="fire"), CraftingScreen(name="crafting"),
           InventoryScreen(name="inventory"), HuntingScreen(name="hunting"), TravelScreen(name="travel")]
for screen in screens:
    sm.add_widget(screen)
sm.current = "start"
