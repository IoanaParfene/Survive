import pygame


class Button:
    def __init__(self, button_type, display_text, icon_pos, size, *varg):
        """ Initialize button attributes """
        # Prefix of button standard images
        self.button_type = button_type
        # Display_text of button standard images
        self.display_text = display_text
        # Permanent button image loading, transforming and rectangle
        self.icon_pos = icon_pos
        # The button width and height
        self.size = size
        # Special extra custom variables for different buttons
        self.varg = list(varg)

    def on_click(self, event, game_state):
        """ On-click button action function"""
        if event.button == 1:
            if pygame.Rect(self.icon_pos[0], self.icon_pos[1], self.size[0], self.size[1]).collidepoint(event.pos):
                function_name = str(self.button_type).lower() + '_button_action'
                eval(function_name)(game_state)


def shelter_button_action(game_state):
    print("Shelter")
    game_state.change_scene("Shelter")


def fire_button_action(game_state):
    print("Fire")
    game_state.change_scene("Fire")


def crafting_button_action(game_state):
    print("Crafting")
    game_state.change_scene("Crafting")


def inventory_button_action(game_state):
    print("Inventory")
    game_state.change_scene("Inventory")


def trapshunt_button_action(game_state):
    print("Traps/Hunt")
    game_state.change_scene("Traps/Hunt")


def travel_button_action(game_state):
    print("Travel")
    game_state.change_scene("Travel")


def pause_button_action(game_state):
    print("Pause")
    import time
    game_state.start_paused_time = time.time()
    game_state.change_scene("Pause")


def back_button_action(game_state):
    print("Back")
    game_state.change_scene("Main")
