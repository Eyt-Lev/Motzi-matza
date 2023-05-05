from src.level import Level
from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from src.services.score_service import ScoreService


class WonScreen(Level):

    def __init__(self):
        super().__init__()
        self.savedScore = False

    def draw(self):
        VisualizationService.draw_win_screen(GlobalState.TIMER.fixedTime)

    def update(self):
        if not self.savedScore:
            ScoreService.update_max_score(
                GlobalState.TIMER.time
            )
            self.savedScore = True
