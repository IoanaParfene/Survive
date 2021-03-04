from Initialization import *
import time

def display_game_time(screen, game_time):
    """ Display player time on screen """
    # Get remaining hours in time of day
    game_hours = game_time/60
    game_hours_today = game_hours%24
    if(game_hours_today<12):
        day_period = "DAYLIGHT"
    else:
        day_period = "DARKNESS"
    time_information = str(int(12-game_hours_today%12)+1) + " HOURS OF " + day_period + " REMAINING"

    # Display remaining hours in time of day in upper left corner
    font = pygame.font.SysFont('Comic Sans MS', 25)
    pygame.draw.rect(screen, (0, 0, 0), (10, 20, 490, 40))
    screen.blit(font.render(time_information, True, (255, 255, 255)), (20,20))


def display_status_bars(screen, status_bars, game_time):
    """ Display status bar each frame """
    # text display font
    font = pygame.font.SysFont('Comic Sans MS', 25)
    for status_bar in status_bars.values():
        # print a background rectangle
        pygame.draw.rect(screen, (0,0,0), (status_bar[1][0]-10, status_bar[1][1], 260, 40))
        # blit the status bar text
        screen.blit(font.render(str(status_bar[0]), True, (255, 255, 255)), status_bar[1])


def display_buttons(screen, buttons):
    """ Show buttons on screen """
    # text display font
    font = pygame.font.SysFont('Comic Sans MS', 40)
    for button in buttons.values():
        # print a background rectangle
        pygame.draw.rect(screen, (0, 0, 0), (button.icon_pos[0] - 10, button.icon_pos[1], button.size[0], button.size[1]))
        # blit the status bar text
        screen.blit(font.render(button.button_type, True, (255, 255, 255)), button.icon_pos)


def display_game(screen, background, game_time, status_bars, buttons):
    screen.blit(background, (-200, 0))
    display_game_time(screen, game_time)
    display_status_bars(screen, status_bars, game_time)
    display_buttons(screen, buttons)