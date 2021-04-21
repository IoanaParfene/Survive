from Initialization import initialization as init
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from Gameplay import file_functions as ff
from kivy.uix.widget import Widget
from kivymd.app import MDApp
import time


class GameOverScreen(Screen):
    """ Screen for the game over message """

    class BackgroundOver(Widget):
        """ Background image of the screen """
        this_source = StringProperty(ff.get_path("..\Images/lost_background.png"))

    def return_main_menu(self, *args):
        """ Return to the main menu and initialize a new game """
        # Initialize the game-state
        init.game_state = init.initialize_game_state()
        # Restart the time
        init.game_state.start_time = time.time()
        # Stop the in-game time
        init.game_state.time_is_stopped = True
        # Save the time spent in the main menu
        init.game_state.start_paused_time = time.time()
        # Change to the start screen
        MDApp.get_running_app().root.current = "start"

