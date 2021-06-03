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

    light_inventory = False

    def travel(self, travel_path):
        """ Travel to a new chosen location"""

        # If the player's inventory is light enough to travel
        if init.game_state.inventory.current_capacity > init.game_state.inventory.max_capacity:
            self.light_inventory = False
            text = "I carry too much to travel."
            self.show_popup(text)
        else:
            self.light_inventory = True
            # Get the new location data
            name, miles, duration = init.game_state.travel_next[travel_path]["Name"], init.game_state.travel_next[travel_path]["Miles"], \
                                    init.game_state.travel_next[travel_path]["Duration"]
            # Add two extra hours to the travel time if the layer is too hungry
            if init.game_state.status_bars["Calories"].current_value < 400:
                duration += 2
            # Update the action description label text
            text = "Walked for " + str(duration) + " hours and reached " + name + "."
            self.show_popup(text)

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

            # Lose the water from the rain catcher
            init.game_state.rain_water_uses = 0

            # Remove traps
            for trap_type, info in init.game_state.traps.items():
                info["Quantity"] = 0

            # Randomize the two new location for the next travel
            init.game_state.current_location = init.game_state.travel_next[travel_path]
            init.game_state.travel_next = [env.randomize_location_info(random.choice(list(init.game_state.game_locations.keys())[1:])),
                                           env.randomize_location_info(random.choice(list(init.game_state.game_locations.keys())[1:]))]
