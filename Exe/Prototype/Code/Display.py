import Prototype.Code.Config as Config
import pygame


def display_game_time(game_state):
    """ Display player time on screen """
    # Get remaining hours in time of day
    game_hours = game_state.game_time / 60
    game_state.current_game_day = int(game_hours / 24 + 1)
    game_hours_today = game_hours % 24
    if game_hours_today < 12:
        game_state.current_day_period = "DAYLIGHT"
    else:
        game_state.current_day_period = "DARKNESS"
    time_information = str(int(12-game_hours_today % 12) + 1) + " HOURS OF " + game_state.current_day_period + " REMAINING"

    # Display remaining hours in time of day in upper left corner
    font = pygame.font.SysFont('Comic Sans MS', 25)
    pygame.draw.rect(game_state.screen, (0, 0, 0), (10, 20, 490, 40))
    game_state.screen.blit(font.render(time_information, True, (255, 255, 255)), (20,20))


def display_game_progress(game_state):
    """ Display location, day and miles left """
    # Get day
    game_progress = game_state.game_location_info[game_state.current_location]["Name"] + " | Day " + \
                    str(game_state.current_game_day) + " | " + \
                    str(game_state.remaining_miles) + " miles left"
    # Display remaining hours in time of day in upper left corner
    font = pygame.font.SysFont('Comic Sans MS', 20)
    pygame.draw.rect(game_state.screen, (0, 0, 0), (10, 65, 490, 40))
    game_state.screen.blit(font.render(game_progress, True, (255, 255, 255)), (20, 65))


def display_status_bars(game_state):
    """ Display status bar each frame """
    # text display font
    font = pygame.font.SysFont('Comic Sans MS', 25)
    for status_bar in game_state.status_bars.values():
        # print a background rectangle
        pygame.draw.rect(game_state.screen, (0, 0, 0), (status_bar[1][0]-10, status_bar[1][1], 260, 40))
        # blit the status bar text
        game_state.screen.blit(font.render(str(status_bar[0]), True, (255, 255, 255)), status_bar[1])


def display_buttons(game_state, buttons):
    """ Show buttons on screen """
    # text display font
    font = pygame.font.SysFont('Comic Sans MS', 38)
    for key in Config.game_buttons[game_state.current_scene]:
        # print a background rectangle
        pygame.draw.rect(game_state.screen, (0, 0, 0), (buttons[key].icon_pos[0] - 10, buttons[key].icon_pos[1], buttons[key].size[0], buttons[key].size[1]))
        # blit the status bar text
        game_state.screen.blit(font.render(buttons[key].display_text, True, (255, 255, 255)), buttons[key].icon_pos)


def display_actions(game_state, actions):
    """ Show actions on screen """
    # text display font
    font = pygame.font.SysFont('Comic Sans MS', 38)
    for key in Config.game_actions[game_state.current_scene]:
        # print a background rectangle
        pygame.draw.rect(game_state.screen, (255, 255, 255), (actions[key].icon_pos[0] - 10, actions[key].icon_pos[1], actions[key].size[0], actions[key].size[1]))
        # blit the status bar text
        if "Item" in key:
            font = pygame.font.SysFont('Comic Sans MS', 24)
            item_number = int(actions[key].display_text[4])
            if item_number == 0:
                text = "DRINK"
            else:
                text = "EAT"
            game_state.screen.blit(font.render(text, True, (0, 0, 0)), actions[key].icon_pos)
        elif "Travel" in key:
            travel_number = int(actions[key].display_text[6])
            name, miles, duration = game_state.game_location_info[game_state.travel_next[travel_number-1]].values()
            text = name + " | " + str(miles) + " miles | " + str(duration) + " hours"
            game_state.screen.blit(font.render(text, True, (0, 0, 0)), actions[key].icon_pos)
        else:
            game_state.screen.blit(font.render(actions[key].display_text, True, (0, 0, 0)), actions[key].icon_pos)


def display_game(game_state, buttons, actions):
    game_state.screen.blit(game_state.background, (-200, 0))
    display_game_time(game_state)
    display_game_progress(game_state)
    display_status_bars(game_state)
    display_buttons(game_state, buttons)
    display_actions(game_state, actions)


def display_inventory(game_state):
    height = 70
    increment_height = 60
    font = pygame.font.SysFont('Comic Sans MS', 24)
    for key, value in game_state.inventory.items.items():
        height += increment_height
        item_text = ""
        # print a background rectangle
        pygame.draw.rect(game_state.screen, (0, 20, 0), (330, height, 700, 45))
        # blit the status bar text
        for detail_key, detail_value in value.items():
            if detail_value is not None:
                item_text += detail_key + " : " + str(detail_value) + ", "
        item_text = item_text.split(":",1)[1].rsplit(",",1)[0]
        game_state.screen.blit(font.render(item_text, True, (255, 255, 255)), (330, height))


def display_message(game_state, message, location, font_size, color):
    font = pygame.font.SysFont('Comic Sans MS', font_size)
    game_state.screen.blit(font.render(message, True, color), location)
