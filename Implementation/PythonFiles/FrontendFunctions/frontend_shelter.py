from PythonFiles.FrontendFunctions import frontend_miscellaneous as fm
from PythonFiles import constants as cs, initialization as init
from PythonFiles.Widgets import widget_constants as wwco
from PythonFiles.Screens import screens as sc


########################################################################################
# FUNCTIONS USED DURING GAME LOOP UPDATES
########################################################################################

def update_shelter_labels():
    """ Update shelter and raincatcher labels """
    # Update shelter label
    if init.game_state.current_location["Name"] == "Pike Lake":
        sc.sm.get_screen("shelter").ids.shelter_label.text = "shelter: yes"
    else:
        sc.sm.get_screen("shelter").ids.shelter_label.text = "shelter: no"
    # Update raincatcher
    if init.game_state.rain_catcher_exists:
        sc.sm.get_screen("shelter").ids.raincatcher_label.text = "raincatcher: yes"
    else:
        sc.sm.get_screen("shelter").ids.raincatcher_label.text = "raincatcher: no"


def update_rain_catcher():
    """ Check if the rain catcher exists """
    # If the rain catcher hasn't been built yet
    if not init.game_state.rain_catcher_exists:
        sc.sm.get_screen("shelter").ids.rain_catcher_button.opacity = 1
        # If the player has a trash bag
        if init.game_state.inventory.items["trash_bag"]["Quantity"] == 1:
            sc.sm.get_screen("shelter").ids.rain_catcher_button.disabled = False
        else:
            sc.sm.get_screen("shelter").ids.rain_catcher_button.disabled = True
    else:
        if init.game_state.raining_now:
            init.game_state.rain_water_uses = 3
        sc.sm.get_screen("shelter").ids.rain_catcher_button.opacity = 0
        sc.sm.get_screen("shelter").ids.rain_catcher_button.disabled = True


def update_water_collecting():
    """ Collect dirty or clean water """
    if init.game_state.rain_water_uses > 0 or init.game_state.current_location["Key"] in cs.water_locations:
        sc.sm.get_screen("game").ids.water_collecting.disabled = False
    else:
        sc.sm.get_screen("game").ids.water_collecting.disabled = True
