from PythonFiles.BackendFunctions import backend_fire as bbf
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from functools import partial

Window.maximize()


def create_label(text, pos_x, pos_y, size_x, size_y, h_align, v_align, scale):
    """ Create a custom label """
    # phone is 1, size_y, compare buttons with 1x, labels with 0x
    label = Label(text=text, pos_hint={"x": pos_x, "y": pos_y}, size_hint=(size_x, size_y),
                  font_size=Window.size[1] * size_y * scale, halign=h_align, valign=v_align)
    return label


def create_button(text, pos_x, pos_y, size_x, size_y, scale, function_name):
    """ Create a custom button """
    button = Button(text=text, background_color=(0.0, 0.0, 0.0, 1.0),
                    pos_hint={"x": pos_x, "y": pos_y}, size_hint=(size_x, size_y),
                    font_size=Window.size[1] * size_y * scale, on_release=eval(function_name))
    return button


# Show that the player is sheltered by the car at pike Lake
car_label = create_label("My car keeps me warm.", 0.35, 0.01, 0.4, 0.2, "left", "bottom", 0.4)
# Show that the player has build a raincatcher at the current location
rain_catcher_label = create_label("I have a rain catcher.", 0.35, 0.1, 0.4, 0.2, "left", "bottom", 0.4)
# Show that the player doesn't have tinder
fire_tinder_label = create_label("I need tinder.", 0.35, 0.6, 0.5, 0.2, "center", "middle", 0.5)
# Show that the player doesn't have tools to start a fire
fire_tools_label = create_label("I need tools to start a fire.", 0.35, 0.6, 0.5, 0.2, "center", "middle", 0.5)
# Show that the player doesn't have tools to start a fire
fire_time_remaining = create_label("", 0.05, 0.7, 0.25, 0.15, "left", "bottom", 0.5)

# Start a fire with matches
matches_start_fire_button = create_button("    START FIRE\nWITH MATCHES", 0.44, 0.67, 0.3, 0.18, 0.3, "partial(bbf.start_fire,'matches')")
# Start a fire with matches
plow_start_fire_button = create_button("    START FIRE\nWITH FIRE PLOW", 0.44, 0.44, 0.3, 0.18, 0.27, "partial(bbf.start_fire,'fire_plow')")
# Start a fire with matches
drill_start_fire_button = create_button("    START FIRE\nWITH BOW DRILL", 0.44, 0.21, 0.3, 0.18, 0.3, "partial(bbf.start_fire,'bow_drill')")

# Add wood to the fire
add_wood_button = create_button("ADD WOOD", 0.38, 0.67, 0.2, 0.18, 0.3, "partial(bbf.add_fuel,'wood')")
# Add hardwood to the fire
add_hardwood_button = create_button("ADD HARDWOOD", 0.63, 0.67, 0.2, 0.18, 0.27, "partial(bbf.add_fuel,'hardwood')")
# Add tinder tot the fire
add_tinder_button = create_button("ADD TINDER", 0.38, 0.44, 0.2, 0.18, 0.3, "partial(bbf.add_fuel,'tinder')")
# Boil dirty water to make it clean
boil_water_button = create_button("BOIL WATER", 0.63, 0.44, 0.2, 0.18, 0.3, "partial(bbf.boil_water)")

# Add hardwood to the fire
cook_meat_button = create_button("COOK MEAT", 0.38, 0.21, 0.2, 0.18, 0.3, "partial(bbf.cook_meat)")
# Add tinder tot the fire
smoke_meat_button = create_button("SMOKE MEAT", 0.63, 0.21, 0.2, 0.18, 0.3, "partial(bbf.smoke_meat)")

