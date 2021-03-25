import Survive.variable_initialization as var_init
import Survive.status_bars as sb
import random
import time
import copy
import Survive.initialization as init

class GameState:
    def __init__(self, status_bars):
        #self.screen = var_init.screen
        self.game_speed = copy.copy(var_init.game_speed)
        self.start_time = copy.copy(var_init.start_time)
        self.game_time = copy.copy(var_init.game_time)
        self.paused_time = copy.copy(var_init.paused_time)
        self.start_paused_time = copy.copy(var_init.start_paused_time)
        self.skipped_time = copy.copy(var_init.skipped_time)
        self.current_day_period = copy.copy(var_init.current_day_period)
        self.current_game_day = copy.copy(var_init.current_game_day)
        self.game_over = copy.copy(var_init.game_over)
        self.save_time = 0
        self.time_is_stopped = copy.copy(var_init.time_is_stopped)
        self.running = copy.copy(var_init.running)

        self.status_bars = status_bars

        self.current_location = var_init.current_location
        self.game_locations = var_init.game_locations
        self.game_location_info = var_init.game_location_info
        self.remaining_miles = var_init.remaining_miles
        self.travel_next = [random.choice(list(self.game_locations.keys())[1:]),
                            random.choice(list(self.game_locations.keys())[1:])]

        ##self.current_scene = var_init.current_scene
        ##self.game_scenes = var_init.game_scenes
        #self.background = var_init.background
        ##self.current_location = var_init.current_location
        ##self.game_locations = var_init.game_locations
        ##self.game_location_info = var_init.game_location_info
        ##self.inventory = inventory
        ##self.current_weather = var_init.current_weather
        ##self.remaining_miles = var_init.remaining_miles
        ##self.travel_next = [random.choice(list(self.game_locations.keys())[1:]),
                            ##random.choice(list(self.game_locations.keys())[1:])]
        ##self.fire = var_init.fire

    def update_paused_time(self):
        last_paused_time = time.time() - self.start_paused_time
        self.start_paused_time = 0
        self.time_is_stopped = False
        self.paused_time += last_paused_time
        print(last_paused_time)

    def change_scene(self, new_scene):
        for key in self.game_scenes.keys():
            if key == "Pause" and self.game_scenes[key] is True:
                self.update_paused_time()
            if key == new_scene:
                self.game_scenes[key] = True
            else:
                self.game_scenes[key] = False
        self.current_scene = new_scene

    def get_game_time(self):
        """ Calculate in game passed minutes """
        return self.skipped_time + ((time.time() - self.start_time - self.paused_time) / 3) * self.game_speed

    def action_effect(self, action):
        pass

    def travel(self, travel_path):
        location = self.travel_next[travel_path]
        name, miles, duration = self.game_location_info[location].values()
        #self.action_loading_message("Walking for " + str(duration) + " hours towards nearby " + name, (50, 250))
        self.skipped_time += duration * 60
        if self.remaining_miles-miles <= 0:
            self.game_over = "Won"
        else:
            self.remaining_miles -= miles
        self.current_location = location
        self.travel_next = [random.choice(list(self.game_locations.keys())[1:]),
                            random.choice(list(self.game_locations.keys())[1:])]
        print(name, miles, duration)

status_bars = init.initialize_game()
game_state = GameState(status_bars)