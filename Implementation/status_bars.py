import time


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


def initialize_status_bars():
    """ Initialize the status bar objects into a list"""
    # StatusBar object + screen display location
    new_status_bars = {"Calories": StatusBar("Calories", 3000, 1200),
                       "Condition": StatusBar("Condition", 100, 100),
                       "Body Heat": StatusBar("Body Heat", 100, 100),
                       "Hydration": StatusBar("Hydration", 100, 100)}
    # Almost identical with the actual game_time
    game_time = time.time()
    # Add initial calorie and hydration decay
    new_status_bars["Hydration"].add_decay_factor(1, 25, game_time)
    new_status_bars["Calories"].add_decay_factor(1, 6, game_time)
    new_status_bars["Body Heat"].add_decay_factor(1, 30, game_time)
    new_status_bars["Condition"].add_decay_factor(1, 50, game_time)
    return new_status_bars


# Initialize status_bars
status_bars = initialize_status_bars()
