from Initialization import initialization as init
from GameLoopManagement import widget_update_functions as wuf
from Gameplay import game_play_functions as gpf
from Screens import screens as sc


def game_loop():
    """ Game loop frame by frame """
    if sc.sm.current == "start":
        # Enable game load button if a save file is available
        wuf.enable_load_button()
        pass

    if sc.sm.current == "game":
        # Activate game time when entering gameplay menu
        gpf.activate_game_time()
        pass

    if sc.sm.current == "pause":
        # Pause game time when entering pause menu
        gpf.pause_game_time()
        pass

    for screen_type in ["game", "shelter", "fire", "crafting", "inventory", "hunting", "travel"]:
        # Update time once per frame
        if sc.sm.current == screen_type:
            # Manage game over
            wuf.check_for_game_over_screen(screen_type)
            # Update game time once per frame
            gpf.update_game_time()
            # Update the inventory once per frame
            gpf.update_inventory()
            # Update status_bars
            gpf.update_status_bars()
        # Update time and location labels
        wuf.update_progress_labels(screen_type)
        # Update status bars and labels
        wuf.update_status_bar_labels(screen_type)
        # Change background
        wuf.change_background(screen_type)

    if sc.sm.current == "start":
        pass

    elif sc.sm.current == "game":
        pass

    elif sc.sm.current == "pause":
        pass

    elif sc.sm.current == "over":
        pass

    elif sc.sm.current == "shelter":
        pass

    elif sc.sm.current == "fire":
        wuf.update_fire_labels("fire")

    elif sc.sm.current == "crafting":
        pass

    elif sc.sm.current == "inventory":
        # Update inventory overview screen
        wuf.update_inventory_widgets()
        # Update inventory capacity widgets
        wuf.update_inventory_capacity_widgets("inventory")

    elif sc.sm.current == "hunting":
        pass

    elif sc.sm.current == "travel":
        # Update the next travel location widgets
        wuf.update_next_travel_locations()


