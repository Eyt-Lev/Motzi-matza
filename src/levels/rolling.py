import pygame

from src.level import Level
from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from src.components.endScreen import Reasons

ROLL_TO_COLLECT = 3
DOUGH_HAVE = 5


class RollingLevel(Level):

    def __init__(self):
        super().__init__()
        self.sprites = pygame.sprite.Group()
        self.spritesSecondary = pygame.sprite.Group()
        self.time = 0
        self.doughSent = 0
        self.rolledCollected = 0
        self.last_succeed = False

    def draw(self):
        super().draw()

        VisualizationService.draw_rolling_bg()
        for sprite in self.sprites:
            sprite.draw()
        for sprite in self.spritesSecondary:
            sprite.draw()

        VisualizationService.draw_pause_btn()

    def update(self):
        super().update()

        self.time += 1

    def check_succes(self):
        if self.rolledCollected == ROLL_TO_COLLECT:
            return True
        return False

    def check_failed(self):
        if self.doughSent == DOUGH_HAVE:
            GlobalState.GAME.deathMsg = Reasons.flourBoxesOver
            return True
        return False

    def on_success(self):
        GlobalState.GAME.level = 4.5
        GlobalState.GAME.last_level_completed = 4
