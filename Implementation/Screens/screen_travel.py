from Initialization import initialization as init
from Gameplay import game_play_functions as gpf
from Initialization import environment as env
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView
from Screens import GUI_classes as gui
from kivy.uix.button import Button
from kivy.uix.label import Label
import random


class TravelScreen(gui.BaseGameplayScreen):
    """ Screen for the travel menu """

    def travel(self, travel_path):
        """ Travel to a new chosen location"""
        # Get the new location data
        name, miles, duration = init.game_state.travel_next[travel_path]["Name"], init.game_state.travel_next[travel_path]["Miles"], \
                                init.game_state.travel_next[travel_path]["Duration"]
        # Add two extra hours to the travel time if the layer is too hungry
        if init.game_state.status_bars["Calories"].current_value < 400:
            duration += 2
        # Update the action description label text
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

        # Add the lost second for the loading screen
        init.game_state.paused_time += 1

        # Update the status bars during the action
        gpf.update_bars_during_action(duration, ["f", "s"])

        # Check if the player won the ga,e
        if init.game_state.remaining_miles - miles <= 0:
            init.game_state.game_over = "Won"
        else:
            init.game_state.remaining_miles -= miles

        # Remove the calories spent traveling
        gpf.immediate_status_bar_decay("Calories", duration*60)

        # Set the shelter making progress to 0
        init.game_state.shelter_complete = False

        # Take the trash bag from the raincatcher
        init.game_state.rain_catcher_exists = False

        # Randomize the two new location for the next travel
        init.game_state.current_location = init.game_state.travel_next[travel_path]
        init.game_state.travel_next = [env.randomize_location_info(random.choice(list(init.game_state.game_locations.keys())[1:])),
                                       env.randomize_location_info(random.choice(list(init.game_state.game_locations.keys())[1:]))]
