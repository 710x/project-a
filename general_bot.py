from actions.init_game.init_game import InitGame
from utils.android_boy import AndroidBoy


class Bot:
    def __init__(self, serial, app_package=None):
        if serial and app_package:
            self.boy = AndroidBoy(serial, center_point=(240, 160), is_joystick_show=False, app_package=app_package)
            self.init_game = InitGame(self.boy)
