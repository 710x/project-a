from time import sleep
from actions.base import BaseGame


class Charactor(BaseGame):
    def __init__(self, boy):
        super().__init__(boy, action_name='charactor')

    def set_charactor_name(self, name=None):
        if name and self.find_and_click('options'):
            sleep(1)
            if self.find_and_click('profile'):
                if self.find_and_click('charactor_name_input', delta=(130, 20)):
                    sleep(1)
                    self.boy.enter_text(name)
                    sleep(1)
                    if self.find_and_click('ok'):
                        sleep(1)
                        if self.find_and_click('x'):
                            sleep(1)
                            return True
        return False

