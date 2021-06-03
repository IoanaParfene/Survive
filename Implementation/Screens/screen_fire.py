from Initialization import initialization as init
from Initialization import constants as cs
from Screens import GUI_classes as gui


class FireScreen(gui.BaseGameplayScreen):
    """ Screen for the fire starting menu """

    def show_info(self):
        self.show_popup(cs.fire_screen_info)
