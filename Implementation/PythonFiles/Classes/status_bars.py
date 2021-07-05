
class StatusBar:
    """ Any of the Calorie, Condition, Body Heat and Hydration bars"""

    def __init__(self, name, max_value, init_value):
        # The display name of the status bar
        self.name = name
        # The maximum value of the bar
        self.max_value = max_value
        # The current value of the bar
        self.current_value = init_value
        # The increase/decrease of the bar over one game minute
        self.fluctuation = None

    def add_fluctuation_factor(self, value, duration, game_time):
        """ Add a fluctuation factor for current status bar """
        """ Set 'value' taken/added for each interval of 1 game minute """
        # Last time(in-game minute) the fluctuation happened
        last_fluctuation = game_time // duration
        # Add the fluctuation factor with the value, the interval and the last time it happened
        self.fluctuation = [value, duration, last_fluctuation]

    def change_fluctuation_factor(self, value, duration, game_time):
        """ Change the fluctuation factor for the current status bar """
        self.add_fluctuation_factor(value, duration, game_time)

    def remove_fluctuation_factor(self):
        """ Remove the fluctuation factor for current status bar """
        self.fluctuation = None

    def __str__(self):
        """ For console printing purposes """
        return self.name + ": " + str(max(0, min(self.max_value, self.current_value))) + "/" + str(self.max_value)
