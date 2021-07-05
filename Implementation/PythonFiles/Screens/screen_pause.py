from PythonFiles.BackendFunctions import backend_os as bbo
from PythonFiles import initialization as init
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivymd.app import MDApp
import pickle
import time


class PauseScreen(Screen):
    """ Screen for the pause menu """

    class BackgroundPause(Widget):
        """ Background image of the screen """
        this_source = StringProperty(bbo.get_path("../../GraphicFiles/pause.jpg"))

    def save_quit_window(self, *args):
        """ Save and quit action implementation """
        with open(bbo.get_path('save_game.pkl'), 'wb') as save_game:
            # Add the game_state to the .pkl file
            init.game_state.save_time = time.time()
            pickle.dump(init.game_state, save_game)
        # Change to the main menu
        MDApp.get_running_app().root.current = "start"

    def change_window(self, new_current_window):
        """ Change to the new selected screen """
        MDApp.get_running_app().root.current = new_current_window