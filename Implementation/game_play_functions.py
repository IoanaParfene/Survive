import variable_initialization as var_init
import game_state as gs
import time


def get_game_time():
    """ Calculate in game passed minutes """
    return gs.game_state.skipped_time + ((time.time() - gs.game_state.start_time - gs.game_state.paused_time) / 3) * gs.game_state.game_speed


def update_paused_time():
    """ Add time spent in the pause menu to the paused_time variable """
    last_paused_time = time.time() - gs.game_state.start_paused_time
    gs.game_state.start_paused_time = 0
    gs.game_state.time_is_stopped = False
    gs.game_state.paused_time += last_paused_time


def gradual_status_bar_decay(status_bar_name):
    """ Apply damage factors of current bar for each of their time intervals """
    status_bars = gs.game_state.status_bars
    for item in status_bars[status_bar_name].decay:
        # Decay supposed that happened based on passed game time
        decay_counter = gs.game_state.game_time // item[1]
        if abs(decay_counter - item[2]) > 0:
            if not int(status_bars[status_bar_name].current_value - abs(decay_counter - item[2]) * item[0]) < (-status_bars[status_bar_name].max_value / 10):
                status_bars[status_bar_name].current_value = int(status_bars[status_bar_name].current_value - abs(decay_counter - item[2]) * item[0])
                if (-status_bars[status_bar_name].max_value / 7) < status_bars[status_bar_name].current_value < (-status_bars[status_bar_name].max_value / 15):
                    gs.game_state.game_over = "Lost"
            # Last decay that happened based on passed game time
            item[2] = decay_counter


def update_status_bars():
    """ Update status bars value each frame """
    for status_bar_name in gs.game_state.status_bars.keys():
        gradual_status_bar_decay(status_bar_name)


def immediate_status_bar_decay(status_bar_name, damage):
    """ Take immediate decay based on damage of a certain action"""
    status_bars = gs.game_state.status_bars
    if status_bars[status_bar_name].current_value - damage < (-status_bars[status_bar_name].max_value / 20):
        gs.game_state.game_over = "Lost"
    else:
        status_bars[status_bar_name].current_value -= damage


def immediate_status_bar_increase(status_bar_name, increase):
    """ Immediate increase in value based on certain action """
    status_bars = gs.game_state.status_bars
    if min(status_bars[status_bar_name].max_value, status_bars[status_bar_name].current_value + increase) == status_bars[status_bar_name].max_value:
        status_bars[status_bar_name].current_value = status_bars[status_bar_name].max_value
    else:
        status_bars[status_bar_name].current_value = int(increase + status_bars[status_bar_name].current_value)


def update_inventory():
    """ Update Inventory capacity and item weights """
    total_weight = 0
    for key, value in gs.game_state.inventory.items.items():
        gs.game_state.inventory.items[key]["InventorySpace"] = float(int(gs.game_state.inventory.items[key]["Quantity"] * gs.game_state.inventory.items[key]["Weight"]))
        total_weight += gs.game_state.inventory.items[key]["InventorySpace"]
    gs.game_state.inventory.current_capacity = total_weight
