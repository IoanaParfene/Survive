from PythonFiles import initialization as init
from PythonFiles.Screens import screens as sc


########################################################################################
# FUNCTIONS USED DURING GAME LOOP UPDATES
########################################################################################

def status_bar_value_text(status_bar):
    """ Get the current selected status bar value """
    # Return the minimum, maximum or current value if in-between extremities
    new_status_bar_value = max(0, min(init.game_state.status_bars[status_bar].max_value,
                                      init.game_state.status_bars[status_bar].current_value))
    return new_status_bar_value


########################################################################################
# GAME LOOP UPDATING FUNCTIONS
########################################################################################

def update_status_bar_labels(screen_type):
    """ Update status bar and label values """
    for status_bar_name in init.game_state.status_bars.keys():
        # Hydration, Condition, Body Heat
        if status_bar_name != "Calories":
            bar_value = status_bar_value_text(status_bar_name)
            bar = eval("sc.sm.get_screen(screen_type).ids.my_" + status_bar_name.split(" ", 1)[-1].lower() + '_bar')
            bar.value = int(bar_value)
            label = eval("sc.sm.get_screen(screen_type).ids." + status_bar_name.split(" ", 1)[-1].lower() + '_label_value')
            label.text = str(int(bar_value))
    # Calories status bar update
    calories = status_bar_value_text("Calories")
    sc.sm.get_screen(screen_type).ids.calories_label.text = "CALORIES: " + str(int(calories)) + "/3000"
