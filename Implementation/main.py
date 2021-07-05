from PythonFiles.Screens import screens as sc
from kivy.uix.widget import Widget
from PythonFiles.game_loop import game_loop
from kivy.clock import Clock
from kivymd.app import MDApp

from kivy.core.window import Window
Window.maximize()


class GamePlay(Widget):
    def update(self):
        pass


class SurviveApp(MDApp):

    def run_game(self, *args):
        """ Game loop frame by frame """
        game_loop()

    def on_start(self):
        """ Called when starting the application """
        Clock.schedule_interval(self.run_game, 1 / 60)

    def build(self):
        return sc.sm


if __name__ == "__main__":
    SurviveApp().run()
