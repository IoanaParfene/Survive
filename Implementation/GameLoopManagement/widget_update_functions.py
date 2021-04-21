from GameLoopManagement import text_update_functions as tuf
from Initialization import initialization as init
from Gameplay import game_play_functions as gpf
from Initialization import constants as cs
from Gameplay import file_functions as ff
from Screens import screens as sc


def enable_load_button():
    """ Enable or disable load button """
    sc.sm.get_screen("start").ids.load_button.disabled = not ff.save_file_exists()


def check_for_game_over_screen(screen_type):
    """ Check if the game over screen needs to be deployed"""
    # If the game is over
    if gpf.check_game_over_condition():
        # Delete an existing save file given the perma-death nature of the game
        ff.delete_save_file()
        # Update the game over screen background
        if init.game_state.game_over != "Lost":
            sc.sm.get_screen("over").ids.background_over.this_source = ff.get_path("../Images/won_background.png")
        if init.game_state.game_over != "Won":
            sc.sm.get_screen("over").ids.background_over.this_source = ff.get_path("../Images/lost_background.png")
        # Change the screen
        sc.sm.get_screen(screen_type).change_window("over")


def update_progress_labels(screen_type):
    """ Update the location, day time and remaining miles labels"""
    # Update time label
    sc.sm.get_screen(screen_type).ids.time_label.text = tuf.game_time_description_update()
    # Update location label
    sc.sm.get_screen(screen_type).ids.location_label.text = tuf.get_progress_description_update()


def update_status_bar_labels(screen_type):
    """ Update status bar and label values """
    for status_bar_name in init.game_state.status_bars.keys():
        # Hydration, Condition, Body Heat
        if status_bar_name != "Calories":
            bar_value = tuf.status_bar_value_update(status_bar_name)
            bar = eval("sc.sm.get_screen(screen_type).ids.my_" + status_bar_name.split(" ", 1)[-1].lower() + '_bar')
            bar.value = int(bar_value)
            label = eval(
                "sc.sm.get_screen(screen_type).ids." + status_bar_name.split(" ", 1)[-1].lower() + '_label_value')
            label.text = str(int(bar_value))
    # Calories status bar update
    calories = tuf.status_bar_value_update("Calories")
    sc.sm.get_screen(screen_type).ids.calories_label.text = "CALORIES: " + str(int(calories)) + "/3000"


def update_background_widget(screen_type):
    """ Change background after the time of day """
    sc.sm.get_screen(screen_type).ids.background.change_background()


def update_rain_widget(screen_type):
    """ Change rain animation position """
    sc.sm.get_screen(screen_type).rain.show_rain()


def update_inventory_widgets():
    """ Update the displayed items for the current page of the inventory """

    # The names of the first 5 items
    display_list = tuf.get_inventory_display_items()

    # Calculate display page for current inventory category
    if (len(display_list)-1) // 5 < cs.inventory_display_page:
        cs.inventory_display_page -= 1

    # Display the item for the current page and category in the selected slot
    for slot in range(1,6):
        # If slot is occupied
        if slot + 5 * cs.inventory_display_page - 1 < len(display_list) and (slot + 5 * cs.inventory_display_page -1) >= 0:
            # Enable the slot button
            eval("sc.sm.get_screen('inventory').ids.inv_slot_" + str(slot)).disabled = False
            # Update the slot item name
            eval("sc.sm.get_screen('inventory').ids.inv_item_" + str(slot)).text = display_list[slot + 5 * cs.inventory_display_page - 1][1]["Name"]
            # Update the slot item quantity
            eval("sc.sm.get_screen('inventory').ids.inv_quantity_" + str(slot)).text = str(int(display_list[slot + 5 * cs.inventory_display_page - 1][1]["Quantity"])) + " remaining"
            # Update the slot item taken space
            eval("sc.sm.get_screen('inventory').ids.inv_space_" + str(slot)).text = "Space: " + str(int(display_list[slot + 5 * cs.inventory_display_page - 1][1]["InventorySpace"]))
        else:
            # Disable the slot button
            eval("sc.sm.get_screen('inventory').ids.inv_slot_" + str(slot)).disabled = True
            # Update the slot item name
            eval("sc.sm.get_screen('inventory').ids.inv_item_" + str(slot)).text = ""
            # Update the slot item quantity
            eval("sc.sm.get_screen('inventory').ids.inv_quantity_" + str(slot)).text = ""
            # Update the slot item taken space
            eval("sc.sm.get_screen('inventory').ids.inv_space_" + str(slot)).text = ""


def update_inventory_capacity_widgets(screen_type):
    """ Update and display inventory capacity types """
    # Update the occupied inventory space bar
    sc.sm.get_screen(screen_type).ids.my_inventory_capacity_bar.value = int(init.game_state.inventory.current_capacity)
    # Update the maximum capacity of the inventory bar
    sc.sm.get_screen(screen_type).ids.my_inventory_capacity_bar.max = init.game_state.inventory.max_capacity
    # Update the text for the inventory capacity
    sc.sm.get_screen(screen_type).ids.inventory_capacity_label.text = str(int(init.game_state.inventory.current_capacity)) \
                                                                      + "/" + str(init.game_state.inventory.max_capacity)


def update_next_travel_locations():
    """ Update next travel location buttons"""
    sc.sm.get_screen("travel").ids.travel_1.text = tuf.get_next_travel_location_text(0)
    sc.sm.get_screen("travel").ids.travel_2.text = tuf.get_next_travel_location_text(1)


def update_fire_labels(screen_type):
    """ Update remaining tinder, wood and hardwood in the FIRE screen """
    # Update tinder label
    sc.sm.get_screen(screen_type).ids.tinder_label.text = tuf.fire_label_description_update("tinder")
    # Update wood label
    sc.sm.get_screen(screen_type).ids.wood_label.text = tuf.fire_label_description_update("wood")
    # Update hardwood label
    sc.sm.get_screen(screen_type).ids.hardwood_label.text = tuf.fire_label_description_update("hardwood")

