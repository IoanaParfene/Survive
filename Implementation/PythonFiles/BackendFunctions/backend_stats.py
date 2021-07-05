from PythonFiles import constants as cs, initialization as init


########################################################################################
# FUNCTIONS USED DURING GAME LOOP UPDATES
########################################################################################

def gradual_status_bar_fluctuation(status_bar_name):
    """ Apply value change factors of current bar for each of their time intervals """
    status_bars = init.game_state.status_bars
    if status_bars[status_bar_name].fluctuation is not None:
        item = status_bars[status_bar_name].fluctuation
        # Fluctuation supposed to happen based on passed game time
        fluctuation_counter = init.game_state.game_time // item[1]
        if abs(fluctuation_counter - item[2]) > 0:
            if status_bar_name == "Body Heat":
                pass
            if not int(status_bars[status_bar_name].current_value - abs(fluctuation_counter - item[2]) * item[0]) < (-status_bars[status_bar_name].max_value / 10):
                status_bars[status_bar_name].current_value = min(status_bars[status_bar_name].current_value - abs(fluctuation_counter - item[2]) * item[0], status_bars[status_bar_name].max_value)
                #status_bars[status_bar_name].current_value = status_bars[status_bar_name].current_value - abs(fluctuation_counter - item[2]) * item[0]
                if (-status_bars[status_bar_name].max_value / 7) < status_bars[status_bar_name].current_value < (-status_bars[status_bar_name].max_value / 15):
                    if status_bar_name != "Calories":
                        init.game_state.game_over = "Lost"
            # Last fluctuation that happened based on passed game time
            item[2] = fluctuation_counter


def immediate_status_bar_decay(status_bar_name, damage):
    """ Take immediate decay based on damage of a certain action"""
    status_bars = init.game_state.status_bars
    status_bars[status_bar_name].current_value -= damage
    if status_bars[status_bar_name].current_value - damage < (-status_bars[status_bar_name].max_value / 20):
        if status_bar_name != "Calories":
            init.game_state.game_over = "Lost"


def immediate_status_bar_increase(status_bar_name, increase):
    """ Immediate increase in value based on certain action """
    status_bars = init.game_state.status_bars
    if min(status_bars[status_bar_name].max_value, status_bars[status_bar_name].current_value + increase) == status_bars[status_bar_name].max_value:
        status_bars[status_bar_name].current_value = status_bars[status_bar_name].max_value
    elif status_bars[status_bar_name].current_value <= 0:
        status_bars[status_bar_name].current_value = int(increase)
    else:
        status_bars[status_bar_name].current_value = int(increase + status_bars[status_bar_name].current_value)


def get_heat_fluctuation_code():
    """ Get fluctuation code """
    # Get the heat factor data to obtain the fluctuation code
    fluctuation_code = ""
    # Check the factor booleans
    for name in cs.heat_factor_names:
        # Get the complete boolean variable names
        complete_name = "init.game_state." + name
        # Add an "n" in front of the current factor character if False
        if not eval(complete_name):
            fluctuation_code += "n"
        # Get the current factor character
        fluctuation_code += name.lower()[0]
    return fluctuation_code


########################################################################################
# GAME LOOP UPDATING FUNCTIONS
########################################################################################

def update_status_bars():
    """ Update status bars value each frame """
    for status_bar_name in init.game_state.status_bars.keys():
        gradual_status_bar_fluctuation(status_bar_name)


def update_heat_fluctuation_factor(fluctuation_code):
    """ Update heat fluctuation factor based on location, day time, fire, weather """
    # Modify the Body Heat fluctuation factor if the environmental factors change
    if fluctuation_code != init.game_state.current_heat_factor_code:
        # Save the current environmental factor code
        init.game_state.current_heat_factor_code = fluctuation_code
        # If the status bar should stay stagnant, delete fluctuation factor
        if cs.heat_factor_fluctuation[fluctuation_code] == 0.0:
            init.game_state.status_bars["Body Heat"].remove_fluctuation_factor()
        else:
            # Time interval between two concurrent fluctuations with the factor value
            value = (cs.heat_factor_fluctuation[fluctuation_code] / 60) * (-1.0)
            # Modify the fluctuation factor
            init.game_state.status_bars["Body Heat"].add_fluctuation_factor(value, 1, init.game_state.game_time)