from Initialization import initialization as init
from Gameplay import game_play_functions as gpf
from Screens import GUI_classes as gui


class ShelterScreen(gui.BaseGameplayScreen):
    """ Screen for the shelter menu """

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
