from Initialization import initialization as init
import time


def get_game_time():
    """ Calculate in game passed minutes """
    return init.game_state.skipped_time + ((time.time() - init.game_state.start_time - init.game_state.paused_time) / 3) * init.game_state.game_speed


def update_game_time():
    """ Update game time once per frame in gameplay screens """
    init.game_state.game_time = get_game_time()


def update_paused_time():
    """ Add time spent in the pause menu to the paused_time variable """
    last_paused_time = time.time() - init.game_state.start_paused_time
    init.game_state.start_paused_time = 0
    init.game_state.time_is_stopped = False
    init.game_state.paused_time += last_paused_time


def activate_game_time():
    """ Activate and update game time if it is paused """
    if init.game_state.time_is_stopped:
        update_paused_time()


def pause_game_time():
    """ Pause game time if it is running """
    if not init.game_state.time_is_stopped:
        init.game_state.time_is_stopped = True
        init.game_state.start_paused_time = time.time()


def gradual_status_bar_decay(status_bar_name):
    """ Apply damage factors of current bar for each of their time intervals """
    status_bars = init.game_state.status_bars
    for item in status_bars[status_bar_name].decay:
        # Decay supposed to happen based on passed game time
        decay_counter = init.game_state.game_time // item[1]
        if abs(decay_counter - item[2]) > 0:
            if not int(status_bars[status_bar_name].current_value - abs(decay_counter - item[2]) * item[0]) < (-status_bars[status_bar_name].max_value / 10):
                status_bars[status_bar_name].current_value = int(status_bars[status_bar_name].current_value - abs(decay_counter - item[2]) * item[0])
                if (-status_bars[status_bar_name].max_value / 7) < status_bars[status_bar_name].current_value < (-status_bars[status_bar_name].max_value / 15):
                    if status_bar_name != "Calories":
                        init.game_state.game_over = "Lost"
            # Last decay that happened based on passed game time
            item[2] = decay_counter


def update_status_bars():
    """ Update status bars value each frame """
    for status_bar_name in init.game_state.status_bars.keys():
        gradual_status_bar_decay(status_bar_name)


def immediate_status_bar_decay(status_bar_name, damage):
    """ Take immediate decay based on damage of a certain action"""
    status_bars = init.game_state.status_bars
    if status_bars[status_bar_name].current_value - damage < (-status_bars[status_bar_name].max_value / 20):
        if status_bar_name != "Calories":
            init.game_state.game_over = "Lost"
    else:
        status_bars[status_bar_name].current_value -= damage


def immediate_status_bar_increase(status_bar_name, increase):
    """ Immediate increase in value based on certain action """
    status_bars = init.game_state.status_bars
    if min(status_bars[status_bar_name].max_value, status_bars[status_bar_name].current_value + increase) == status_bars[status_bar_name].max_value:
        status_bars[status_bar_name].current_value = status_bars[status_bar_name].max_value
    elif status_bars[status_bar_name].current_value <= 0:
        status_bars[status_bar_name].current_value = int(increase)
    else:
        status_bars[status_bar_name].current_value = int(increase + status_bars[status_bar_name].current_value)


def update_inventory():
    """ Update Inventory capacity and item weights """
    total_weight = 0
    for key, value in init.game_state.inventory.items.items():
        init.game_state.inventory.items[key]["InventorySpace"] = float(int(init.game_state.inventory.items[key]["Quantity"] * init.game_state.inventory.items[key]["Weight"]))
        total_weight += init.game_state.inventory.items[key]["InventorySpace"]
    init.game_state.inventory.current_capacity = total_weight


def check_game_over_condition():
    """ Check to see if the game is over"""
    if init.game_state.game_time // 60 > 1 or init.game_state.current_game_day > 1:
        # If game is lost or won
        if init.game_state.game_over != "No":
            return True
    return False
