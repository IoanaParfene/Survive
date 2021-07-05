from PythonFiles import constants as cs, initialization as init
from PythonFiles.Screens import screens as sc


########################################################################################
# GAME LOOP UPDATING FUNCTIONS
########################################################################################

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

        # Update item picture
        sc.sm.get_screen('crafting').ids.craft_pic.source = "GraphicFiles/Icons/" + item_name + ".png"

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