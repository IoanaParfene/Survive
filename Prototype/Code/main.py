import Prototype.Code.Initialization as Initialization
import Prototype.Code.Gameplay as Gameplay
import Prototype.Code.Display as Display
import Prototype.Code.Config as Config
import Prototype.Code.GameState as GameState
import pygame
import time


def main():
    """ Initialize game elements and run main loop """

    # Start time
    Config.start_time = time.time()

    # Initialize game elements
    inventory, status_bars, buttons, actions = Initialization.initialize_game()

    # Initialize game state
    game_state = GameState.GameState(inventory, status_bars)

    # Run game loop by frame
    while game_state.running:
        if game_state.game_over != "No":
            Gameplay.game_over(game_state, buttons)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_state.running = False
        elif game_state.game_scenes["Pause"] is True:
            # Display game screen each frame
            Display.display_game(game_state, buttons, actions)

            # For interaction
            Gameplay.current_game_loop(game_state, buttons, actions)

        elif game_state.game_scenes["Shelter"] is True:
            # Display and create scene graphics and interactive elements
            Gameplay.render_menu_scene(game_state, buttons, actions)

        elif game_state.game_scenes["Fire"] is True:
            # Display and create scene graphics and interactive elements
            Gameplay.render_menu_scene(game_state, buttons, actions)
            message = "Wood: " + str(game_state.inventory.items["wood"]["Quantity"])
            Display.display_message(game_state, message, (400, 500), 40, (0,0,0))
            if game_state.fire[0]:
                print((game_state.game_time - game_state.fire[2])/60)
                if 0 <= (game_state.game_time - game_state.fire[2])/60 <= game_state.fire[1]:
                    message_2 = "Remaining hours of fire: " + str(game_state.fire[1]-int((game_state.game_time - game_state.fire[2])/60))
                    Display.display_message(game_state, message_2, (400, 100), 30, (0, 0, 0))
                else:
                    game_state.fire = Config.fire
        elif game_state.game_scenes["Crafting"] is True:
            # Display and create scene graphics and interactive elements
            Gameplay.render_menu_scene(game_state, buttons, actions)

        elif game_state.game_scenes["Inventory"] is True:
            # Display and create scene graphics and interactive elements
            Gameplay.render_menu_scene(game_state, buttons, actions)
            Display.display_inventory(game_state)

        elif game_state.game_scenes["Traps/Hunt"] is True:
            # Display and create scene graphics and interactive elements
            Gameplay.render_menu_scene(game_state, buttons, actions)

        elif game_state.game_scenes["Travel"] is True:
            # Display and create scene graphics and interactive elements
            Gameplay.render_menu_scene(game_state, buttons, actions)

        elif game_state.game_scenes["Main"] is True:
            # Display and create scene graphics and interactive elements
            print(game_state.get_game_time())
            Gameplay.render_menu_scene(game_state, buttons, actions)

        pygame.display.update()


#main()
