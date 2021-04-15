from Gameplay import file_functions as ff, game_play_functions as gpf
from kivy.properties import StringProperty, NumericProperty
from Initialization import initialization as init
from Initialization import environment as env
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.modalview import ModalView
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.clock import Clock
import random



class ActionTime(ModalView):

    def __init__(self, text, **kwargs):
        super(ActionTime, self).__init__(**kwargs)

        # Set the specific text for the action
        self.ids.action_time_label.text = text
        # Call dismiss_view after one second
        Clock.schedule_once(self.dismiss_view, 1)

    def dismiss_view(self, dt):
        self.dismiss()


class TravelScreen(Screen):

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


    def travel(self, travel_path):
        """ Travel to a new chosen location"""
        name, miles, duration = init.game_state.travel_next[travel_path]["Name"], init.game_state.travel_next[travel_path]["Miles"], \
                                init.game_state.travel_next[travel_path]["Duration"]
        if init.game_state.status_bars["Calories"].current_value < 400:
            duration += 2

        text = "Walked for " + str(duration) + " hours and reached " + name + "."

        # Add a popup displaying the action result text
        view = ModalView(pos_hint={"x": 0.0, "y": 0.0}, size_hint=(1.0, 1.0), background="Images/black.png")
        layout = FloatLayout(pos_hint={"x": 0.0, "y": 0.0}, size_hint=(1.0, 1.0))
        layout.add_widget(Label(text=text, pos_hint={"x": 0.1, "y": 0.4}, size_hint=(0.8, 0.5),
                                    font_size=self.height * 0.1, text_size=self.size, halign='center', valign='middle'))
        layout.add_widget(Button(pos_hint={"x": 0.44, "y": 0.3}, size_hint=(0.12, 0.1), font_size=self.height * 0.05,
                       background_color=(2.5, 2.5, 2.5, 1.0), on_release=view.dismiss,
                       color=(0.0, 0.0, 0.0, 1.0), text="OKAY", bold=True))
        view.add_widget(layout)
        view.open()

        init.game_state.paused_time += 1
        init.game_state.skipped_time += duration * 60
        if init.game_state.remaining_miles - miles <= 0:
            init.game_state.game_over = "Won"
        else:
            init.game_state.remaining_miles -= miles

        gpf.immediate_status_bar_decay("Calories", duration*50)
        init.game_state.current_location = init.game_state.travel_next[travel_path]
        init.game_state.travel_next = [env.randomize_location_info(random.choice(list(init.game_state.game_locations.keys())[1:])),
                                       env.randomize_location_info(random.choice(list(init.game_state.game_locations.keys())[1:]))]

    def return_game_window(self, *args):
        MDApp.get_running_app().root.current = "game"

    def change_window(self, new_current_window):
        MDApp.get_running_app().root.current = new_current_window

