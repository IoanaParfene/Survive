from Initialization import initialization as init
from Gameplay import game_play_functions as gpf
from Initialization import constants as cs
from Screens import GUI_classes as gui


class ShelterScreen(gui.BaseGameplayScreen):
    """ Screen for the shelter menu """

    def show_info(self):
        self.show_popup(cs.shelter_screen_info)

    def rest(self, hours):
        """ Sleep action implementation """
        # Add the lost second for the loading screen
        init.game_state.paused_time += 1
        # Update the status bars during the special action
        gpf.update_bars_during_action(hours, [])
        # Add condition increase
        if min(100, init.game_state.status_bars["Condition"].current_value + 3) == 100:
            init.game_state.status_bars["Condition"].current_value = 100
        else:
            init.game_state.status_bars["Condition"].current_value += hours * 4

    def build_raincatcher(self, hours):
        """ Build raincatcher from a plastic bag"""
        # Add the lost second for the loading screen
        init.game_state.paused_time += 1
        # Update the status bars during the special action
        gpf.update_bars_during_action(hours, [])
        # Add rain catcher existence to the game-state object
        init.game_state.rain_catcher_exists = True
        self.show_popup("I built a rain catcher. It took 15 minutes.")