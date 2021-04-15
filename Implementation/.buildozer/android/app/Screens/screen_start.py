from Initialization import initialization as init
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from Gameplay import file_functions as ff
from kivy.uix.widget import Widget
from kivymd.app import MDApp
import pickle
import time
import os


class StartMenu(Screen):

    class BackgroundStart(Widget):

        this_source = StringProperty(ff.get_path("../Images/start_screen.png"))

    def on_enter(self):
        # Enable game load button if a save file is available
        # self.ids.load_button.disabled = not ff.save_file_exists()
        pass

    def try_loading(self, *args):
        if os.path.isfile(ff.get_path('save_game.pkl')):
            with open(ff.get_path('save_game.pkl'), 'rb') as load_game:
                bob = pickle.load(load_game)
            for vari in vars(init.game_state):
                setattr(init.game_state, vari, getattr(bob, vari))
            init.game_state.start_time += time.time() - init.game_state.save_time
            init.game_state.start_paused_time += time.time() - init.game_state.save_time
            MDApp.get_running_app().root.current = "game"

    def new_game(self, *args):
        MDApp.get_running_app().root.current = "game"
        init.game_state = init.initialize_game_state()
        init.game_state.start_time = time.time()
        init.game_state.time_is_stopped = True
        init.game_state.start_paused_time = time.time()

