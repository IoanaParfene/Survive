import variable_initialization as var_init
import status_bars as sb
import inventory as inv
import random
import copy


def randomize_location_info(location_key):
    """ Randomize Information about a travel location """
    locations_info = dict()
    locations_info["Key"] = location_key
    locations_info["Name"] = var_init.game_location_info[location_key]["Name"]
    locations_info["Miles"] = var_init.game_location_info[location_key]["Miles"]
    locations_info["Duration"] = random.randint(var_init.game_location_info[location_key]["Duration"],var_init.game_location_info[location_key]["Duration"]+2)
    locations_info["Water Source"] = var_init.game_location_info[location_key]["Water Source"]
    # Randomize a list of explorable items
    number_explorable_items = random.randint(var_init.game_location_info[location_key]["Explorables"][0]-1, var_init.game_location_info[location_key]["Explorables"][0]+2)
    choices = [item[0] for item in var_init.game_location_info[location_key]["Explorables"][1]]
    weights = (item[1] for item in var_init.game_location_info[location_key]["Explorables"][1])
    explorable_item_list = random.choices(choices, weights=weights, k=number_explorable_items)
    locations_info["Explorables"] = explorable_item_list
    return locations_info


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
        # Options for the next travel
        self.travel_next = [randomize_location_info(random.choice(list(var_init.game_locations.keys())[1:])),
                            randomize_location_info(random.choice(list(var_init.game_locations.keys())[1:]))]
        # Name in string of the current location
        self.current_location = randomize_location_info("pike_lake")
        # A list of all the game location names
        self.game_locations = var_init.game_locations
        # A dictionary of game locations and their attributes
        self.game_location_info = var_init.game_location_info
        # Remaining miles to safety
        self.remaining_miles = var_init.remaining_miles
        # Inventory
        self.inventory = inventory


game_state = GameState(sb.status_bars, inv.inventory)


