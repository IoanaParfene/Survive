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
            # Update rain
            gpf.update_rain()
            # Update fire
            gpf.update_fire()
            # Update the inventory once per frame
            gpf.update_inventory()
            # Update the items that have spoiled
            gpf.update_spoiled_items()
            # Update fluctuation factor based on location, day time, fire, weather
            gpf.update_heat_fluctuation_factor(gpf.get_fluctuation_code())
            # Update status_bars
            gpf.update_status_bars()
            # Manage activated traps
            wuf.update_trap_notifications(screen_type)
        # Update time and location labels
        wuf.update_progress_labels(screen_type)
        # Update status bars and labels
        wuf.update_status_bar_labels(screen_type)
        # Change background
        wuf.update_background_widget(screen_type)
        # Show or hide rain animation
        wuf.update_rain_widget(screen_type)
        # Manage the fire menu widgets
        wuf.manage_fire_menu()
        # Manage the rain catcher
        wuf.manage_rain_catcher()
        # Manage water collecting
        wuf.manage_water_collecting()
        # Update hunting screen action buttons
        wuf.update_hunting_screen()

    if sc.sm.current == "start":
        pass

    elif sc.sm.current == "game":
        pass

    elif sc.sm.current == "pause":
        pass

    elif sc.sm.current == "over":
        pass

    elif sc.sm.current == "shelter":
        # Check if there is shelter from the car and show a message on-screen
        wuf.check_for_car_shelter()

    elif sc.sm.current == "fire":
        # Show the resources for the fire
        wuf.update_fire_labels("fire")

    elif sc.sm.current == "crafting":
        # Update crafting overview screen
        wuf.update_craftable_widgets()
        pass

    elif sc.sm.current == "inventory":
        # Update inventory overview screen
        wuf.update_inventory_widgets()
        # Update inventory capacity widgets
        wuf.update_inventory_capacity_widgets("inventory")

    elif sc.sm.current == "hunting":
        # Show the hunting/trap items
        wuf.update_hunting_labels()

    elif sc.sm.current == "travel":
        # Update the next travel location widgets
        wuf.update_next_travel_locations()


