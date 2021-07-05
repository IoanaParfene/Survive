from PythonFiles.FrontendFunctions import frontend_miscellaneous as ffm
from PythonFiles.Widgets import widget_constants as wwco
from PythonFiles import initialization as init
from PythonFiles.Screens import screens as sc


########################################################################################
# FUNCTIONS USED DURING GAME LOOP UPDATES
########################################################################################

def fire_label_description_text(resource):
    """ Return text with specific fire resource quantity """
    text = resource + ": " + str(int(init.game_state.inventory.items[resource]["Quantity"]))
    return text


def get_remaining_fire_time_text():
    """ Text for the fire time label"""
    # Remaining fire time in minutes
    remaining_fire_time = int(
        init.game_state.fire_duration - (init.game_state.game_time - init.game_state.start_fire_time))
    if remaining_fire_time > 59:
        fire_text = "FIRE: " + str(remaining_fire_time//60) + "h " + str(remaining_fire_time%60)
    else:
        fire_text = "FIRE: " + str(remaining_fire_time)
    return fire_text


########################################################################################
# GAME LOOP UPDATING FUNCTIONS
########################################################################################

def update_fire_labels(screen_type):
    """ Update remaining tinder, wood and hardwood in the FIRE screen """
    # Update tinder label
    sc.sm.get_screen(screen_type).ids.tinder_label.text = fire_label_description_text("tinder")
    # Update wood label
    sc.sm.get_screen(screen_type).ids.wood_label.text = fire_label_description_text("wood")
    # Update hardwood label
    sc.sm.get_screen(screen_type).ids.hardwood_label.text = fire_label_description_text("hardwood")


def update_fire_menu():
    """ Update the fire buttons"""

    # Enable and disable the fire screen buttons based on met requirements
    if not init.game_state.fire_on:
        ffm.show_widget(False, "fire", wwco.fire_time_remaining)
        ffm.show_widget(False, "fire", wwco.add_wood_button)
        ffm.show_widget(False, "fire", wwco.add_hardwood_button)
        ffm.show_widget(False, "fire", wwco.add_tinder_button)
        ffm.show_widget(False, "fire", wwco.boil_water_button)
        ffm.show_widget(False, "fire", wwco.cook_meat_button)
        ffm.show_widget(False, "fire", wwco.smoke_meat_button)

        # Check if the player doesn't have tinder, disable the fire starting buttons
        if init.game_state.inventory.items["tinder"]["Quantity"] == 0:
            wwco.matches_start_fire_button.disabled = True
            wwco.plow_start_fire_button.disabled = True
            wwco.drill_start_fire_button.disabled = True
        else:
            # I the player has tinder, make buttons appear
            for item_code in ["matches", "bow_drill", "fire_plow"]:
                if init.game_state.inventory.items[item_code]["Quantity"] != 0:

                    eval("wwco." + item_code.split("_", 1)[-1] + "_start_fire_button").disabled = False
                else:
                    eval("wwco." + item_code.split("_", 1)[-1] + "_start_fire_button").disabled = True

        for item_code in ["matches", "bow_drill", "fire_plow"]:
            ffm.show_widget(True, "fire", eval("wwco." + item_code.split("_", 1)[-1] + "_start_fire_button"))
    else:

        ffm.show_widget(False, "fire", wwco.fire_tinder_label)
        ffm.show_widget(False, "fire", wwco.fire_tools_label)
        ffm.show_widget(False, "fire", wwco.matches_start_fire_button)
        ffm.show_widget(False, "fire", wwco.plow_start_fire_button)
        ffm.show_widget(False, "fire", wwco.drill_start_fire_button)

        # Update the remaining fire time widget
        wwco.fire_time_remaining.text = get_remaining_fire_time_text()
        ffm.show_widget(True, "fire", wwco.fire_time_remaining)
        if init.game_state.inventory.items["tinder"]["Quantity"] > 0:
            wwco.add_tinder_button.disabled = False
        else:
            wwco.add_tinder_button.disabled = True
        if init.game_state.inventory.items["wood"]["Quantity"] > 0:
            wwco.add_wood_button.disabled = False
        else:
            wwco.add_wood_button.disabled = True
        if init.game_state.inventory.items["hardwood"]["Quantity"] > 0:
            wwco.add_hardwood_button.disabled = False
        else:
            wwco.add_hardwood_button.disabled = True
        if init.game_state.inventory.items["water_bottle_unsafe"]["Quantity"] > 0:
            wwco.boil_water_button.disabled = False
        else:
            wwco.boil_water_button.disabled = True
        if init.game_state.inventory.items["raw_meat"]["Quantity"] > 0:
            wwco.cook_meat_button.disabled = False
        else:
            wwco.cook_meat_button.disabled = True
        if init.game_state.inventory.items["raw_meat"]["Quantity"] > 0:
            wwco.smoke_meat_button.disabled = False
        else:
            wwco.smoke_meat_button.disabled = True

        ffm.show_widget(True, "fire", wwco.add_tinder_button)
        ffm.show_widget(True, "fire", wwco.add_wood_button)
        ffm.show_widget(True, "fire", wwco.add_hardwood_button)
        ffm.show_widget(True, "fire", wwco.boil_water_button)
        ffm.show_widget(True, "fire", wwco.cook_meat_button)
        ffm.show_widget(True, "fire", wwco.smoke_meat_button)
