from Initialization import initialization as init
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivymd.app import MDApp


class CraftingScreen(Screen):

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

    def access_screen(self, *args):
        MDApp.get_running_app().root.current = "crafting"

    def return_game_window(self, *args):
        MDApp.get_running_app().root.current = "game"

    def change_window(self, new_current_window):
        MDApp.get_running_app().root.current = new_current_window