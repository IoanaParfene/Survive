from PythonFiles.BackendFunctions import backend_miscellaneous as bbm
from PythonFiles.BackendFunctions import backend_os as bbo
from PythonFiles import initialization as init
from PythonFiles.Screens import screens as sc


########################################################################################
# FUNCTIONS USED DURING GAME LOOP UPDATES
########################################################################################

def show_widget(create_widget, screen_type, widget_name):
    """ Show dynamically added widgets """
    if create_widget:
        try:
            sc.sm.get_screen(screen_type).add_widget(widget_name)
        except:
            pass
    else:
        try:
            sc.sm.get_screen(screen_type).remove_widget(widget_name)
        except:
            pass


def activate_widget(enable_widget, screen_type, widget_name):
    """ Disable or enable dynamically added widgets """
    if enable_widget:
        try:
            eval("sc.sm.get_screen("+screen_type+").ids."+widget_name).disabled = False
        except:
            pass
    else:
        try:
            eval("sc.sm.get_screen("+screen_type+").ids."+widget_name).disabled = True
        except:
            pass


########################################################################################
# GAME LOOP UPDATING FUNCTIONS
########################################################################################

def update_load_button():
    """ Enable or disable load button """
    sc.sm.get_screen("start").ids.load_button.disabled = not bbo.save_file_exists()


def update_game_over_screen(screen_type):
    """ Check if the game over screen needs to be deployed"""
    # If the game is over
    if bbm.check_game_over_condition():
        # Delete an existing save file given the perma-death nature of the game
        bbo.delete_save_file()
        # Update the game over screen background
        if init.game_state.game_over != "Lost":
            sc.sm.get_screen("over").ids.background_over.this_source = bbo.get_path(
                "../../GraphicFiles/won_background.png")
        if init.game_state.game_over != "Won":
            sc.sm.get_screen("over").ids.background_over.this_source = bbo.get_path(
                "../../GraphicFiles/lost_background.png")
        # Change the screen
        sc.sm.get_screen(screen_type).change_window("over")
