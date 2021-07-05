from kivy.properties import StringProperty, NumericProperty
from PythonFiles import initialization as init
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.modalview import ModalView
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivymd.app import MDApp
import random

class Background(Widget):
    """ Class for changing the background during the day """

    # The path to background image
    this_source = StringProperty("GraphicFiles/night.png")

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
            self.this_source = "GraphicFiles/dawn.png"
        if game_hours_today < 7:
            self.this_source = "GraphicFiles/orange.png"
        elif game_hours_today < 10:
            self.this_source = "GraphicFiles/purple.png"
        elif game_hours_today < 12:
            self.this_source = "GraphicFiles/sunset.png"
        else:
            self.this_source = "GraphicFiles/night.png"


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
    """ Base class for gameplay menu screens """

    # Background animation object
    background = Background()
    # Rain animation object
    rain = Rain()

    def change_window(self, new_current_window):
        """ Screen changing method """
        MDApp.get_running_app().root.current = new_current_window

    def check_night_action(self):
        """ Return if it is too dark to do a specific action and if the player has a flashlight"""

        # Return variables
        too_dark = False
        has_flashlight = False

        # Check if the player has a flashlight
        if init.game_state.inventory.items["flashlight"]["Quantity"] > 0:
            has_flashlight = True

        # If it is night, randomize if it is also too dark
        if not init.game_state.daylight_now:
            too_dark = random.choices([True, False], weights=(70, 30), k=1)[0]

        if too_dark:
            if has_flashlight:
                text = "Good thing I have a flashlight! "
            else:
                text = "It's too dark! I can't see anything! "
        else:
            text = ""

        return too_dark, has_flashlight, text

    def show_popup(self, text, *args):
        """ Show a pop-up with a given text """
        # Get font size
        if len(args) > 0:
            font_size = args[0]
        else:
            font_size = 0.06
        view = ModalView(pos_hint={"x": 0.0, "y": 0.0}, size_hint=(1.0, 1.0), background="GraphicFiles/black.png")
        layout = FloatLayout(pos_hint={"x": 0.0, "y": 0.0}, size_hint=(1.0, 1.0))
        layout.add_widget(Label(text=text, pos_hint={"x": 0.1, "y": 0.4}, size_hint=(0.8, 0.5),
                                font_size=self.height * font_size, text_size=self.size, halign='center', valign='middle'))
        layout.add_widget(Button(pos_hint={"x": 0.44, "y": 0.3}, size_hint=(0.12, 0.1), font_size=self.height * 0.05,
                                 background_color=(2.5, 2.5, 2.5, 1.0), on_release=view.dismiss,
                                 color=(0.0, 0.0, 0.0, 1.0), text="OKAY", bold=True))
        view.add_widget(layout)
        view.open()


class DescriptionLabel(FloatLayout):
    """ Universal label for displaying a message on the screen """

    # Position coordinates of the label
    pos_x = NumericProperty(-500)
    pos_y = NumericProperty(-500)

    # Size of the label
    size_x = NumericProperty(-500)
    size_y = NumericProperty(-500)

    # Size scale
    scale = NumericProperty(-500)

    def __init__(self, text, pos_x, pos_y, size_x, size_y, h_align, v_align, scale, **kwargs):
        super(DescriptionLabel, self).__init__(**kwargs)
        # Set the specific text for the label
        self.text = text
        # Set the position of the label
        self.pos_x = pos_x
        self.pos_y = pos_y
        # Set the size of the label
        self.size_x = size_x
        self.size_y = size_y
        # Set alignments
        self.halign = h_align
        self.valign = v_align
        self.scale = scale

    def dismiss_view(self, dt):
        """ Label deleting method """
        self.dismiss()
