from Initialization import constants as cs
import random


def randomize_location_info(location_key):
    """ Randomize Information about a travel location """
    locations_info = dict()
    locations_info["Key"] = location_key
    locations_info["Name"] = cs.game_location_info[location_key]["Name"]
    locations_info["Miles"] = cs.game_location_info[location_key]["Miles"]
    locations_info["Duration"] = random.randint(cs.game_location_info[location_key]["Duration"],
                                                cs.game_location_info[location_key]["Duration"] + 2)
    locations_info["Water Source"] = cs.game_location_info[location_key]["Water Source"]
    # Randomize a list of explorable items
    number_explorable_items = random.randint(cs.game_location_info[location_key]["Explorables"][0] - 1,
                                             cs.game_location_info[location_key]["Explorables"][0] + 2)
    choices = [item[0] for item in cs.game_location_info[location_key]["Explorables"][1]]
    weights = (item[1] for item in cs.game_location_info[location_key]["Explorables"][1])
    explorable_item_list = random.choices(choices, weights=weights, k=number_explorable_items)
    locations_info["Explorables"] = explorable_item_list
    return locations_info
