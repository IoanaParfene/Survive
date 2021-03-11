import Prototype.Code.Display as Display
import Prototype.Code.Config as Config
import pygame


def update_status_bars(game_state):
    for status_bar in game_state.status_bars.values():
        status_bar[0].gradual_decay(game_state)


def get_current_scene(game_state):
    for key in game_state.game_scenes.keys():
        if game_state.game_scenes[key]:
            return key


def current_game_loop(game_state, buttons, actions):
    current_scene = game_state.current_scene
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Action of a certain button was clicked
            for key in Config.game_buttons[current_scene]:
                buttons[key].on_click(event, game_state)
            for key in Config.game_actions[current_scene]:
                actions[key].on_click(event, game_state)


def render_menu_scene(game_state, buttons, actions):
    # Update game time
    game_state.game_time = game_state.get_game_time()

    # Display game screen each frame
    Display.display_game(game_state, buttons, actions)

    # Backend updates
    update_status_bars(game_state)

    # For interaction
    current_game_loop(game_state, buttons, actions)


def game_over(game_state, buttons):
    font = pygame.font.SysFont('Comic Sans MS', 40)
    pygame.draw.rect(game_state.screen, (0, 0, 0), (0, 0, 1200, 600))
    if game_state.game_over == "Won":
        game_state.screen.blit(font.render("Congratulations, you survived!", True, (255, 255, 255)), (300, 200))
    else:
        game_state.screen.blit(font.render("You didn't make it!", True, (255, 255, 255)), (300, 200))
    game_state.screen.blit(
        font.render("Days in the wilderness: " + str(game_state.current_game_day), True, (255, 255, 255)), (300, 300))

