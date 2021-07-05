from PythonFiles import constants as cs, initialization as init
from PythonFiles.Screens import screens as sc


########################################################################################
# FUNCTIONS USED DURING GAME LOOP UPDATES
########################################################################################

def get_inventory_display_items():
    """ Return the first 5 item names to display for the current inventory page """
    display_dictionary = dict()
    for key, value in init.game_state.inventory.items.items():
        if cs.inventory_display_category in init.game_state.inventory.items[key]["Categories"]:
            if init.game_state.inventory.items[key]["Quantity"] > 0:
                display_dictionary[key] = init.game_state.inventory.items[key]
    # Sort item objects alphabetically
    display_dictionary = dict(sorted(display_dictionary.items(), key=lambda x: x[0].lower()))
    # Get the item names in a list
    display_list = []
    for key, value in display_dictionary.items():
        display_list.append((key, display_dictionary[key]))
    return display_list


########################################################################################
# GAME LOOP UPDATING FUNCTIONS
########################################################################################

def update_inventory_widgets():
    """ Update the displayed items for the current page of the inventory """

    # The names of the first 5 items
    display_list = get_inventory_display_items()

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
            # Update the item picture
            eval("sc.sm.get_screen('inventory').ids.inv_pic_" + str(slot)).opacity = 1
            eval("sc.sm.get_screen('inventory').ids.inv_pic_" + str(slot)).source = "GraphicFiles/Icons/" + \
                        display_list[slot + 5 * cs.inventory_display_page - 1][0] +".png"

        else:
            # Disable the slot button
            eval("sc.sm.get_screen('inventory').ids.inv_slot_" + str(slot)).disabled = True
            # Update the slot item name
            eval("sc.sm.get_screen('inventory').ids.inv_item_" + str(slot)).text = ""
            # Update the slot item quantity
            eval("sc.sm.get_screen('inventory').ids.inv_quantity_" + str(slot)).text = ""
            # Update the slot item taken space
            eval("sc.sm.get_screen('inventory').ids.inv_space_" + str(slot)).text = ""
            # Update the item picture
            eval("sc.sm.get_screen('inventory').ids.inv_pic_" + str(slot)).opacity = 0


def update_inventory_capacity_widgets(screen_type):
    """ Update and display inventory capacity types """
    # Update the occupied inventory space bar
    sc.sm.get_screen(screen_type).ids.my_inventory_capacity_bar.value = int(init.game_state.inventory.current_capacity)
    # Update the maximum capacity of the inventory bar
    sc.sm.get_screen(screen_type).ids.my_inventory_capacity_bar.max = init.game_state.inventory.max_capacity
    # Update the text for the inventory capacity
    sc.sm.get_screen(screen_type).ids.inventory_capacity_label.text = str(
        int(init.game_state.inventory.current_capacity)) + "/" + str(init.game_state.inventory.max_capacity)
