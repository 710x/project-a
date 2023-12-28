from time import sleep

from actions.base import BaseGame


class InitGame(BaseGame):
    def __init__(self, boy):
        super().__init__(boy, action_name='init_game')

    def start_game(self):
        self.boy.start_if_not_running()

    def waiting(self):
        while self.check_screen('game_logo') or self.check_screen('downloading_assets') or self.check_screen('loading'):
            sleep(60)

    def login(self):
        if self.check_screen('connect'):
            self.find_and_click('connect')
            sleep(60)
            self.waiting()
            # self.boy.swipe(start=(30, 640), end=(600, 640))
            if self.check_screen('google'):
                self.find_and_click('google')
                sleep(60)
                if self.check_screen('vi_use_another_account') or self.check_screen('en_use_another_account'):
                    self.find_and_click('vi_use_another_account', delta=(0, -60))
                    self.find_and_click('en_use_another_account', delta=(0, -60))
                    sleep(60)
                    while self.check_screen('signing_in'):
                        sleep(60)
                    if self.check_screen('i_agree'):
                        self.find_and_click('i_agree')
                        sleep(60)
                        if self.check_screen('confirm'):
                            self.find_and_click('confirm')
                            sleep(60)
                            self.waiting()
                            if self.check_screen('game_progress_found'):
                                self.find_and_click('ok')
                                sleep(60)
                                self.waiting()
        if self.check_screen('authorized'):
            self.find_and_click('authorized')
            sleep(60)
            if self.check_screen('confirm'):
                self.find_and_click('confirm')
                sleep(60)
                self.waiting()

        return self.check_screen('play') and self.check_screen('4_buttons')


