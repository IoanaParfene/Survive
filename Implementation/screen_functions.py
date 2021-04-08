import variable_initialization as var_init
import game_state as gs
import screens as sc


def display_inventory():
    """ """
    display_dictionary = dict()
    for key, value in gs.game_state.inventory.items.items():
        if var_init.inventory_display_category in gs.game_state.inventory.items[key]["Categories"]:
            if gs.game_state.inventory.items[key]["Quantity"] > 0:
                display_dictionary[key] = gs.game_state.inventory.items[key]

    display_dictionary = dict(sorted(display_dictionary.items(), key=lambda x: x[0].lower()))

    display_list = []
    for key, value in display_dictionary.items():
        display_list.append((key, display_dictionary[key]))

    if (len(display_list)-1) // 5 < var_init.inventory_display_page:
        var_init.inventory_display_page -=1
    for item in range(1,6):
        #print(len(display_list), item + 5 * var_init.inventory_display_page - 1)
        if item + 5 * var_init.inventory_display_page - 1 < len(display_list):
            #print(len(display_list))
            if item == 1:
                sc.sm.get_screen("inventory").ids.inv_item_1.text = display_list[item + 5 * var_init.inventory_display_page - 1][1]["Name"]
                sc.sm.get_screen("inventory").ids.inv_quantity_1.text = str(int(display_list[item + 5 * var_init.inventory_display_page - 1][1]["Quantity"])) + " remaining"
                sc.sm.get_screen("inventory").ids.inv_weight_1.text = "Weight: " + str(int(display_list[item + 5 * var_init.inventory_display_page - 1][1]["InventorySpace"]))
            elif item == 2:
                sc.sm.get_screen("inventory").ids.inv_item_2.text = display_list[item + 5 * var_init.inventory_display_page - 1][1]["Name"]
                sc.sm.get_screen("inventory").ids.inv_quantity_2.text = str(int(display_list[item + 5 * var_init.inventory_display_page - 1][1]["Quantity"])) + " remaining"
                sc.sm.get_screen("inventory").ids.inv_weight_2.text = "Weight: " + str(int(display_list[item + 5 * var_init.inventory_display_page - 1][1]["InventorySpace"]))
            elif item == 3:
                sc.sm.get_screen("inventory").ids.inv_item_3.text = display_list[item + 5 * var_init.inventory_display_page - 1][1]["Name"]
                sc.sm.get_screen("inventory").ids.inv_quantity_3.text = str(int(display_list[item + 5 * var_init.inventory_display_page - 1][1]["Quantity"])) + " remaining"
                sc.sm.get_screen("inventory").ids.inv_weight_3.text = "Weight: " + str(int(display_list[item + 5 * var_init.inventory_display_page - 1][1]["InventorySpace"]))
            elif item == 4:
                sc.sm.get_screen("inventory").ids.inv_item_4.text = display_list[item + 5 * var_init.inventory_display_page - 1][1]["Name"]
                sc.sm.get_screen("inventory").ids.inv_quantity_4.text = str(int(display_list[item + 5 * var_init.inventory_display_page - 1][1]["Quantity"])) + " remaining"
                sc.sm.get_screen("inventory").ids.inv_weight_4.text = "Weight: " + str(int(display_list[item + 5 * var_init.inventory_display_page - 1][1]["InventorySpace"]))
            elif item == 5:
                sc.sm.get_screen("inventory").ids.inv_item_5.text = display_list[item + 5 * var_init.inventory_display_page - 1][1]["Name"]
                sc.sm.get_screen("inventory").ids.inv_quantity_5.text = str(int(display_list[item + 5 * var_init.inventory_display_page - 1][1]["Quantity"])) + " remaining"
                sc.sm.get_screen("inventory").ids.inv_weight_5.text = "Weight: " + str(int(display_list[item + 5 * var_init.inventory_display_page - 1][1]["InventorySpace"]))
        else:
            if item == 1:
                sc.sm.get_screen("inventory").ids.inv_item_1.text = ""
                sc.sm.get_screen("inventory").ids.inv_quantity_1.text = ""
                sc.sm.get_screen("inventory").ids.inv_weight_1.text = ""
            elif item == 2:
                sc.sm.get_screen("inventory").ids.inv_item_2.text = ""
                sc.sm.get_screen("inventory").ids.inv_quantity_2.text = ""
                sc.sm.get_screen("inventory").ids.inv_weight_2.text = ""
            elif item == 3:
                sc.sm.get_screen("inventory").ids.inv_item_3.text = ""
                sc.sm.get_screen("inventory").ids.inv_quantity_3.text = ""
                sc.sm.get_screen("inventory").ids.inv_weight_3.text = ""
            elif item == 4:
                sc.sm.get_screen("inventory").ids.inv_item_4.text = ""
                sc.sm.get_screen("inventory").ids.inv_quantity_4.text = ""
                sc.sm.get_screen("inventory").ids.inv_weight_4.text = ""
            elif item == 5:
                sc.sm.get_screen("inventory").ids.inv_item_5.text = ""
                sc.sm.get_screen("inventory").ids.inv_quantity_5.text = ""
                sc.sm.get_screen("inventory").ids.inv_weight_5.text = ""


