from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
import pickle
import Survive.screens
from kivy.clock import Clock
from kivy.uix.widget import Widget
import Survive.variable_initialization as var_init
import time
import Survive.game_state as gs
import Survive.time_management as time_management
import os

class GamePlay(Widget):
    def update(self):
        pass


class SurviveApp(App):
    #game_state = gs.GameState()
    sm = Survive.screens.sm


    def run_game(self, *args):

        if (self.sm.current == "start"):
            if not os.path.isfile(var_init.get_path('save_game.pkl')):
                self.sm.get_screen("start").ids.load_button.disabled = True
            else:
                self.sm.get_screen("start").ids.load_button.disabled = False

        if (self.sm.current == "game"):
            if gs.game_state.time_is_stopped == True:
                gs.game_state.update_paused_time()

        if (self.sm.current == "pause"):
            if gs.game_state.time_is_stopped == False:
                gs.game_state.time_is_stopped = True
                gs.game_state.start_paused_time = time.time()

        for screen_type in ["game", "shelter", "fire", "crafting", "inventory", "hunting", "travel"]:
            #print(gs.game_state.game_over)
            if gs.game_state.game_time//60 > 1 or gs.game_state.current_game_day > 1:
                if gs.game_state.game_over != "No":
                    if os.path.isfile(var_init.get_path('save_game.pkl')):
                        os.remove(var_init.get_path("save_game.pkl"))
                    if(gs.game_state.game_over != "Lost"):
                        self.sm.get_screen("over").ids.background_over = var_init.get_path("lost_background.png")
                    if(gs.game_state.game_over != "Won"):
                        self.sm.get_screen("over").ids.background_over = var_init.get_path("won_background.png")
                    self.sm.get_screen(screen_type).change_window("over")

            if (self.sm.current == screen_type):
                gs.game_state.game_time = gs.game_state.get_game_time()

        for screen_type in ["game", "shelter"]:
            if (self.sm.current == screen_type):
                self.sm.get_screen(screen_type).ids.time_label.text = time_management.display_game_time(gs.game_state)
                self.sm.get_screen(screen_type).ids.location_label.text = time_management.display_game_progress(gs.game_state)

                time_management.update_status_bars(gs.game_state)
                """self.sm.get_screen(screen_type).ids.my_hydration_bar.value = gs.game_state.status_bars["Hydration"].current_value
                self.sm.get_screen(screen_type).ids.hydration_label_value.text = str(
                    gs.game_state.status_bars["Hydration"].current_value)
                self.sm.get_screen(screen_type).ids.my_condition_bar.value = gs.game_state.status_bars["Condition"].current_value
                self.sm.get_screen(screen_type).ids.condition_label_value.text = str(
                    gs.game_state.status_bars["Condition"].current_value)
                self.sm.get_screen(screen_type).ids.my_heat_bar.value = gs.game_state.status_bars["Body Heat"].current_value
                self.sm.get_screen(screen_type).ids.heat_label_value.text = str(
                    gs.game_state.status_bars["Body Heat"].current_value)"""
                hydration_value = max(0, min(gs.game_state.status_bars["Hydration"].max_value,
                                             gs.game_state.status_bars["Hydration"].current_value))
                self.sm.get_screen(screen_type).ids.my_hydration_bar.value = hydration_value
                self.sm.get_screen(screen_type).ids.hydration_label_value.text = str(hydration_value)
                condition_value = max(0, min(gs.game_state.status_bars["Condition"].max_value,
                                             gs.game_state.status_bars["Condition"].current_value))
                self.sm.get_screen(screen_type).ids.my_condition_bar.value = condition_value
                self.sm.get_screen(screen_type).ids.condition_label_value.text = str(condition_value)
                heat_value = max(0, min(gs.game_state.status_bars["Body Heat"].max_value,
                                        gs.game_state.status_bars["Body Heat"].current_value))
                self.sm.get_screen(screen_type).ids.my_heat_bar.value = heat_value
                self.sm.get_screen(screen_type).ids.heat_label_value.text = str(heat_value)

                calories = gs.game_state.status_bars["Calories"].current_value
                self.sm.get_screen(screen_type).ids.calories_label.text = "CALORIES: " + str(calories) + "/3000"

        if(self.sm.current == "start"):
            pass
        elif (self.sm.current == "game"):
            self.sm.get_screen("game").ids.background.change_background()
            self.sm.get_screen("shelter").ids.background.change_background()
            self.sm.get_screen("travel").ids.background.change_background()
        elif (self.sm.current == "pause"):
            pass
        elif (self.sm.current == "over"):
            pass
        elif (self.sm.current == "shelter"):
            self.sm.get_screen("shelter").ids.background.change_background()
            self.sm.get_screen("game").ids.background.change_background()
            self.sm.get_screen("travel").ids.background.change_background()
        elif (self.sm.current == "fire"):
            pass
        elif (self.sm.current == "crafting"):
            pass
        elif (self.sm.current == "inventory"):
            pass
        elif (self.sm.current == "hunting"):
            pass
        elif (self.sm.current == "travel"):
            name, miles, duration = gs.game_state.game_location_info[gs.game_state.travel_next[0]].values()
            text = name.upper() + " | " + str(miles) + " MILES | " + str(duration) + " HOURS"
            self.sm.get_screen("travel").ids.travel_1.text = text
            gs.game_state.game_time = gs.game_state.get_game_time()
            name, miles, duration = gs.game_state.game_location_info[gs.game_state.travel_next[1]].values()
            text = name.upper() + " | " + str(miles) + " MILES | " + str(duration) + " HOURS"
            self.sm.get_screen("travel").ids.travel_2.text = text
            self.sm.get_screen("travel").ids.background.change_background()
            self.sm.get_screen("shelter").ids.background.change_background()
            self.sm.get_screen("game").ids.background.change_background()

        #print(gs.game_state.game_time, gs.game_state.start_paused_time, gs.game_state.paused_time, gs.game_state.time_is_stopped)

    def on_start(self):
        Clock.schedule_interval(self.run_game, 1/60)

    #time = StringProperty()

    #def update(self, *args):
        #self.time = str(time.asctime())

    def build(self):
        #self.load_kv('test.kv')
        #Clock.schedule_interval(self.update,1)

        return self.sm

# Kivy style file
kv = Builder.load_file("survive.kv")


if __name__ == "__main__":
    SurviveApp().run()