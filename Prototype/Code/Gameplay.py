from Display import *
import time

def update_status_bars(status_bars, game_time):
    for status_bar in status_bars.values():
        status_bar[0].gradual_decay(game_time)
    status_bar[0].gradual_decay(game_time)