from src.components.endScreen import Reasons
from src.game_status import GameStatus
from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService

from src.level import Level
from src.levels.explain import ExplainLevel
from src.levels.harvest import HarvestLevel
from src.levels.crash import CrashLevel
from src.levels.watering import WateringLevel
from src.levels.rolling import RollingLevel
from src.levels.cooking import CookingLevel
from src.levels.won import WonScreen


class Game:

    def __init__(self):
        self.level = 4
        self.deathMsg = None
        self.last_level_completed = self.level + 0.5
        self.pause = False
        self.levelManager = Level()
        self.explain = ExplainLevel()
        self.levels = {
            1: HarvestLevel(),
            2: CrashLevel(),
            3: WateringLevel(),
            4: RollingLevel(),
            5: CookingLevel(),
            5.5: WonScreen(),
        }

    def playLevel(self):
        if self.pause:
            self.pauseMenu()
            return

        self.levels.get(self.level, self.explain).update()
        self.levels.get(self.level, self.explain).draw()

        if self.level != 0 and self.level % 1 == 0:
            GlobalState.TIMER.update()
            GlobalState.TIMER.showTime(GlobalState.SCREEN)
            # check if timer is 18
            if GlobalState.TIMER.fixedTime == "18:00":
                self.deathMsg = Reasons.ranOutOfTime
                GlobalState.GAME_STATE = GameStatus.GAME_FAILED

    def pauseMenu(self):
        VisualizationService.draw_pos(
            int(self.level)
        )

    def play_rolling(self):
        pass

    def nextLevel(self):
        if self.level <= self.last_level_completed + 0.5:
            self.level += 0.5
            if not self.level % 1 == 0:
                GlobalState.TIMER.ticking = False
            else:
                GlobalState.TIMER.ticking = True

    def failed(self):
        if self.level != 0.5:
            GlobalState.music.play_end_sound()
            self.reset()

    def reset(self):
        if self.level != 0.5:
            self.level = 0.5
            GlobalState.TIMER.resetTimer()

    @staticmethod
    def retry():
        GlobalState.GAME = Game()
        GlobalState.GAME.level = 0.5
        GlobalState.GAME.last_level_completed = 1
        GlobalState.GAME_STATE = GameStatus.GAMEPLAY
