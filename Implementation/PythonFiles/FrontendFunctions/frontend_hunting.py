from PythonFiles.BackendFunctions import backend_hunting as bbh
from PythonFiles import constants as cs, initialization as init
from PythonFiles.Screens import screens as sc


########################################################################################
# GAME LOOP UPDATING FUNCTIONS
########################################################################################

def update_hunting_screen():
    """ Update the possible hunting action """

    for action, info in cs.hunting_trap_actions.items():
        if init.game_state.current_location["Key"] in info["Locations"]:
            eval("sc.sm.get_screen('hunting').ids." + str(action)).opacity = 1
            eval("sc.sm.get_screen('hunting').ids." + str(action)).disabled = False
        else:
            eval("sc.sm.get_screen('hunting').ids." + str(action)).opacity = 0
            eval("sc.sm.get_screen('hunting').ids." + str(action)).disabled = True

    # Update the trap dismantling
    eval("sc.sm.get_screen('hunting').ids.dismantle_traps").disabled = True
    for item, info in init.game_state.traps.items():
        if info["Quantity"] > 0:
            eval("sc.sm.get_screen('hunting').ids.dismantle_traps").disabled = False

    # Update fishing
    if init.game_state.inventory.items["fishing_rod"]["Quantity"] > 0:
        sc.sm.get_screen('hunting').ids.fish.disabled = False
    else:
        sc.sm.get_screen('hunting').ids.fish.disabled = True

    # Update spearing fish
    if init.game_state.inventory.items["wooden_spear"]["Quantity"] > 0:
        sc.sm.get_screen('hunting').ids.spear_fish.disabled = False
    else:
        sc.sm.get_screen('hunting').ids.spear_fish.disabled = True


def update_hunting_labels():
    """ Update the quantity item labels in the hunting screen """
    # Update trap labels
    for item, info in init.game_state.traps.items():
        eval("sc.sm.get_screen('hunting').ids." + str(item)).text = str(item).replace("_"," ") + ": " + str(int(info["Quantity"]))
    # Update bait label
    sc.sm.get_screen("hunting").ids.bait.text = "bait: " + str(int(init.game_state.inventory.items["bait"]["Quantity"]))
    # Update fishing rod label
    sc.sm.get_screen("hunting").ids.fishing_rod.text = "fishing rod: " + str(int(init.game_state.inventory.items["fishing_rod"]["Quantity"]))
    # Update spear label
    sc.sm.get_screen("hunting").ids.spear.text = "spear: " + str(int(init.game_state.inventory.items["wooden_spear"]["Quantity"]))


def update_trap_notifications(screen_name):
    """ Display the pray caught on the screen in the last hour """
    # Passed game_hours
    game_hours = init.game_state.game_time // 60
    # If a new hour has passed
    if game_hours > init.game_state.last_trap_hour:
        print(init.game_state.last_trap_hour)
        # Update traps
        bbh.update_traps()
        # Reset the trap checking hour
        init.game_state.last_trap_hour = game_hours
        # Display the caught pray
        for pray_type in init.game_state.last_hour_trapped_animals:
            sc.sm.get_screen(screen_name).show_popup("I caught a " + pray_type.lower() + ".")
