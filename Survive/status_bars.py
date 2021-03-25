
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


    def gradual_decay(self, game_state):
        """ Apply damage factors of current bar for each of their time intervals """
        for item in self.decay:
            # Decay supposed that happened based on passed game time
            decay_counter = game_state.game_time // item[1]
            if abs(decay_counter - item[2]) > 0:
                if int(self.current_value - abs(decay_counter - item[2]) * item[0]) < (-self.max_value/10):
                    print(self.name)
                    print(int(self.current_value - abs(decay_counter - item[2]) * item[0]))
                    print(-self.max_value/10)
                    print("Bob2")
                    #game_state.game_over = "Lost"
                else:
                    print(int(self.current_value - abs(decay_counter - item[2]) * item[0]))
                    print(-self.max_value / 10)
                    self.current_value = int(self.current_value - abs(decay_counter - item[2]) * item[0])
                    print(self.name, self.current_value)
                    if self.current_value < (-self.max_value / 10):
                        game_state.game_over = "Lost"
                # Last decay that happened based on passed game time
                item[2] = decay_counter

    def immediate_decay(self, damage, game_time):
        """ Take immediate decay based on damage of a certain action"""
        if self.current_value - damage < (-self.max_value / 20):
            print("Bob")
            game_time.game_over = "Lost"
        else:
            self.current_value -= damage

    def immediate_increase(self, increase):
        if min(self.max_value, self.current_value + increase) == self.max_value:
            self.current_value = self.max_value
        else:
            self.current_value += increase

    def __str__(self):
        """ For console printing purposes """
        return self.name + ": " + str(max(0,min(self.max_value,self.current_value))) + "/" + str(self.max_value)
        #return self.name + ": " + str(self.current_value) + "/" + str(self.max_value)
