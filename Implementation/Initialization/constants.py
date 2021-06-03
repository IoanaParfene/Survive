# Game related time variables
game_speed = 1
game_time = 0
paused_time = 0
start_paused_time = 0
start_time = 0
skipped_time = 300
save_time = 0
rain_related_duration = 0
start_rain_related_time = 0
start_fire_time = 0
fire_duration = 0
time_is_stopped = True

# Environment information
current_game_day = 1
daylight_now = True
current_weather = "rain"
initial_miles = 30
remaining_miles = 30
shelter_complete = True
raining_now = True
clothing_on = True
fire_on = False

# PyGame running loop
running = True
game_over = "No"
replay = "No"

# Game locations
current_location = "pike_lake"
game_locations = {"pike_lake": True, "flooded_area": False, "muddy_road": False, "path": False, "woodland": False}
game_location_info = {"pike_lake": {"Name": "Pike Lake", "Miles": 3, "Duration": 3, "Water Source": True, "Explorables": (4,[("flashlight",15), ("wires",30), ("empty_bottle",15), ("newspaper",15), ("duct_tape",9), ("fishing_kit",8), ("matches",8)]) },
                      "flooded_area": {"Name": "Flooded Area", "Miles": 2, "Duration": 4, "Water Source": True, "Explorables": (4, [("plant_fiber", 38), ("maggots", 17), ("cattail_plant", 45)])},
                      "muddy_road": {"Name": "Muddy Road", "Miles": 2, "Duration": 3, "Water Source": False, "Explorables": (10, [("plant_fiber", 9), ("crickets", 14), ("birch_bark", 24), ("edible_berries",33), ("wood",20)])},
                      "muddy_area": {"Name": "Muddy Area", "Miles": 2, "Duration": 3, "Water Source": True, "Explorables": (8, [("plant_fiber", 23), ("crickets", 23), ("birch_bark", 7), ("edible_berries",12), ("wood",35)])},
                      "path": {"Name": "Path", "Miles": 3, "Duration": 3, "Water Source": False, "Explorables": (9, [("maggots", 29), ("crickets", 33), ("cattail_plant", 24), ("edible_berries",14)])},
                      "woodland": {"Name": "Woodland", "Miles": 2, "Duration": 3, "Water Source": False, "Explorables": (7, [("maggots", 38), ("crickets", 28), ("cattail_plant", 28), ("edible_berries",6)])}
                      }
water_locations = ["pike_lake", "flooded_area"]

# Inventory variables
max_inventory_capacity = 25
base_inventory_capacity = 6
current_inventory_capacity = 0
inventory_display_category = "A"
inventory_display_page = 0
space_boosters = [("dry_sack", 7), ("utility_belt_bag", 6), ("rope_net_bag", 4), ("pouch", 1)]
inventory_items = {"wood": {"Name": "Wood", "Weight": 3.0, "Categories": ["A", "Fi"], "Throw": True, "GetActions": {"Shave": ["tinder"]}, "BarActions": None, "Description": "Wood. Burns nicely and can be used to craft different tools."},
                    "area_map": {"Name": "Area Map", "Weight": 0.0, "Categories": ["A","G","Fi"], "Throw": True, "GetActions": {"Tear": ["tinder"]}, "BarActions": None, "Description": "I can get a rough idea how far I'm from safety."},
                    "empty_bottle": {"Name": "Empty Bottle", "Weight": 1.0, "Categories": ["A","Wa"], "Throw": True, "GetActions": None, "BarActions": None, "Description": "Plastic bottle. Empty. I gotta fill this somehow."},
                    "water_bottle_safe": {"Name": "Safe Water Bottle", "Weight": 2.0, "Categories": ["A","Wa"], "Throw": False, "GetActions": {"Pour": ["empty_bottle"]}, "BarActions": {"Drink": [("Hydration", 25.0)]}, "Description": "Plastic bottle. Full of portable water."},
                    "water_bottle_unsafe": {"Name": "Unsafe Water Bottle", "Weight": 2.0, "Categories": ["A","Wa"], "Throw": False, "GetActions": {"Pour": ["empty_bottle"]}, "BarActions": {"Drink": [("Hydration", 25.0)]}, "Description": "Plastic bottle. Full of unsafe water. It looks quite clean but I should purify this somehow."},
                    "energy_bar": {"Name": "Energy Bar", "Weight": 0.0, "Categories": ["A","Fo"], "Throw": False, "GetActions": {"Slice": ["bait","bait"]}, "BarActions": {"Eat": [("Calories", 150.0)]}, "Description": "Supplemental bar containing high energy food. Perfect for people that need a quick energy boost. Calories 150."},
                    "tinder": {"Name": "Tinder", "Weight": 0.34, "Categories": ["A","Fi"], "Throw": True, "GetActions": None, "BarActions": None, "Description": "Combustible material that will ignite with a small spark. Any kind of dry fluffy stuff will do."},
                    "hardwood": {"Name": "Hardwood", "Weight": 4.0, "Categories": ["A","Fi"], "Throw": True, "GetActions": {"Split": ["wood","wood"]}, "BarActions": None, "Description": "Dense wood. Burns long and can be used for crafting."},
                    "matches": {"Name": "Matches", "Weight": 0.0, "Categories": ["A","Fi"], "Throw": True, "GetActions": None, "BarActions": None, "Description": "Stormproof matches are a reliable and fast way to start a fire."},
                    "crickets": {"Name": "Crickets", "Weight": 0.34, "Categories": ["A","Fo"], "Throw": True, "GetActions": {"Slice": ["bait"]}, "BarActions": {"Eat": [("Calories", 100.0)]}, "Description": "Handful of insects. They sure have large back legs. Calories 100."},
                    "maggots": {"Name": "Maggots", "Weight": 0.34, "Categories": ["A","Fo"], "Throw": True, "GetActions": {"Slice": ["bait"]}, "BarActions": {"Eat": [("Calories", 50.0)]}, "Description": "I wonder if I can eat these. Calories 50."},
                    "bottle_of_soda": {"Name": "Soda Bottle", "Weight": 2.0, "Categories": ["A","Fo","Wa"], "Throw": False, "GetActions": None, "BarActions": {"Drink": [("Calories", 300.0), ("Hydration", 25.0)]}, "Description": "Plastic bottle. Sugary drink with added vitamins. Gives a short lasting energy boost. Calories 300."},
                    "edible_berries": {"Name": "Edible Berries", "Weight": 1.0, "Categories": ["A","Fo","Wa"], "Throw": True, "GetActions": {"Slice": ["bait"]}, "BarActions": {"Eat": [("Calories", 100.0), ("Hydration", 5.0)]}, "Description": "Berries. Better than nothing. Calories 100."},
                    "peanuts": {"Name": "Peanuts", "Weight": 1.0, "Categories": ["A","Fo"], "Throw": True, "GetActions": {"Slice": ["bait"]}, "BarActions": {"Eat": [("Calories", 150.0)]}, "Description": "Honey flavored roasted peanuts. Plenty of fat and protein. Calories 150."},
                    "squirrel_juice": {"Name": "Squirrel Juice", "Weight": 1.0, "Categories": ["A","Fo","Wa"], "Throw": False, "GetActions": None, "BarActions": {"Drink": [("Calories", 100.0), ("Hydration", 25.0)]}, "Description": "Bottle of sugary juice. Very tasty and refreshing. Calories 100."},
                    "canned_corn": {"Name": "Canned Corn", "Weight": 2.0, "Categories": ["A","Fo"], "Throw": False, "GetActions": None, "BarActions": {"Eat": [("Calories", 400.0)]}, "Description": "Big can full of corn. Better than peas. Calories 400."},
                    "smoked_jerky": {"Name": "Smoked Jerky", "Weight": 1.0, "Categories": ["A","Fo"], "Throw": False, "GetActions": {"Slice": ["bait","bait"]}, "BarActions": {"Eat": [("Calories", 300.0)]}, "Description": "Strips of meat. Smoked to prevent spoilage. Calories 300."},
                    "can_of_peas": {"Name": "Can of Peas", "Weight": 1.0, "Categories": ["A","Fo"], "Throw": True, "GetActions": None, "BarActions": {"Eat": [("Calories", 300.0)]}, "Description": "Peas in a tin can. Expiration date still alright. Calories 300."},
                    "cattail_plant": {"Name": "Cattail Plant", "Weight": 1.0, "Categories": ["A","Fo"], "Throw": True, "GetActions": {"Harvest": ["edible_plant_part","plant_fiber","tinder"]}, "BarActions": None, "Description": "Very useful plant."},
                    "edible_plant_part": {"Name": "Edible Plant Part", "Weight": 1.0, "Categories": ["A","Fo"], "Throw": True, "GetActions": None, "BarActions": {"Eat": [("Calories", 50.0)]}, "Description": "Here's the edible portion of a plant I found. Calories 50."},
                    "bait": {"Name": "Bait", "Weight": 0.34, "Categories": ["A","G"], "Throw": True, "GetActions": None, "BarActions": None, "Description": "Small edible substance used to attract prey. Good for fishing and traps."},
                    "empty_can": {"Name": "Empty Can", "Weight": 0.0, "Categories": ["A","G"], "Throw": False, "GetActions": None, "BarActions": None, "Description": "Garbage to some, a cooking pot for me. I can boil water in it."},
                    "basic_clothes": {"Name": "Basic Clothes", "Weight": 0.0, "Categories": ["A","G"], "Throw": False, "GetActions": {"Tear": ["piece_of_cloth","piece_of_cloth","torn_clothes"]}, "BarActions": None, "Description": "I have basic clothing. Won't keep me warm."},
                    "trash_bag": {"Name": "Trash Bag", "Weight": 0.0, "Categories": ["A","G"], "Throw": True, "GetActions": {"Braid": ["rope"]}, "BarActions": None, "Description": "A multi-purpose plastic bag."},
                    "dry_sack": {"Name": "Dry Sack", "Weight": 0.0, "Categories": ["A","G"], "Throw": True, "GetActions": None, "BarActions": None, "Description": "A floating, waterproof and lightweight sack for carrying stuff."},
                    "broken_cellphone": {"Name": "Broken Cellphone", "Weight": 1.0, "Categories": ["A","G"], "Throw": True, "GetActions": None, "BarActions": None, "Description": "Would be the most important survival item, except the screen is completely black. Smart phones..."},
                    "duct_tape": {"Name": "Duct Tape", "Weight": 0.0, "Categories": ["A","G"], "Throw": True, "GetActions": {"Braid": ["rope"]}, "BarActions": None, "Description": "Pretty much the best stuff on earth. I think i can CRAFT many things with this."},
                    "flashlight": {"Name": "Flashlight", "Weight": 2.0, "Categories": ["A","G"], "Throw": True, "GetActions": None, "BarActions": None, "Description": "A portable electric light source. Water resistant. Some battery remaining."},
                    "knife": {"Name": "Knife", "Weight": 0.0, "Categories": ["A","G"], "Throw": False, "GetActions": None, "BarActions": None, "Description": "Carbon Steel blade. Handle made of stained birch. Essential for survival."},
                    "first_aid_kit": {"Name": "First Aid Kit", "Weight": 2.0, "Categories": ["A","G"], "Throw": True, "GetActions": {"Open": ["first_aid_manual","bandages","bandages","pouch"]}, "BarActions": None, "Description": "A small first aid kit with bandages for treating wounds."},
                    "newspaper": {"Name": "Newspaper", "Weight": 1.0, "Categories": ["A","G"], "Throw": True, "GetActions": {"Tear": ["tinder","tinder"]}, "BarActions": None, "Description": "Well, it's a newspaper."},
                    "utility_belt_bag": {"Name": "Utility Belt Bag", "Weight": 0.0, "Categories": ["A","G"], "Throw": True, "GetActions": None, "BarActions": None, "Description": "A waist belt that has room for some gear."},
                    "piece_of_cloth": {"Name": "Piece of Cloth", "Weight": 1.0, "Categories": ["A","G"], "Throw": True, "GetActions": {"Wrap": ["bandages"]}, "BarActions": None, "Description": "Piece of cloth. I think I can craft bandages from this."},
                    "torn_clothes": {"Name": "Torn Clothes", "Weight": 0.0, "Categories": ["A","G"], "Throw": False, "GetActions": None, "BarActions": None, "Description": "My clothes are torn. Won't keep me warm."},
                    "rope": {"Name": "Rope", "Weight": 0.34, "Categories": ["A","G"], "Throw": True, "GetActions": None, "BarActions": None, "Description": "Piece of rope. Useful for many purposes in a survival situation. Each piece of rope requires 1/3 unit of carry space."},
                    "bandages": {"Name": "Bandages", "Weight": 1.0, "Categories": ["A","G"], "Throw": True, "GetActions": {"Tear": ["tinder"]}, "BarActions": {"Use": [("Condition", 20)]}, "Description": "Can be used to stop bleeding."},
                    "first_aid_manual": {"Name": "First Aid Manual", "Weight": 1.0, "Categories": ["A","G"], "Throw": True, "GetActions": {"Turn": ["backside_of_paper"]}, "BarActions": None, "Description": "Hmm, a paper... CONDITION can be recovered by use of bandages."},
                    "backside_of_paper": {"Name": "Backside Of A Paper", "Weight": 1.0, "Categories": ["A","G"], "Throw": True, "GetActions": {"Tear": ["tinder"]}, "BarActions": None, "Description": "Stay HYDRATED, keep BODY HEAT up and stay in good CONDITION."},
                    "pouch": {"Name": "Pouch", "Weight": 0.0, "Categories": ["A","G"], "Throw": False, "GetActions": None, "BarActions": None, "Description": "A small pouch. I can carry stuff in it. I can have a couple of these.[+1 CARRY SPACE]"},
                    "fishing_hook": {"Name": "Fishing Hook", "Weight": 0.34, "Categories": ["A","G"], "Throw": True, "GetActions": None, "BarActions": None, "Description": "A fishing hook. Sharp end."},
                    "wires": {"Name": "Wires", "Weight": 0.34, "Categories": ["A","G"], "Throw": True, "GetActions": {"Braid": ["rope","rope","rope","rope"]}, "BarActions": None, "Description": "Bundle of wires that I can use as rope."},
                    "plant_fiber": {"Name": "Plant Fiber", "Weight": 1.0, "Categories": ["A","G"], "Throw": True, "GetActions": {"Wrap": ["rope"]}, "BarActions": None, "Description": "Workable raw material found in nature."},
                    "birch_bark": {"Name": "Birch Bark", "Weight": 1.0, "Categories": ["A","Fi"], "Throw": True, "GetActions": {"Scrape": ["tinder","tinder","tinder"]}, "BarActions": None, "Description": "This stuff is great when I need to start a fire."},
                    "butane_lighter": {"Name": "Butane Lighter", "Weight": 1.0, "Categories": ["A","Fi"], "Throw": True, "GetActions": None, "BarActions": None, "Description": "A portable device used to generate a flame. Some butane gas is still left."},
                    "fishing_kit": {"Name": "Fishing Kit", "Weight": 2.0, "Categories": ["A","G"], "Throw": True, "GetActions": {"Open": ["rope","fishing_hook","empty_can"]}, "BarActions": None, "Description": "A spool of fishing line with couple of fishing hooks in a tin can."},
                    "fire_plow": {"Name": "Fire Plow", "Weight": 1.0, "Categories": ["A","Fi"], "Throw": True, "GetActions": None, "BarActions": None, "Description": "A primitive tool for starting a fire. Rubbing two sticks together should produce an ember."},
                    "bow_drill": {"Name": "Bow Drill", "Weight": 2.0, "Categories": ["A","Fi"], "Throw": True, "GetActions": None, "BarActions": None, "Description": "A primitive tool for starting a fire. Using the bow drill requires some skill and plenty of patience."},
                    "fishing_rod": {"Name": "Fishing Rod", "Weight": 3.0, "Categories": ["A","G"], "Throw": True, "GetActions": {"Tear": ["rope", "rope", "wood", "fishing_hook"]}, "BarActions": None, "Description": "A survival fishing rod made of stick, rope, and a hook. Good enough to catch a fish."},
                    "wooden_spear": {"Name": "Wooden Spear", "Weight": 1.0, "Categories": ["A","G"], "Throw": True, "GetActions": {"Tear": ["wood"]}, "BarActions": None, "Description": "It's a wooden spear with a pretty sharp tip. Better than bare handed hunting."},
                    "rope_net_bag": {"Name": "Rope Net Bag", "Weight": 0.0, "Categories": ["A","G"], "Throw": True, "GetActions":  None, "BarActions": None, "Description": "A survival net bag made of rope. Useful for carrying additional gear[+4 CARRY SPACE]."},
                    "wood_bundle": {"Name": "Wood Bundle", "Weight": 6.0, "Categories": ["A","Fi"], "Throw": True, "GetActions": {"Tear": ["wood", "wood", "wood", "wood"]}, "BarActions": None, "Description": "Bunch of wood tied together. Makes it easier to carry."},
                    "raw_meat": {"Name": "Raw Meat", "Weight": 1.0, "Categories": ["A","Fo"], "Throw": True, "GetActions": {"Slice": ["bait", "bait"]}, "BarActions": {"Eat": [("Calories", 400.0)]}, "Description": "Ready for cooking."},
                    "spoiled_meat": {"Name": "Spoiled Meat", "Weight": 3.0, "Categories": ["A","Fo"], "Throw": True, "GetActions": None, "BarActions": {"Eat": [("Calories", 200.0)]}, "Description": "This Smells very bad. I think I should throw this away."},
                    "cooked_meat": {"Name": "Cooked Meat", "Weight": 1.0, "Categories": ["A", "Fo"], "Throw": True, "GetActions": None, "BarActions": {"Eat": [("Calories", 800.0)]}, "Description": "Oh my gosh! This smells delicious."},
                    "dead_hare": {"Name": "Dead Hare", "Weight": 4.0, "Categories": ["A", "Fo"], "Throw": True, "GetActions": {"Cut": ["raw_meat", "raw_meat", "raw_meat", "bait", "hare_skin"]}, "BarActions": None, "Description": "Furry creature. Not going anywhere any more. Decent survival food after preparing and cooking."},
                    "dead_fish": {"Name": "Dead Fish", "Weight": 1.0, "Categories": ["A", "Fo"], "Throw": True, "GetActions": {"Cut": ["raw_meat"]}, "BarActions": None, "Description": "It's a dead fish. Raw."},
                    "dead_bird": {"Name": "Dead Bird", "Weight": 3.0, "Categories": ["A", "Fo"], "Throw": True, "GetActions": {"Cut": ["raw_meat", "raw_meat"]}, "BarActions": None, "Description": "Small dead bird."},
                    "hare_skin": {"Name": "Hare Skin", "Weight": 1.0, "Categories": ["A", "G"], "Throw": True, "GetActions": None, "BarActions": None, "Description": "Skin of a dead hare. Could be used to make a pouch."}
                   }

spoil_items = {"raw_meat": {"FreshTime": 15, "SpoilItems": ["spoiled_meat"]},
               "cooked_meat": {"FreshTime": 24, "SpoilItems": ["spoiled_meat"]},
               "dead_hare": {"FreshTime": 24, "SpoilItems": ["spoiled_meat", "spoiled_meat", "spoiled_meat"]},
               "dead_fish": {"FreshTime": 8, "SpoilItems": ["spoiled_meat"]},
               "dead_bird": {"FreshTime": 14, "SpoilItems": ["spoiled_meat", "spoiled_meat"]}
              }
spoiling_rates = {"raw_meat": [],
                  "cooked_meat": [],
                  "dead_hare": [],
                  "dead_fish": [],
                  "dead_bird": []
                }
damaging_consumables = {"water_bottle_unsafe": {"DamageInterval": (0,60)},
                        "raw_meat": {"DamageInterval": (30,70)},
                        "spoiled_meat": {"DamageInterval": (50,90)}
                        }

# Crafting Menu
craftable_items = {#"fire_plow": {"Name": "Fire Plow", "Limit": True, "Duration": 30, "Needed": [("wood", 1)], "Description": "A primitive tool for starting a fire. Rubbing two sticks together should produce an ember. I can only have one."},
                   #"bow_drill": {"Name": "Bow Drill", "Limit": True, "Duration": 30, "Needed": [("hardwood", 1), ("rope", 1)], "Description": "A primitive tool for starting a fire. Using the bow drill requires some skill and plenty of patience. I can only have one."},
                   #"fishing_rod": {"Name": "Fishing Rod", "Limit": True, "Duration": 30, "Needed": [("wood", 1), ("rope", 2), ("fishing_hook", 1)], "Description": "A survival fishing rod made of stick, rope, and a hook. Good enough to catch a fish. I can only have one."},
                   #"fishing_hook": {"Name": "Wooden Fishing Hook", "Limit": False, "Duration": 60, "Needed": [("wood", 1)], "Description": "A fishing hook. Sharp end."},
                   "rope": {"Name": "Rope", "Limit": False, "Duration": 30, "Needed": [("piece_of_cloth", 1)], "Description": "Piece of rope. Useful for many purposes in a survival situation. Each piece of rope requires 1/3 unit of carry space."},
                   #"wooden_spear": {"Name": "Wooden Spear", "Limit": True, "Duration": 30, "Needed": [("hardwood", 1)], "Description": "It's a wooden spear with a pretty sharp tip. Better than bare handed hunting. I can only have one."},
                   "rope_net_bag": {"Name": "Rope Net Bag", "Limit": True, "Duration": 180, "Needed": [("rope", 3)], "Description": "A survival net bag made of rope. Useful for carrying additional gear[+4 CARRY SPACE]. I can only have one."},
                   "pouch": {"Name": "Pouch", "Limit": False, "Duration": 120, "Needed": [("hare_skin",1), ("rope", 1)], "Description": "A small pouch. I can carry stuff in it. I can have a couple of these.[+1 CARRY SPACE]"},
                   "wood_bundle": {"Name": "Wood Bundle", "Limit": False, "Duration": 60, "Needed": [("wood", 4), ("rope", 1)], "Description": "Bunch of wood tied together. Makes it easier to carry."}
                    }
craftable_scroll_page = 0


# Hunting and traps
hunting_trap_actions = {#"track": {"Locations": ["muddy_road", "path", "woodland"]},
                        "set_bird_trap": {"Locations": ["muddy_road", "muddy_area", "path", "woodland"]},
                        "set_fish_trap": {"Locations": ["flooded_area", "muddy_area"]},
                        "set_deadfall": {"Locations": ["path", "woodland"]},
                        #"spear_fish": {"Locations": ["flooded_area", "muddy_area"]},
                        #"fish": {"Locations": ["flooded_area", "muddy_area"]},
                        "dismantle_traps": {"Locations": ["flooded_area", "muddy_road", "muddy_area", "path", "woodland"]}
                        }

traps = {"deadfall": {"Needed":[("wood", 1), ("bait", 1)], "HourlyTrapChance": 0.03, "Prey": "hare"},
         "fish_trap": {"Needed":[("rope", 1), ("wood", 1), ("bait", 1)], "HourlyTrapChance": 0.04, "Prey": "fish"},
         "bird_trap": {"Needed":[("rope", 1), ("wood", 1), ("bait", 1)], "HourlyTrapChance": 0.05, "Prey": "bird"}
        }
last_trap_hour = 0
last_hour_trapped_animals = []

# Heat factor fluctuation
# shelter, rain, daytime, clothing, fire
heat_factor_fluctuation = {"srdcf": 0.0, "snrdcf": 0.0, "srndcf": 0.0, "srdncf": 0.0, "srdcnf": 0.0, "snrndcf": 0.0,
                      "snrdncf": 0.0, "snrdcnf": 0.0, "srndncf": 0.0, "srndcnf": 0.0, "srdncnf": 0.0, "snrndncf": 0.0,
                      "snrndcnf": 0.0, "snrdncnf": 0.0, "srndncnf": 0.0, "snrndncnf": 0.0,
                      "nsrdcf": -2.0, "nsnrdcf": 30.0, "nsrndcf": -3.0, "nsrdncf": -4.5, "nsrdcnf": -3.5,
                      "nsnrndcf": 25.0, "nsnrdncf": 28.0, "nsnrdcnf": 0.5, "nsrndncf": -4.5, "nsrndcnf": -8.0,
                      "nsrdncnf": -6.0, "nsnrndncf": 23.0, "nsnrndcnf": -4.5, "nsnrdncnf": 0.0, "nsrndncnf": -9.5,
                      "nsnrndncnf": -6.0,
                     }
heat_factor_names = ["shelter_complete", "raining_now", "daylight_now", "clothing_on", "fire_on"]
# Start heat factor code = nsrdcf
current_heat_factor_code = None

# Food and water
rain_water = 0
rain_water_uses = 0
rain_catcher_exists = False

# Screen info
shelter_screen_info = "I can use a trash bag to build a raincatcher to collect water during rain. It takes an hour."
fire_screen_info = "I need tinder to start a fire.\nI can boil dirty water from the creek.\nI can cook raw meat or smoke it to prevent it from spoiling."
hunting_screen_info = "I can set traps to catch food.\nDEADFALL(1 wood, 1 bait - 60 minutes): catches hares\nFISH TRAP(1 wood, 1 rope, 1 bait - 60 minutes): catches fish\nBIRD TRAP(1 wood, 1 rope, 1 bait - 60 minutes): catches birds\nI should dismantle the traps before travelling to recover some materials."