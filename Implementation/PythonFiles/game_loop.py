from PythonFiles.FrontendFunctions import frontend_miscellaneous as ffm, frontend_crafting as ffc, frontend_fire as fff
from PythonFiles.FrontendFunctions import frontend_environment as ffe, frontend_inventory as ffi, frontend_stats as ffs
from PythonFiles.FrontendFunctions import frontend_shelter as ffsh, frontend_hunting as ffh, frontend_travel as fft
from PythonFiles.BackendFunctions import backend_miscellaneous as bbm, backend_inventory as bbi, backend_stats as bbs
from PythonFiles.BackendFunctions import backend_time as bbt, backend_fire as bbf
from PythonFiles import constants as cs, initialization as init
from PythonFiles.Screens import screens as sc


def game_loop():
    """ Game loop frame by frame """

    if sc.sm.current == "start":
        # Enable game load button if a save file is available
        ffm.update_load_button()

    if sc.sm.current == "game":
        # Activate game time when entering gameplay menu
        bbt.activate_game_time()

    if sc.sm.current == "pause":
        # Pause game time when entering pause menu
        bbt.pause_game_time()

    for screen_type in ["game", "shelter", "fire", "crafting", "inventory", "hunting", "travel"]:
        # Update time once per frame
        if sc.sm.current == screen_type:
            # Manage game over
            ffm.update_game_over_screen(screen_type)
            # Update game time once per frame
            bbt.update_game_time()
            # Update rain
            bbm.update_rain()
            # Update fire
            bbf.update_fire()
            # Update the inventory once per frame
            bbi.update_inventory()
            # Update the items that have spoiled
            bbi.update_spoiled_items()
            # Update fluctuation factor based on location, day time, fire, weather
            bbs.update_heat_fluctuation_factor(bbs.get_heat_fluctuation_code())
            # Update status_bars
            bbs.update_status_bars()
            # Manage activated traps
            ffh.update_trap_notifications(screen_type)
        # Update time and location labels
        ffe.update_progress_labels(screen_type)
        # Update status bars and labels
        ffs.update_status_bar_labels(screen_type)
        # Change background
        ffe.update_background_widget(screen_type)
        # Show or hide rain animation
        ffe.update_rain_widget(screen_type)
        # Manage the fire menu widgets
        fff.update_fire_menu()
        # Manage the rain catcher
        ffsh.update_rain_catcher()
        # Manage water collecting
        ffsh.update_water_collecting()
        # Update hunting screen action buttons
        ffh.update_hunting_screen()

    if sc.sm.current == "shelter":
        # Check if there is shelter from the car and show a message on-screen
        ffsh.update_shelter_labels()

    elif sc.sm.current == "fire":
        # Show the resources for the fire
        fff.update_fire_labels("fire")

    elif sc.sm.current == "crafting":
        # Update crafting overview screen
        ffc.update_craftable_widgets()
        pass

    elif sc.sm.current == "inventory":
        # Update inventory overview screen
        ffi.update_inventory_widgets()
        # Update inventory capacity widgets
        ffi.update_inventory_capacity_widgets("inventory")

    elif sc.sm.current == "hunting":
        # Show the hunting/trap items
        ffh.update_hunting_labels()

    elif sc.sm.current == "travel":
        # Update the next travel location widgets
        fft.update_next_travel_locations()


