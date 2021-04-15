from kivy.uix.screenmanager import ScreenManager, NoTransition
from Screens.screen_inventory import InventoryScreen
from Screens.screen_game_over import GameOverScreen
from Screens.screen_crafting import CraftingScreen
from Screens.screen_shelter import ShelterScreen
from Screens.screen_hunting import HuntingScreen
from Screens.screen_travel import TravelScreen
from Screens.screen_pause import PauseScreen
from Screens.screen_game import GameWindow
from Screens.screen_start import StartMenu
from Screens.screen_fire import FireScreen
from kivy.lang import Builder

# Build Kivy files
Builder.load_file('KivyFiles/kivy_crafting.kv')
Builder.load_file('KivyFiles/kivy_fire.kv')
Builder.load_file('KivyFiles/kivy_game.kv')
Builder.load_file('KivyFiles/kivy_game_over.kv')
Builder.load_file('KivyFiles/kivy_hunting.kv')
Builder.load_file('KivyFiles/kivy_inventory.kv')
Builder.load_file('KivyFiles/kivy_pause.kv')
Builder.load_file('KivyFiles/kivy_shelter.kv')
Builder.load_file('KivyFiles/kivy_start.kv')
Builder.load_file('KivyFiles/kivy_travel.kv')

# Initialize Window Manager
sm = ScreenManager(transition=NoTransition())

# Game screens/windows/menus
screens = [StartMenu(name="start"), GameWindow(name="game"), GameOverScreen(name="over"), PauseScreen(name="pause"),
           ShelterScreen(name="shelter"), FireScreen(name="fire"), CraftingScreen(name="crafting"),
           InventoryScreen(name="inventory"), HuntingScreen(name="hunting"), TravelScreen(name="travel")]

# Add the screens to the screen manager
for screen in screens:
    sm.add_widget(screen)

# Set the first screen as the start menu
sm.current = "start"
