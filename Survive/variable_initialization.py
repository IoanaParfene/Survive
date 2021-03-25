import time

# Game related time variables
game_speed = 10
game_time = 0
paused_time = 0
start_paused_time = 0
start_time = 0
skipped_time = 0
time_is_stopped = True

# Environiment information
current_game_day = 1
current_day_period = "DAYLIGHT"
current_weather = "rain"
remaining_miles = 50

# PyGame running loop
running = True
game_over = "No"
replay = "No"

# Game locations
current_location = "pike_lake"
game_locations = {"pike_lake": True, "flooded_area": False, "muddy_road": False, "path": False, "woodland": False}
game_location_info = {"pike_lake": {"Name": "Pike Lake", "Miles": 3, "Duration":3},
                      "flooded_area": {"Name": "Flooded Area", "Miles:": 4, "Duration":5},
                      "muddy_road": {"Name": "Muddy Road", "Miles:": 4, "Duration":5},
                      "path": {"Name": "Path", "Miles:": 3, "Duration":3},
                      "woodland": {"Name": "Woodland", "Miles:": 4, "Duration":3}
                      }

def get_path(file):
    import os
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, file)
    return my_file