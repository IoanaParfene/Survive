import math

from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout

from Initialization import initialization as init
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.modalview import ModalView
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivymd.app import MDApp


class Background(Widget):
    """ Class for changing the background during the day """

    # The path to background image
    this_source = StringProperty("Images/night.png")

    def change_background(self, *args):
        """ Change background after the day period """
        # Total game hours that have passed
        game_hours = init.game_state.game_time / 60
        # The current day of the game
        init.game_state.current_game_day = int(game_hours / 24 + 1)
        # Game hours that have passed in the current day
        game_hours_today = game_hours % 24

        # Change background image path based on the time of the current day
        if game_hours_today < 2:
            self.this_source = "Images/dawn.png"
        if game_hours_today < 7:
            self.this_source = "Images/orange.png"
        elif game_hours_today < 10:
            self.this_source = "Images/purple.png"
        elif game_hours_today < 12:
            self.this_source = "Images/sunset.png"
        else:
            self.this_source = "Images/night.png"


class ActionTime(ModalView):

    def __init__(self, text, **kwargs):
        super(ActionTime, self).__init__(**kwargs)

        # Set the specific text for the action
        self.ids.action_time_label.text = text
        # Call dismiss_view after one second
        Clock.schedule_once(self.dismiss_view, 1)

    def dismiss_view(self, dt):
        self.dismiss()


class Rain(Widget):
    """ Class for the rain animation """

    # The y position of the rain animation
    this_y = NumericProperty(-0.25)

    def show_rain(self, *args):
        """ Change rain animation """
        if init.game_state.raining_now:
            if self.this_y < -0.25:
                self.this_y += 5000
        else:
            if self.this_y > -5000.25:
                self.this_y -= 5000


class BaseGameplayScreen(Screen):
    """ Base class for gameplay menu screens """

    # Background animation object
    background = Background()
    # Rain animation object
    rain = Rain()

    def change_window(self, new_current_window):
        """ Screen changing method """
        MDApp.get_running_app().root.current = new_current_window

    def show_popup(self, text):
        """ Show a pop-up with a given text """
        view = ModalView(pos_hint={"x": 0.0, "y": 0.0}, size_hint=(1.0, 1.0), background="Images/black.png")
        layout = FloatLayout(pos_hint={"x": 0.0, "y": 0.0}, size_hint=(1.0, 1.0))
        layout.add_widget(Label(text=text, pos_hint={"x": 0.1, "y": 0.4}, size_hint=(0.8, 0.5),
                                font_size=self.height * 0.05, text_size=self.size, halign='center', valign='middle'))
        layout.add_widget(Button(pos_hint={"x": 0.44, "y": 0.3}, size_hint=(0.12, 0.1), font_size=self.height * 0.05,
                                 background_color=(2.5, 2.5, 2.5, 1.0), on_release=view.dismiss,
                                 color=(0.0, 0.0, 0.0, 1.0), text="OKAY", bold=True))
        view.add_widget(layout)
        view.open()


class DescriptionLabel(FloatLayout):
    """ Universal label for displaying a message on the screen """

    # Position coordinates of the label
    pos_x = NumericProperty(-500)
    pos_y = NumericProperty(-500)

    # Size of the label
    size_x = NumericProperty(-500)
    size_y = NumericProperty(-500)

    # Size scale
    scale = NumericProperty(-500)

    def __init__(self, text, pos_x, pos_y, size_x, size_y, h_align, v_align, scale, **kwargs):
        super(DescriptionLabel, self).__init__(**kwargs)
        # Set the specific text for the label
        self.text = text
        # Set the position of the label
        self.pos_x = pos_x
        self.pos_y = pos_y
        # Set the size of the label
        self.size_x = size_x
        self.size_y = size_y
        # Set alignments
        self.halign = h_align
        self.valign = v_align
        self.scale = scale

    def dismiss_view(self, dt):
        """ Label deleting method """
        self.dismiss()


class RoundButton(Button):

    # Position coordinates of the label
    pos_x = NumericProperty(-500)
    pos_y = NumericProperty(-500)

    # Size of the label
    size_x = NumericProperty(-500)
    size_y = NumericProperty(-500)

    #
    disable = BooleanProperty(False)
    release_function = StringProperty("")

    def __init__(self, pos_x, pos_y, size_x, size_y, disable, release_function, **kwargs):
        super(RoundButton, self).__init__(**kwargs)
        # Set the position of the label
        self.pos_x = pos_x
        self.pos_y = pos_y
        # Set the size of the label
        self.size_x = size_x
        self.size_y = size_y
        #
        self.disable = disable
        self.release_function = release_function

    def on_touch_down(self, touch):
        print(self.pos[0], self.pos[0] + self.width)
        print(self.pos[1], self.pos[1] + self.height)
        print(touch.x, touch.y)
        left = touch.x >= self.pos[0] + self.width / 2.0
        down = touch.y >= self.pos[1] + self.height / 2.0
        up = touch.y <= self.pos[1] + self.size[1] - self.height / 2.0
        right = touch.x <= self.pos[0] + self.size[0] - self.width / 2.0
        #p = ((math.pow((x - h), 2) // math.pow(a, 2)) +(math.pow((y - k), 2) // math.pow(b, 2)))

        h = self.pos[0] + self.width/2
        k = self.pos[1] + self.height/2
        x = touch.x
        y = touch.y
        a = self.width/2
        b = self.height/2
        print(h,k,x,y,a,b)
        in_circle = ((math.pow((x - h), 2) / math.pow(a, 2)) +
             (math.pow((y - k), 2) / math.pow(b, 2)))

        if in_circle<=1:
            print('collided!')
            self.dispatch('on_release')
        else:
            print('outside of area!')