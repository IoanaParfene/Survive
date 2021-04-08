import variable_initialization as var_init
from kivy.uix.widget import Widget
import game_play_functions as gpf
import display_functions as df
import screen_functions as sf
from kivy.clock import Clock
from kivymd.app import MDApp
import game_state as gs
import screens as sc
import time
import os

from kivy.core.window import Window
Window.maximize()


class GamePlay(Widget):
    def update(self):
        pass


class SurviveApp(MDApp):

    def run_game(self, *args):
        """ Game loop frame b frame """
        if sc.sm.current == "start":
            if not os.path.isfile(df.get_path('save_game.pkl')):
                sc.sm.get_screen("start").ids.load_button.disabled = True
            else:
                sc.sm.get_screen("start").ids.load_button.disabled = False

        if sc.sm.current == "game":
            if gs.game_state.time_is_stopped:
                gpf.update_paused_time()

        if sc.sm.current == "pause":
            if not gs.game_state.time_is_stopped:
                gs.game_state.time_is_stopped = True
                gs.game_state.start_paused_time = time.time()

        for screen_type in ["game", "shelter", "fire", "crafting", "inventory", "hunting", "travel"]:
            gpf.update_inventory()
            if gs.game_state.game_time // 60 > 1 or gs.game_state.current_game_day > 1:
                if gs.game_state.game_over != "No":
                    if os.path.isfile(df.get_path('save_game.pkl')):
                        os.remove(df.get_path("save_game.pkl"))
                    if gs.game_state.game_over != "Lost":
                        sc.sm.get_screen("over").ids.background_over.this_source = df.get_path("Images/won_background.png")
                    if gs.game_state.game_over != "Won":
                        sc.sm.get_screen("over").ids.background_over.this_source = df.get_path("Images/lost_background.png")
                    sc.sm.get_screen(screen_type).change_window("over")

            if sc.sm.current == screen_type:
                gs.game_state.game_time = gpf.get_game_time()

        for screen_type in ["game", "shelter", "travel", "inventory"]:
                sc.sm.get_screen(screen_type).ids.time_label.text = df.game_time_description()
                sc.sm.get_screen(screen_type).ids.location_label.text = df.get_progress_description()

                gpf.update_status_bars()
                hydration_value = max(0, min(gs.game_state.status_bars["Hydration"].max_value,
                                             gs.game_state.status_bars["Hydration"].current_value))
                sc.sm.get_screen(screen_type).ids.my_hydration_bar.value = hydration_value
                sc.sm.get_screen(screen_type).ids.hydration_label_value.text = str(hydration_value)
                condition_value = max(0, min(gs.game_state.status_bars["Condition"].max_value,
                                             gs.game_state.status_bars["Condition"].current_value))
                sc.sm.get_screen(screen_type).ids.my_condition_bar.value = condition_value
                sc.sm.get_screen(screen_type).ids.condition_label_value.text = str(condition_value)
                heat_value = max(0, min(gs.game_state.status_bars["Body Heat"].max_value,
                                        gs.game_state.status_bars["Body Heat"].current_value))
                sc.sm.get_screen(screen_type).ids.my_heat_bar.value = heat_value
                sc.sm.get_screen(screen_type).ids.heat_label_value.text = str(heat_value)

                calories = max(0, min(gs.game_state.status_bars["Calories"].max_value,
                           gs.game_state.status_bars["Calories"].current_value))
                sc.sm.get_screen(screen_type).ids.calories_label.text = "CALORIES: " + str(calories) + "/3000"

        for screen_type in ["game", "shelter", "travel", "inventory"]:
            sc.sm.get_screen(screen_type).ids.background.change_background()

        if sc.sm.current == "start":
            pass
        elif sc.sm.current == "game":
            pass
        elif sc.sm.current == "pause":
            pass
        elif sc.sm.current == "over":
            pass
        elif sc.sm.current == "shelter":
            pass
        elif sc.sm.current == "fire":
            pass
        elif sc.sm.current == "crafting":
            pass
        elif sc.sm.current == "inventory":
            sf.display_inventory()
            sc.sm.get_screen(screen_type).ids.my_inventory_capacity_bar.value = int(gs.game_state.inventory.current_capacity)
            sc.sm.get_screen(screen_type).ids.my_inventory_capacity_bar.max = gs.game_state.inventory.max_capacity
            sc.sm.get_screen(screen_type).ids.inventory_capacity_label.text = str(int(gs.game_state.inventory.current_capacity)) + "/" + \
                                                            str(gs.game_state.inventory.max_capacity)
        elif sc.sm.current == "hunting":
            pass
        elif sc.sm.current == "travel":
            name, miles = gs.game_state.travel_next[0]["Name"], gs.game_state.travel_next[0]["Miles"]
            hours = var_init.game_location_info[gs.game_state.travel_next[0]["Key"]]["Duration"]
            if gs.game_state.status_bars["Calories"].current_value<400:
                text = name.upper() + " | " + str(miles) + " MILES | " + str(hours+2) + "-" + str(hours+2+1) + " HOURS"
            else:
                text = name.upper() + " | " + str(miles) + " MILES | " + str(hours) + "-" + str(hours + 1) + " HOURS"
            if gs.game_state.current_day_period == "DARKNESS":
                text = "???"
            sc.sm.get_screen("travel").ids.travel_1.text = text
            gs.game_state.game_time = gpf.get_game_time()

            name, miles = gs.game_state.travel_next[1]["Name"], gs.game_state.travel_next[1]["Miles"]
            hours = var_init.game_location_info[gs.game_state.travel_next[1]["Key"]]["Duration"]
            if gs.game_state.status_bars["Calories"].current_value < 400:
                text = name.upper() + " | " + str(miles) + " MILES | " + str(hours + 2) + "-" + str(
                    hours + 2 + 1) + " HOURS"
            else:
                text = name.upper() + " | " + str(miles) + " MILES | " + str(hours) + "-" + str(
                    hours + 1) + " HOURS"
            if gs.game_state.current_day_period == "DARKNESS":
                text = "???"
            sc.sm.get_screen("travel").ids.travel_2.text = text

        # print(gs.game_state.game_time, gs.game_state.start_paused_time, gs.game_state.paused_time, gs.game_state.time_is_stopped)

    def on_start(self):
        Clock.schedule_interval(self.run_game, 1 / 60)

    def build(self):
        return sc.sm

    def on_pause(self):
        print("Pizza")
        return True

    def on_resume(self):
        print("resumed")

if __name__ == "__main__":
    SurviveApp().run()
