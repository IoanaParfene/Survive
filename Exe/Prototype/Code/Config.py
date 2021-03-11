import pygame


# Get path to different data files
def get_path(file):
    import os
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, file)
    return my_file


# Initialize the game
pygame.init()

# Title and App Icon
pygame.display.set_caption("Survive")

# Create Window and Background
screen = pygame.display.set_mode((1200, 600))

# Background
background = pygame.image.load(get_path("Pictures/Background.jpg"))
background = pygame.transform.scale(background, (1600, 1200))

# Font
pygame.font.init()

# Game related time variables
game_speed = 1
game_time = 0
paused_time = 0
start_paused_time = 0
start_time = 0
skipped_time = 0


# Environiment information
current_game_day = 1
current_day_period = "DAYLIGHT"
current_weather = "rain"
remaining_miles = 50

# PyGame running loop
running = True
game_over = "No"
replay = "No"

# Game scene variables
current_scene = "Main"
game_scenes = {"Main": True, "Pause": False, "Shelter": False, "Fire": False, "Crafting": False, "Inventory": False,
               "Traps/Hunt": False, "Travel": False}

# Game actions and buttons
game_buttons = {"Main": ["Shelter", "Fire", "Crafting", "Inventory", "Traps/Hunt", "Travel", "Pause"],
                "Pause": ["Main"], #"SaveQuit"
                "Shelter": ["Main"], #, "Info"],
                "Fire": ["Main"],
                "Crafting": ["Main"],
                "Inventory": ["Main"],
                "Traps/Hunt": ["Main"],
                "Travel": ["Main"]
                }
game_actions = {"Main": ["Explore", "GetWater"],
                "Pause": [],
                "Shelter": ["Sleep1", "Sleep4"],
                "Fire": ["MakeFire"],
                "Crafting": [],
                "Inventory": ["Item0", "Item1"], #, "Item2"],
                "Traps/Hunt": [],
                "Travel": ["Travel1", "Travel2"]
                }


# Game locations
current_location = "pike_lake"
game_locations = {"pike_lake": True, "flooded_area": False, "muddy_road": False, "path": False, "woodland": False}
game_location_info = {"pike_lake": {"Name": "Pike Lake", "Miles": 3, "Duration":3},
                      "flooded_area": {"Name": "Flooded Area", "Miles:": 4, "Duration":5},
                      "muddy_road": {"Name": "Muddy Road", "Miles:": 4, "Duration":5},
                      "path": {"Name": "Path", "Miles:": 3, "Duration":3},
                      "woodland": {"Name": "Woodland", "Miles:": 4, "Duration":3}
                      }


# Inventory
inventory_items = {"wood": {"Name": "Wood", "Weight": 3, "Quantity": 8, "Calories": None, "Hydration": None},
                   "area_map": {"Name": "Area Map", "Weight": 0, "Quantity": 1, "Calories": None, "Hydration": None},
                   "plastic_bag": {"Name": "Plastic Bag", "Weight": 0, "Quantity": 1, "Calories": None, "Hydration": None},
                   "empty_bottle": {"Name": "Empty Bottle", "Weight": 1, "Quantity": 1, "Calories": None, "Hydration": None},
                   "water_bottle": {"Name": "Water Bottle", "Weight": 2, "Quantity": 2, "Calories": None, "Hydration": 25},
                   "energy_bar": {"Name": "Energy Bar", "Weight": 1, "Quantity": 2, "Calories": 300, "Hydration": None}
                   }

# Fire
# is on, hours remaining, start_time
fire = ["False", 0, 0]