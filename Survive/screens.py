from kivy.properties import ObjectProperty, StringProperty, BooleanProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
import Survive.variable_initialization as var_init
import Survive.game_state as gs
from kivy.lang import Builder
from kivy.clock import Clock
import time
from kivy.uix.widget import Widget
from kivy.uix.image import Image
import pickle
import os
import Survive.game_state as gs
import Survive.initialization as init

# Kivy style file
kv = Builder.load_file("survive.kv")


# Window/menu manager
"""class WindowManager(ScreenManager):
    ScreenManager.transition = NoTransition()
    pass"""

# Initialize Window Manager
sm = ScreenManager(transition=NoTransition())


class GameWindow(Screen):

    class Background(Widget):

        this_source = StringProperty("Images/night.png")

        def change_background(self, *args):
            #background = ObjectProperty()
            game_hours = gs.game_state.game_time / 60
            gs.game_state.current_game_day = int(game_hours / 24 + 1)
            game_hours_today = game_hours % 24
            #print("here",game_hours_today)
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
        sm.current = new_current_window


class StartMenu(Screen):

    class BackgroundStart(Widget):

        this_source = StringProperty(var_init.get_path("Images/start_screen.png"))


    def try_loading(self, *args):
        if os.path.isfile(var_init.get_path('save_game.pkl')):
            with open(var_init.get_path('save_game.pkl'), 'rb') as load_game:
                bob = pickle.load(load_game)
            for vari in vars(gs.game_state):
                setattr(gs.game_state, vari, getattr(bob, vari))
            gs.game_state.start_time += time.time() - gs.game_state.save_time
            gs.game_state.start_paused_time += time.time() - gs.game_state.save_time
            sm.current = "game"
        #pass

    def new_game(self, *args):
        sm.current = "game"
        # Initialize game elements
        status_bars = init.initialize_game()
        gs.game_state = gs.GameState(status_bars)
        gs.game_state.start_time = time.time()
        gs.game_state.time_is_stopped = True
        gs.game_state.start_paused_time = time.time()


class GameOverScreen(Screen):

    class BackgroundOver(Widget):

        this_source = StringProperty(var_init.get_path("Images/pause.jpg"))

    def access_screen(self, *args):
        sm.current = "over"

    def return_main_menu(self, *args):
        status_bars = init.initialize_game()
        gs.game_over = "No"
        gs.game_state = gs.GameState(status_bars)
        gs.game_state.start_time = time.time()
        gs.game_state.time_is_stopped = True
        gs.game_state.start_paused_time = time.time()

        sm.current = "start"


class PauseScreen(Screen):

    class BackgroundPause(Widget):

        this_source = StringProperty(var_init.get_path("Images/pause.jpg"))

    def access_screen(self, *args):
        sm.current = "pause"

    def return_game_window(self):
        #root.game_state.time_is_stopped = True
        #self.app.game_state.update_paused_time()
        sm.current = "game"

    def save_quit_window(self, *args):
        #pass
        with open(var_init.get_path('save_game.pkl'), 'wb') as save_game:
            gs.game_state.save_time = time.time()
            pickle.dump(gs.game_state, save_game)
        #print(gs.game_state.remaining_miles)
        sm.current = "start"


class ShelterScreen(Screen):

    class BackgroundShelter(Widget):
        this_source = StringProperty(var_init.get_path("Images/shelter_background.png"))

    def access_screen(self, *args):
        sm.current = "shelter"

    def return_game_window(self, *args):
        sm.current = "game"

    class ActionMessage(Widget):
        my_y = NumericProperty(sm.get_center_y()-5000)

        def change_y(self, value):
            self.my_y = sm.get_center_y() -sm.get_center_y()- value

    def message_action(self, *args):
        time.sleep(2)
        self.ids.action_message.change_y(5000)

    def rest_1_h(self, *args):
        self.ids.action_message.change_y(0)
        Clock.schedule_once(self.message_action, 1/600)
        gs.game_state.paused_time += 2
        gs.game_state.skipped_time += 60
        gs.game_state.action_effect("sleep1")
        if min(100, gs.game_state.status_bars["Condition"].current_value + 3) == 100:
            gs.game_state.status_bars["Condition"].current_value = 100
        else:
            gs.game_state.status_bars["Condition"].current_value += 4
        print(gs.game_state.skipped_time)


    def rest_4_h(self, *args):
        self.ids.action_message.change_y(0)
        Clock.schedule_once(self.message_action, 1/600)
        gs.game_state.paused_time += 2
        gs.game_state.skipped_time += 4 * 60
        gs.game_state.action_effect("sleep4")
        if min(100, gs.game_state.status_bars["Condition"].current_value + 3) == 100:
            gs.game_state.status_bars["Condition"].current_value = 100
        else:
            gs.game_state.status_bars["Condition"].current_value += 16
        print(gs.game_state.skipped_time)

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

    def access_screen(self, *args):
        sm.current = "inventory"

    def return_game_window(self, *args):
        sm.current = "game"

    def change_window(self, new_current_window):
        sm.current = new_current_window

class HuntingScreen(Screen):

    def access_screen(self, *args):
        sm.current = "hunting"

    def return_game_window(self, *args):
        sm.current = "game"

    def change_window(self, new_current_window):
        sm.current = new_current_window

class TravelScreen(Screen):

    class BackgroundTravel(Widget):
        this_source = StringProperty(var_init.get_path("Images/shelter_background.png"))

    def access_screen(self, *args):
        sm.current = "travel"

    def return_game_window(self, *args):
        sm.current = "game"

    def travel(self, choice):
        print("Travel", choice)
        gs.game_state.travel(choice)
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
