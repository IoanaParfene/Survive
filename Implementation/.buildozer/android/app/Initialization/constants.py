# Game related time variables
game_speed = 1
game_time = 0
paused_time = 0
start_paused_time = 0
start_time = 0
skipped_time = 0
save_time = 0
time_is_stopped = True

# Environment information
current_game_day = 1
current_day_period = "DAYLIGHT"
current_weather = "rain"
remaining_miles = 30

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

# Inventory variables
max_inventory_capacity = 25
current_inventory_capacity = 0 #Drink, Eat, PatchWound
inventory_items = {"wood": {"Name": "Wood", "Weight": 3.0, "Categories": ["A", "Fi"], "Throw": True, "GetActions": {"Shave": ["tinder"]}, "BarActions": None, "Description": "Wood. Burns nicely and can be used to craft different tools."},
                    "area_map": {"Name": "Area Map", "Weight": 0.0, "Categories": ["A","G","Fi"], "Throw": True, "GetActions": {"Tear": ["tinder"]}, "BarActions": None, "Description": "I can get a rough idea how far I'm from safety."},
                    "empty_bottle": {"Name": "Empty Bottle", "Weight": 1.0, "Categories": ["A","Wa"], "Throw": True, "GetActions": None, "BarActions": None, "Description": "Plastic bottle. Empty. I gotta fill this somehow."},
                    "water_bottle_safe": {"Name": "Safe Water Bottle", "Weight": 2.0, "Categories": ["A","Wa"], "Throw": False, "GetActions": None, "BarActions": {"Drink": [("Hydration", 25.0)]}, "Description": "Plastic bottle. Full of portable water."},
                    "water_bottle_unsafe": {"Name": "Unsafe Water Bottle", "Weight": 2.0, "Categories": ["A","Wa"], "Throw": False, "GetActions": None, "BarActions": {"Drink": [("Hydration", 25.0), ("Condition",-30.0)]}, "Description": "Plastic bottle. Full of unsafe water. It looks quite clean but I should purify this somehow."},
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
                    "knife": {"Name": "Knife", "Weight": 0.0, "Categories": ["A","G"], "Throw": False, "GetActions": {"Braid": ["rope"]}, "BarActions": None, "Description": "Carbon Steel blade. Handle made of stained birch. Essential for survival."},
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
                    }

inventory_display_category = "A"
inventory_display_page = 0