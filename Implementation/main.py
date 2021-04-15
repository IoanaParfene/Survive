from GameLoopManagement import game_loop as gl
from kivy.uix.widget import Widget
from Screens import screens as sc
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
        gl.game_loop()

    def on_start(self):
        """ Called when starting the application """
        Clock.schedule_interval(self.run_game, 1 / 60)

    def build(self):
        return sc.sm


if __name__ == "__main__":
    SurviveApp().run()
