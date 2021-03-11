import Prototype.Code.Config as Config
import random
import pygame
import time

class GameState:
    def __init__(self, inventory, status_bars):
        self.screen = Config.screen
        self.game_speed = Config.game_speed
        self.start_time = Config.start_time
        self.game_time = Config.game_time
        self.paused_time = Config.paused_time
        self.start_paused_time = Config.start_paused_time
        self.skipped_time = Config.skipped_time
        self.running = Config.running
        self.current_scene = Config.current_scene
        self.game_scenes = Config.game_scenes
        self.background = Config.background
        self.current_location = Config.current_location
        self.game_locations = Config.game_locations
        self.game_location_info = Config.game_location_info
        self.inventory = inventory
        self.status_bars = status_bars
        self.current_day_period = Config.current_day_period
        self.current_weather = Config.current_weather
        self.current_game_day = Config.current_game_day
        self.remaining_miles = Config.remaining_miles
        self.travel_next = [random.choice(list(self.game_locations.keys())[1:]),
                            random.choice(list(self.game_locations.keys())[1:])]
        self.game_over = Config.game_over
        self.fire = Config.fire

    def update_paused_time(self):
        last_paused_time = time.time() - self.start_paused_time
        self.start_paused_time = 0
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
        self.action_loading_message("Walking for " + str(duration) + " hours towards nearby " + name, (50, 250))
        self.skipped_time += duration * 60
        if self.remaining_miles-miles <=0:
            self.game_over = "Won"
        else:
            self.remaining_miles -= miles
        self.current_location = location
        self.travel_next = [random.choice(list(self.game_locations.keys())[1:]),
                            random.choice(list(self.game_locations.keys())[1:])]
        self.change_scene("Main")
        print(name, miles, duration)


    def action_loading_message(self, message, writing_corner):
        font = pygame.font.SysFont('Comic Sans MS', 40)
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 1200, 600))
        self.screen.blit(font.render(message, True, (255, 255, 255)), writing_corner)
        pygame.display.update()
        time.sleep(2)
        self.paused_time += 2