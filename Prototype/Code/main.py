from Gameplay import *
import pygame
import time

# Initialize the game
pygame.init()

# Title and App Icon
pygame.display.set_caption("Survive")

# Create Window and Background
screen = pygame.display.set_mode((1200, 600))
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (1600, 1200))

# Font
pygame.font.init()

# Game status
paused = False

def get_game_time(skipped_time, start_time):
    """ Calculate in game passed minutes """
    return skipped_time + (time.time() - start_time) / 1 * 60


def main():
    """ Initialize game elements and run main loop """
    # Start time
    start_time = time.time()
    skipped_time = 0
    game_time = skipped_time + (time.time() - start_time) / 180 * 60  # minutes
    #global paused

    # Initialize game elements
    inventory, status_bars, buttons = initialize_game(screen, game_time)

    # Run game loop by frame
    running = True
    while running:
        if paused:

            # Display game screen each frame
            display_game(screen, background, game_time, status_bars, buttons)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Action if a certain button was clicked
                    buttons["Pause"].on_click(event)
        else:
            # Get game time
            game_time = get_game_time(skipped_time, start_time)

            # Display game screen each frame
            display_game(screen, background, game_time, status_bars, buttons)

            # Backend updates
            update_status_bars(status_bars, game_time)

            # For interaction
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Action if a certain button was clicked
                    for button in buttons.values():
                        button.on_click(event)

        """if int(time.time() - start_time) > current_time:
            current_time = int(time.time() - start_time)"""

        pygame.display.update()


main()
