from kivy.properties import StringProperty, NumericProperty
from Initialization import initialization as init
from kivy.uix.screenmanager import Screen
from kivy.uix.modalview import ModalView
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivymd.app import MDApp


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


class ActionTime(ModalView):

    def __init__(self, text, **kwargs):
        super(ActionTime, self).__init__(**kwargs)

        # Set the specific text for the action
        self.ids.action_time_label.text = text
        # Call dismiss_view after one second
        Clock.schedule_once(self.dismiss_view, 1)

    def dismiss_view(self, dt):
        self.dismiss()


class Rain(Widget):
    """ Class for the rain animation """

    # The y position of the rain animation
    this_y = NumericProperty(-0.25)

    def show_rain(self, *args):
        """ Change rain animation """
        if init.game_state.raining_now:
            if self.this_y < -0.25:
                self.this_y += 5000
        else:
            if self.this_y > -5000.25:
                self.this_y -= 5000


class BaseGameplayScreen(Screen):

    background = Background()
    rain = Rain()

    def change_window(self, new_current_window):
        MDApp.get_running_app().root.current = new_current_window