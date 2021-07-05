from PythonFiles.BackendFunctions import backend_miscellaneous as bbm
from PythonFiles.BackendFunctions import backend_inventory as bbi
from PythonFiles import constants as cs, initialization as init
from PythonFiles.BackendFunctions import backend_stats as bbs
from PythonFiles.Widgets import widget_customs as wwc
import random

class HuntingScreen(wwc.BaseGameplayScreen):
    """ Screen for the hunting menu """

    # Used to enable/disable trap buttons
    enough_fish_trap_supplies = False
    enough_bird_trap_supplies = False
    enough_deadfall_supplies = False

    def show_info(self):
        self.show_popup(cs.hunting_screen_info)

    def set_trap(self, trap_type):
        """ Set the type of trap """

        # Prepare the text to share on the screen
        needed_materials_text = "I need "
        owned_materials_text = ".\nI currently have "

        # Check if there are enough materials to set the trap
        enough_materials = True
        for material, quantity in cs.traps[trap_type]["Needed"]:
            material_owned_quantity = init.game_state.inventory.items[material]["Quantity"]
            if material_owned_quantity < quantity:
                enough_materials = False
            needed_materials_text += str(int(quantity)) + " " + init.game_state.inventory.items[material]["Name"] + ", "
            owned_materials_text += str(int(material_owned_quantity)) + " " + init.game_state.inventory.items[material]["Name"] + ", "

        # Check if there is enough visibility for the foraging actions
        too_dark, has_flashlight, daylight_text = self.check_night_action()

        if too_dark and not has_flashlight:
            self.show_popup(daylight_text)
        else:
            if not enough_materials:
                # Show the needed materials on-screen
                not_enough_materials_text = daylight_text+ needed_materials_text[:-2] + owned_materials_text[:-2] + "."
                self.show_popup(not_enough_materials_text)
                # Disable action screen
                exec("self.enough_" + trap_type + "_supplies = False")
            else:
                # Add the lost second for the loading screen
                init.game_state.paused_time += 1
                # Update the status bars during the special action
                bbm.update_bars_during_action(1, [])
                # Allow action screen
                exec("self.enough_" + trap_type + "_supplies = True")

                # Place the trap
                for material, quantity in cs.traps[trap_type]["Needed"]:
                    init.game_state.inventory.items[material]["Quantity"] -= quantity
                init.game_state.traps[trap_type]["Quantity"] += 1

                self.show_popup(daylight_text + "I placed the trap. It took me one hour.")

    def dismantle_traps(self):
        """ Remove th traps before leaving """
        traps_exist = False
        for trap_type, info in init.game_state.traps.items():
            if info["Quantity"] > 0:
                traps_exist = True
            for material, quantity in info["Needed"]:
                init.game_state.inventory.items[material]["Quantity"] += quantity * info["Quantity"]
            info["Quantity"] = 0

        # Add the lost second for the loading screen
        init.game_state.paused_time += 1
        # Update the status bars during the special action
        bbm.update_bars_during_action(1, [])

        if traps_exist:
            self.show_popup("I removed all the traps. It took me an hour.")
        else:
            self.show_popup("I haven't placed any traps.")

    def catch_fish(self, true_weight):
        """ Fish or Spear Fish """
        # Check if there is enough visibility for the action
        too_dark, has_flashlight, text = self.check_night_action()

        if has_flashlight or not too_dark:
            # Randomize if the fish was caught or not
            caught_fish = random.choices([True, False], weights=(true_weight, 100-true_weight), k=1)[0]

            if caught_fish:
                init.game_state.inventory.items["dead_fish"]["Quantity"] += 1
                bbi.add_item_spoil_rate("dead_fish", 1)
                text += "\nI caught a fish."
            else:
                text += "\nI couldn't catch any fish."

        # Add the lost second for the loading screen
        init.game_state.paused_time += 1
        # Update the status bars during the special action
        bbm.update_bars_during_action(1, [])

        # Display the text in a popup
        self.show_popup(text)
