from Initialization import initialization as init
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from Gameplay import file_functions as ff
from Screens import GUI_classes as gui
from kivy.uix.widget import Widget
from kivymd.app import MDApp
import pickle
import time
import os


class StartMenu(gui.BaseGameplayScreen):
    """ Screen for the main menu """

    class BackgroundStart(Widget):
        """ Background image of the screen """
        this_source = StringProperty(ff.get_path("../Images/start_screen.png"))


    def try_loading(self, *args):
        """ Loading game action """
        # If there exists a save file
        if os.path.isfile(ff.get_path('save_game.pkl')):
            # Get the game_state saved data
            with open(ff.get_path('save_game.pkl'), 'rb') as load_game:
                data = pickle.load(load_game)
            # Populate the current game_state
            for variable in vars(init.game_state):
                setattr(init.game_state, variable, getattr(data, variable))
            # Update the in-game time
            init.game_state.start_time += time.time() - init.game_state.save_time
            init.game_state.start_paused_time += time.time() - init.game_state.save_time
            # Change to the gameplay screen
            MDApp.get_running_app().root.current = "game"

    def new_game(self, *args):
        """ New game action """
        # Change to the gameplay screen
        MDApp.get_running_app().root.current = "game"
        # Initialize a new game_state
        init.game_state = init.initialize_game_state()
        # Initialize the in-game time
        init.game_state.start_time = time.time()
        init.game_state.time_is_stopped = True
        init.game_state.start_paused_time = time.time()

        self.show_popup("My car stopped working...I am in the middle of the woods and it's raining!\n There's mud all over the car tracks. I have to get back to the main road!")

