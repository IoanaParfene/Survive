import pygame
import time


class Action:
    def __init__(self, action_type, display_text, icon_pos, size, *varg):
        """ Initialize action attributes """
        # Prefix of action standard images
        self.action_type = action_type
        # Display text of action standard images
        self.display_text = display_text
        # Permanent action image loading, transforming and rectangle
        self.icon_pos = icon_pos
        # The button width and height
        self.size = size
        # Special extra custom variables for different actions
        self.varg = list(varg)

    def on_click(self, event, game_state, *varg):
        """ On-click action function"""
        if event.button == 1:
            if pygame.Rect(self.icon_pos[0], self.icon_pos[1], self.size[0], self.size[1]).collidepoint(event.pos):
                function_name = str(self.action_type).lower() + '_action'
                eval(function_name)(game_state)


def getwater_action(game_state):
    print("Get Water")


def explore_action(game_state):
    print("Explore")


def sleep1_action(game_state):
    print("Sleep 1h")
    game_state.action_loading_message("Resting 1 hour", (400, 250))
    game_state.skipped_time += 60
    game_state.action_effect("sleep1")
    if min(100, game_state.status_bars["Condition"][0].current_value + 3) == 100:
        game_state.status_bars["Condition"][0].current_value = 100
    else:
        game_state.status_bars["Condition"][0].current_value += 4
    print(game_state.skipped_time)


def sleep4_action(game_state):
    print("Sleep 4h")
    game_state.skipped_time += 4*60
    game_state.action_effect("sleep4")
    game_state.action_loading_message("Resting 4 hours", (400, 250))
    if min(100, game_state.status_bars["Condition"][0].current_value + 3) == 100:
        game_state.status_bars["Condition"][0].current_value = 100
    else:
        game_state.status_bars["Condition"][0].current_value += 16
    print(game_state.skipped_time)


def travel1_action(game_state):
    print("Travel1")
    game_state.travel(0)


def travel2_action(game_state):
    print("Travel2")
    game_state.travel(1)


def item0_action(game_state):
    print("Item0")
    item_0 = game_state.inventory.items["water_bottle"]
    if item_0["Quantity"] > 0:
        item_0["Quantity"] -= 1
        print(game_state.status_bars["Hydration"][0])
        game_state.status_bars["Hydration"][0].immediate_increase(item_0["Hydration"])
        game_state.inventory.items["empty_bottle"]["Quantity"] += 1


def item1_action(game_state):
    print("Item1")
    item_1 = game_state.inventory.items["energy_bar"]
    if item_1["Quantity"] > 0:
        item_1["Quantity"] -= 1
        print(item_1["Calories"])
        game_state.status_bars["Calories"][0].immediate_increase(item_1["Calories"])


def makefire_action(game_state):
    print("MakeFire")
    wood = game_state.inventory.items["wood"]
    if wood["Quantity"] > 0:
        wood["Quantity"] -= 1
        game_state.fire[1] += 1
        if not game_state.fire[0]:
            game_state.fire[0] = True
            game_state.fire[2] = game_state.game_time()
        game_state.status_bars["Body Heat"][0].current_value += 4
