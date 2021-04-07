import variable_initialization as var_init
import status_bars as sb
import inventory as inv
import random
import copy


class GameState:
    def __init__(self, status_bars, inventory):
        # Time related variables
        self.game_speed = copy.copy(var_init.game_speed)
        # Start time of a new game_play
        self.start_time = copy.copy(var_init.start_time)
        # Current game minutes
        self.game_time = copy.copy(var_init.game_time)
        # Real time spent in the start/paused/game_over menus
        self.paused_time = copy.copy(var_init.paused_time)
        # Start pausing time
        self.start_paused_time = copy.copy(var_init.start_paused_time)
        # Game minutes that were skipped during actions
        self.skipped_time = copy.copy(var_init.skipped_time)
        # Daylight or Darkness
        self.current_day_period = copy.copy(var_init.current_day_period)
        # In-game day
        self.current_game_day = copy.copy(var_init.current_game_day)
        # No, Won or Lost
        self.game_over = copy.copy(var_init.game_over)
        # Real time spent outside of the game
        self.save_time = copy.copy(var_init.save_time)
        # True or False, True when saving the game
        self.time_is_stopped = copy.copy(var_init.time_is_stopped)
        # If the game is running
        self.running = copy.copy(var_init.running)
        # The four status bars in the game as an object list
        self.status_bars = status_bars
        # Name in string of the current location
        self.current_location = var_init.current_location
        # A list of all the game location names
        self.game_locations = var_init.game_locations
        # A dictionary of game locations and their attributes
        self.game_location_info = var_init.game_location_info
        # Remaining miles to safety
        self.remaining_miles = var_init.remaining_miles
        # Options for the next travel
        self.travel_next = [random.choice(list(self.game_locations.keys())[1:]),
                            random.choice(list(self.game_locations.keys())[1:])]
        # Inventory
        self.inventory = inventory

game_state = GameState(sb.status_bars, inv.inventory)