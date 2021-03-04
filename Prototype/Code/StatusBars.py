import pygame

class StatusBar:
    """ Any of the Calorie, Condition, Body Heat and Hydration bars"""
    def __init__(self, name, max_value, init_value):
        self.name = name
        self.max_value = max_value
        self.current_value = init_value
        self.decay = []

    def add_decay_factor(self, damage, duration, game_time):
        """ Add a decay factor for current status bar """
        """ Set 'damage' taken each interval of 'duration' seconds and when 'last_decay' happened """
        last_decay = game_time // duration
        self.decay.append([damage, duration, last_decay])

    def gradual_decay(self, game_time):
        """ Apply damage factors of current bar for each of their time intervals """
        for item in self.decay:
            # Decay supposed that happened based on passed game time
            decay_counter = game_time // item[1]
            if abs(decay_counter-item[2]) > 0:
                self.current_value -= item[0]
                # Last decay that happened based on passed game time
                item[2] = decay_counter

    def immediate_decay(self, damage):
        """ Take immediate decay based on damage of a certain action"""
        self.current_value -= damage

    def __str__(self):
        """ For console printing purposes """
        return self.name + ": " + str(self.current_value) + "/" + str(self.max_value)


