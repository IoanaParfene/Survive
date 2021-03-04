import pygame

class Button:
    # Button width in pixels
    pixels = 60

    def __init__(self, button_type, icon_pos, size, screen, *varg):
        """ Initialize button attributes """
        # Prefix of button standard images
        self.button_type = button_type
        # Permanent button image loading, transforming and rectangle
        self.icon_pos = icon_pos
        # The butoon width and height
        self.size = size
        # The pygame screen
        self.screen = screen
        # Special extra custom variables for different buttons
        self.varg = list(varg)

    def on_click(self, event):
        """ On-click button action function"""
        if event.button == 1:
            if pygame.Rect(self.icon_pos[0],self.icon_pos[1],self.size[0],self.size[1]).collidepoint(event.pos):
                function_name = str(self.button_type).lower() + '_button_action'
                eval(function_name)(self)


def shelter_button_action(button):
    pass

def fire_button_action(button):
    pass

def getwater_button_action(button):
    pass

def crafting_button_action(button):
    pass

def inventory_button_action(button):
    pass

def explore_button_action(button):
    pass

def trapshunt_button_action(button):
    pass

def travel_button_action(button):
    pass

def ll_button_action(button):
    pass

