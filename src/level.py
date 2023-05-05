from src.global_state import GlobalState
from src.game_status import GameStatus


class Level:
    def __init__(self):
        self.onTime = False

    def update(self):
        if self.check_succes():
            self.on_success()
            return
        if self.check_failed():
            self.on_fail()
            return

    def draw(self):
        pass

    @staticmethod
    def on_fail():
        GlobalState.GAME_STATE = GameStatus.GAME_FAILED

    def on_success(self):
        pass

    def check_succes(self):
        pass

    def check_failed(self):
        pass

    def next_level(self):
        pass

    def failed(self):
        pass
