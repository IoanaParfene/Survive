from Initialization import initialization as init
from Gameplay import game_play_functions as gpf
from Initialization import constants as cs
from Screens import GUI_classes as gui


class HuntingScreen(gui.BaseGameplayScreen):
    """ Screen for the hunting menu """

    def show_info(self):
        self.show_popup(cs.hunting_screen_info)

    def set_trap(self, trap_type):
        """ Set the type of trap """
        needed_materials_text = "I need "
        owned_materials_text = ".\nI currently have "

        enough_materials = True
        for material, quantity in cs.traps[trap_type]["Needed"]:
            material_owned_quantity = init.game_state.inventory.items[material]["Quantity"]
            if material_owned_quantity < quantity:
                enough_materials = False
            needed_materials_text += str(int(quantity)) + " " + init.game_state.inventory.items[material]["Name"] + ", "
            owned_materials_text += str(int(material_owned_quantity)) + " " + init.game_state.inventory.items[material]["Name"] + ", "

        if not enough_materials:
            # Show the needed materials on-screen
            not_enough_materials_text = needed_materials_text[:-2] + owned_materials_text[:-2] + "."
            self.show_popup(not_enough_materials_text)
        else:
            # Add the lost second for the loading screen
            init.game_state.paused_time += 1
            # Update the status bars during the special action
            gpf.update_bars_during_action(1, [])

            # Place the trap
            for material, quantity in cs.traps[trap_type]["Needed"]:
                init.game_state.inventory.items[material]["Quantity"] -= quantity
            init.game_state.traps[trap_type]["Quantity"] += 1
            self.show_popup("I placed the trap. It took me one hour.")

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
        gpf.update_bars_during_action(1, [])

        if traps_exist:
            self.show_popup("I removed all the traps. It took me an hour.")
        else:
            self.show_popup("I haven't placed any traps.")
