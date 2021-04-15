from Initialization import constants as cs
import copy


class GameState:
    def __init__(self, status_bars, inventory, first_location, first_travel_locations):
        # Time related variables
        self.game_speed = copy.copy(cs.game_speed)
        # Start time of a new game_play
        self.start_time = copy.copy(cs.start_time)
        # Current game minutes
        self.game_time = copy.copy(cs.game_time)
        # Real time spent in the start/paused/game_over menus
        self.paused_time = copy.copy(cs.paused_time)
        # Start pausing time
        self.start_paused_time = copy.copy(cs.start_paused_time)
        # Game minutes that were skipped during actions
        self.skipped_time = copy.copy(cs.skipped_time)
        # Daylight or Darkness
        self.current_day_period = copy.copy(cs.current_day_period)
        # In-game day
        self.current_game_day = copy.copy(cs.current_game_day)
        # No, Won or Lost
        self.game_over = copy.copy(cs.game_over)
        # Real time spent outside of the game
        self.save_time = copy.copy(cs.save_time)
        # True or False, True when saving the game
        self.time_is_stopped = copy.copy(cs.time_is_stopped)
        # If the game is running
        self.running = copy.copy(cs.running)
        # The four status bars in the game as an object list
        self.status_bars = status_bars
        # Options for the next travel
        self.travel_next = first_travel_locations
        # Name in string of the current location
        self.current_location = first_location
        # A list of all the game location names
        self.game_locations = cs.game_locations
        # A dictionary of game locations and their attributes
        self.game_location_info = cs.game_location_info
        # Remaining miles to safety
        self.remaining_miles = cs.remaining_miles
        # Inventory
        self.inventory = inventory



