from actions.init_game.init_game import InitGame
from utils.android_boy import AndroidBoy


class Bot:
    def __init__(self, serial):
        if serial:
            self.boy = AndroidBoy(serial, center_point=(240, 160), is_joystick_show=False,
                                  app_package='com.hunters.on.chain.mainnet')
            self.init_game = InitGame(self.boy)