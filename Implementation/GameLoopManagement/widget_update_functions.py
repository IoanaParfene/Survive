from GameLoopManagement import text_update_functions as tuf
from Initialization import initialization as init
from Gameplay import game_play_functions as gpf
from Initialization import constants as cs
from Gameplay import file_functions as ff
from Screens import random_widgets as rw
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
            label = eval("sc.sm.get_screen(screen_type).ids." + status_bar_name.split(" ", 1)[-1].lower() + '_label_value')
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
    if (len(display_list) - 1) // 5 < cs.inventory_display_page:
        cs.inventory_display_page -= 1

    # Display the item for the current page and category in the selected slot
    for slot in range(1, 6):
        # If slot is occupied
        if slot + 5 * cs.inventory_display_page - 1 < len(display_list) and (
                slot + 5 * cs.inventory_display_page - 1) >= 0:
            # Enable the slot button
            eval("sc.sm.get_screen('inventory').ids.inv_slot_" + str(slot)).disabled = False
            # Update the slot item name
            eval("sc.sm.get_screen('inventory').ids.inv_item_" + str(slot)).text = \
                display_list[slot + 5 * cs.inventory_display_page - 1][1]["Name"]
            # Update the slot item quantity
            eval("sc.sm.get_screen('inventory').ids.inv_quantity_" + str(slot)).text = str(
                int(display_list[slot + 5 * cs.inventory_display_page - 1][1]["Quantity"])) + " remaining"
            # Update the slot item taken space
            eval("sc.sm.get_screen('inventory').ids.inv_space_" + str(slot)).text = "Space: " + str(
                int(display_list[slot + 5 * cs.inventory_display_page - 1][1]["InventorySpace"]))
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
    sc.sm.get_screen(screen_type).ids.inventory_capacity_label.text = str(
        int(init.game_state.inventory.current_capacity)) + "/" + str(init.game_state.inventory.max_capacity)


def update_craftable_widgets():
    """ Update the displayed item for the current page of the craft menu """

    # The name of the item
    item_name = ""
    counter = 0
    for key, value in cs.craftable_items.items():
        if cs.craftable_scroll_page == counter:
            item_name = key
        counter += 1

    if cs.craftable_scroll_page < len(cs.craftable_items):
        # Update the item name
        sc.sm.get_screen('crafting').ids.craft_name.text = cs.craftable_items[item_name]["Name"]
        # Update the item description
        sc.sm.get_screen('crafting').ids.craft_description.text = "     " + cs.craftable_items[item_name]["Description"]

        # Update the item required and owned materials labels
        needed_materials_text = ""
        owned_materials_text = ""
        enough_materials = True
        for material_name, material_quantity in cs.craftable_items[item_name]["Needed"]:
            needed_materials_text += str(material_quantity) + " " + cs.inventory_items[material_name]["Name"] + ", "
            owned_materials_text += str(int(init.game_state.inventory.items[material_name]["Quantity"])) + " " + cs.inventory_items[material_name]["Name"] + ", "
            if init.game_state.inventory.items[material_name]["Quantity"] < material_quantity:
                enough_materials = False
        needed_materials_text = needed_materials_text[:-2]
        owned_materials_text = owned_materials_text[:-2]
        sc.sm.get_screen('crafting').ids.craft_requirement_label.text = needed_materials_text
        sc.sm.get_screen('crafting').ids.craft_resource_label.text = owned_materials_text

        # Update the item crafting time label
        sc.sm.get_screen('crafting').ids.craft_duration.text = str(cs.craftable_items[item_name]["Duration"]) + " minutes"

        # Update item space label
        sc.sm.get_screen('crafting').ids.craft_space.text = "Space: " + str(int(init.game_state.inventory.items[item_name]["Weight"]))

        # Update the craft button based on resources available and on item limit and existence
        item_reached_limit = False
        if cs.craftable_items[item_name]["Limit"] is True:
            if init.game_state.inventory.items[item_name]["Quantity"] > 0:
                item_reached_limit = True
        if item_reached_limit is True or enough_materials is False:
            sc.sm.get_screen('crafting').ids.craft_button.disabled = True
        else:
            sc.sm.get_screen('crafting').ids.craft_button.disabled = False

        # Update the item limit label
        if item_reached_limit is True:
            sc.sm.get_screen('crafting').ids.limit_label.color = (2.0,0.2,0.2,1.0)
        else:
            sc.sm.get_screen('crafting').ids.limit_label.color = (2.0, 0.2, 0.2, 0.0)

        # Update the scroll buttons
        if cs.craftable_scroll_page == len(cs.craftable_items)-1:
            sc.sm.get_screen('crafting').ids.right_scroll.disabled = True
        else:
            sc.sm.get_screen('crafting').ids.right_scroll.disabled = False
        if cs.craftable_scroll_page == 0:
            sc.sm.get_screen('crafting').ids.left_scroll.disabled = True
        else:
            sc.sm.get_screen('crafting').ids.left_scroll.disabled = False


def update_hunting_screen():
    """ Update the possible hunting action """

    for action, info in cs.hunting_trap_actions.items():
        if init.game_state.current_location["Key"] in info["Locations"]:
            eval("sc.sm.get_screen('hunting').ids." + str(action)).opacity = 1
            eval("sc.sm.get_screen('hunting').ids." + str(action)).disabled = False
        else:
            eval("sc.sm.get_screen('hunting').ids." + str(action)).opacity = 0
            eval("sc.sm.get_screen('hunting').ids." + str(action)).disabled = True


def update_hunting_labels():
    """ Update the quantity item labels in the hunting screen """
    # Update trap labels
    for item, info in init.game_state.traps.items():
        eval("sc.sm.get_screen('hunting').ids." + str(item)).text = str(item) + ": " + str(int(info["Quantity"]))
    # Update bait label
    sc.sm.get_screen("hunting").ids.bait.text = "bait: " + str(int(init.game_state.inventory.items["bait"]["Quantity"]))
    # Update fishing rod label
    sc.sm.get_screen("hunting").ids.fishing_rod.text = "fishing rod: " + str(int(init.game_state.inventory.items["fishing_rod"]["Quantity"]))
    # Update spear label
    sc.sm.get_screen("hunting").ids.spear.text = "spear: " + str(int(init.game_state.inventory.items["wooden_spear"]["Quantity"]))


def update_next_travel_locations():
    """ Update next travel location buttons """
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


def check_for_car_shelter():
    """ Check if the player is sheltered by the car and show a label on-screen"""
    if init.game_state.current_location["Name"] == "Pike Lake":
        show_widget(True, "shelter", rw.car_label)
    else:
        show_widget(False, "shelter", rw.car_label)


def manage_fire_menu():
    """ Create all the fire buttons and labels"""

    if not init.game_state.fire_on:
        show_widget(False, "fire", rw.fire_time_remaining)
        show_widget(False, "fire", rw.add_wood_button)
        show_widget(False, "fire", rw.add_hardwood_button)
        show_widget(False, "fire", rw.add_tinder_button)
        show_widget(False, "fire", rw.boil_water_button)
        show_widget(False, "fire", rw.cook_meat_button)
        show_widget(False, "fire", rw.smoke_meat_button)
        # Check if the player has any tinder
        if init.game_state.inventory.items["tinder"]["Quantity"] == 0:
            show_widget(True, "fire", rw.fire_tinder_label)
            show_widget(False, "fire", rw.fire_tools_label)
            show_widget(False, "fire", rw.start_fire_button)
        else:
            show_widget(False, "fire", rw.fire_tinder_label)
            for item_code in ["matches"]:
                if init.game_state.inventory.items[item_code]["Quantity"] == 0:
                    show_widget(True, "fire", rw.fire_tools_label)
                else:
                    show_widget(False, "fire", rw.fire_tools_label)
                    show_widget(True, "fire", rw.start_fire_button)
    else:
        show_widget(False, "fire", rw.fire_tinder_label)
        show_widget(False, "fire", rw.fire_tools_label)
        show_widget(False, "fire", rw.start_fire_button)

        # Update the remaining fire time widget
        rw.fire_time_remaining.text = tuf.get_remaining_fire_time_text()
        show_widget(True, "fire", rw.fire_time_remaining)
        if init.game_state.inventory.items["tinder"]["Quantity"] > 0:
            rw.add_tinder_button.disabled = False
        else:
            rw.add_tinder_button.disabled = True
        if init.game_state.inventory.items["wood"]["Quantity"] > 0:
            rw.add_wood_button.disabled = False
        else:
            rw.add_wood_button.disabled = True
        if init.game_state.inventory.items["hardwood"]["Quantity"] > 0:
            rw.add_hardwood_button.disabled = False
        else:
            rw.add_hardwood_button.disabled = True
        if init.game_state.inventory.items["water_bottle_unsafe"]["Quantity"] > 0:
            rw.boil_water_button.disabled = False
        else:
            rw.boil_water_button.disabled = True
        if init.game_state.inventory.items["raw_meat"]["Quantity"] > 0:
            rw.cook_meat_button.disabled = False
        else:
            rw.cook_meat_button.disabled = True
        if init.game_state.inventory.items["raw_meat"]["Quantity"] > 0:
            rw.smoke_meat_button.disabled = False
        else:
            rw.smoke_meat_button.disabled = True

        show_widget(True, "fire", rw.add_tinder_button)
        show_widget(True, "fire", rw.add_wood_button)
        show_widget(True, "fire", rw.add_hardwood_button)
        show_widget(True, "fire", rw.boil_water_button)
        show_widget(True, "fire", rw.cook_meat_button)
        show_widget(True, "fire", rw.smoke_meat_button)


def manage_rain_catcher():
    """ Check if the rain catcher exists """
    # If the rain catcher hasn't been built yet
    if not init.game_state.rain_catcher_exists:
        show_widget(False, "shelter", rw.rain_catcher_label)
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
        show_widget(True, "shelter", rw.rain_catcher_label)


def manage_water_collecting():
    """ Collect dirty or clean water """
    if init.game_state.rain_water_uses > 0 or init.game_state.current_location["Key"] in cs.water_locations:
        sc.sm.get_screen("game").ids.water_collecting.disabled = False
    else:
        sc.sm.get_screen("game").ids.water_collecting.disabled = True


def update_trap_notifications(screen_name):
    """ Display the pray caught on the screen in the last hour """
    # Passed game_hours
    game_hours = init.game_state.game_time // 60
    # If a new hour has passed
    if game_hours > init.game_state.last_trap_hour:
        # Update traps
        gpf.update_traps()
        # Reset the trap checking hour
        init.game_state.last_trap_hour = game_hours
        # Display the caught pray
        for pray_type in init.game_state.last_hour_trapped_animals:
            sc.sm.get_screen(screen_name).show_popup("I caught a " + pray_type.lower() + ".")
