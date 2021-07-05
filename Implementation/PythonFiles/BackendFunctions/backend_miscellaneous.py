from PythonFiles.BackendFunctions import backend_stats as bbs, backend_time as bbt
from PythonFiles import initialization as init
import random


########################################################################################
# FUNCTIONS USED DURING GAME LOOP UPDATES
########################################################################################

def check_game_over_condition():
    """ Check to see if the game is over"""
    if init.game_state.game_time // 60 > 1 or init.game_state.current_game_day > 1:
        # If game is lost or won
        if init.game_state.game_over != "No":
            return True
    return False


def update_bars_during_action(hours, irrelevant_factors):
    """ Update status bars during fast-forwarding actions like sleep, travel, explore, etc """

    # Update bars each minute during the action
    for index in range(0, int(hours * 60)):
        # Add the passed minute
        init.game_state.skipped_time += 1
        # Update the time
        bbt.update_game_time()
        # Update rain
        update_rain()
        # Get the heat factor code
        fluctuation_code = bbs.get_heat_fluctuation_code()
        # Update the code with the action specific factors
        if fluctuation_code is not None:
            for factor in irrelevant_factors:
                # If the action cancels any factors, add "n" in front of their character in the code
                if fluctuation_code.count("n" + factor) == 0:
                    fluctuation_code = fluctuation_code.split(factor)[0] + "n" + factor + \
                                       fluctuation_code.split(factor)[1]
        # Update the body heat factor
        bbs.update_heat_fluctuation_factor(fluctuation_code)
        # Update the status bars
        bbs.update_status_bars()


########################################################################################
# GAME LOOP UPDATING FUNCTIONS
########################################################################################

def update_rain():
    """ Update rain begin/end/duration """
    # If it is raining
    if init.game_state.raining_now:
        # Get how many hours it has been raining for
        rained_game_hours = (init.game_state.game_time - init.game_state.start_rain_related_time)/60
        # If is has been raining for more than the set raining duration
        if init.game_state.rain_related_duration < rained_game_hours:
            # Stop the rain
            init.game_state.raining_now = False
            # Save the time it stopped raining
            init.game_state.start_rain_related_time = init.game_state.game_time
            # Randomize the duration of the up-coming no-rain period
            init.game_state.rain_related_duration = random.randint(8, 72)
    else:
        not_rained_game_hours = (init.game_state.game_time - init.game_state.start_rain_related_time)/60
        # If the no-rain time is over
        if init.game_state.rain_related_duration < not_rained_game_hours:
            # Start the rain
            init.game_state.raining_now = True
            # Save the time it started raining
            init.game_state.start_rain_related_time = init.game_state.game_time
            # Randomize the duration of the up-coming rain period
            init.game_state.rain_related_duration = random.randint(5, 24)








