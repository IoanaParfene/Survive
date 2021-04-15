from Initialization import initialization as init
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from Gameplay import file_functions as ff
from kivy.uix.widget import Widget
from kivymd.app import MDApp
import time


class GameOverScreen(Screen):
    class BackgroundOver(Widget):
        this_source = StringProperty(ff.get_path("..\Images/lost_background.png"))

    def access_screen(self, *args):
        MDApp.get_running_app().root.current = "over"

    def return_main_menu(self, *args):
        init.game_state = init.initialize_game_state()
        init.game_state.start_time = time.time()
        init.game_state.time_is_stopped = True
        init.game_state.start_paused_time = time.time()
        MDApp.get_running_app().root.current = "start"

