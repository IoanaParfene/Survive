
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

    def __str__(self):
        """ For console printing purposes """
        return self.name + ": " + str(max(0, min(self.max_value, self.current_value))) + "/" + str(self.max_value)
