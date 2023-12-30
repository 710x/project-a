import math
import random
from time import sleep

from actions.base import BaseGame


class Play(BaseGame):
    def __init__(self, boy):
        super().__init__(boy, action_name='play')
        self.v = 60

    def finding_game(self):
        while self.check_screen('cancel'):
            sleep(2)
        return True

    @staticmethod
    def count_radian(p=None):
        if not p:
            return None
        center_screen = (480, 320)
        top_screen = (480, 640)
        monster_point = p
        ang = math.degrees(math.atan2(top_screen[1] - center_screen[1], top_screen[0] - center_screen[0]) - math.atan2(monster_point[1] - center_screen[1], monster_point[0] - center_screen[0]))
        return (ang + 360 if ang < 0 else ang) * math.pi / 180

    @staticmethod
    def random_radian():
        return random.random() * math.pi * 2

    @staticmethod
    def distance(p=None):
        center_screen = (480, 320)
        if not p:
            return
        return math.sqrt((center_screen[0] - p[0]) ** 2 + (center_screen[1] - p[1]) ** 2)

    def move_charactor(self, p, ):
        rad = self.count_radian(p)
        dist = self.distance(p)
        self.boy.joystick(radius=dist, degrees=rad, duration=dist / self.v)

    def playing_game(self):
        return

    def start_game_play(self):
        if self.find_and_click('home'):
            sleep(1)
            if self.find_and_click('home'):
                if not self.check_screen('game_mode_hunt'):
                    if self.find_and_click('game_mode'):
                        sleep(1)
                        self.find_and_click('hunt')
                if self.find_and_click('play'):
                    sleep(1)
                    if self.finding_game():
                        self.playing_game()
