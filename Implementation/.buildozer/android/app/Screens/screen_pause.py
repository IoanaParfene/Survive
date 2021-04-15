from Initialization import initialization as init
from Gameplay import game_play_functions as gpf
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from Gameplay import file_functions as ff
from kivy.uix.widget import Widget
from kivymd.app import MDApp
import pickle
import time


class PauseScreen(Screen):
    class BackgroundPause(Widget):
        this_source = StringProperty(ff.get_path("../Images/pause.jpg"))

    def on_enter(self):
        # Pause game time when entering pause menu
        #gpf.pause_game_time()
        pass

    def access_screen(self, *args):
        MDApp.get_running_app().root.current = "pause"

    def return_game_window(self):
        # root.game_state.time_is_stopped = True
        # self.app.game_state.update_paused_time()
        MDApp.get_running_app().root.current = "game"

    def save_quit_window(self, *args):

        with open(ff.get_path('save_game.pkl'), 'wb') as save_game:
            init.game_state.save_time = time.time()
            pickle.dump(init.game_state, save_game)

        MDApp.get_running_app().root.current = "start"