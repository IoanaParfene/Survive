from PythonFiles.Widgets import widget_customs as wwc
from PythonFiles import constants as cs


class FireScreen(wwc.BaseGameplayScreen):
    """ Screen for the fire starting menu """

    def show_info(self):
        self.show_popup(cs.fire_screen_info)