import pygame
import random

from src.level import Level
from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from src.components.endScreen import Reasons
from src.components.crash.crash_wheat import CrashWheat
from src.components.crash.flourBox import FlourBox

WHEATS_TO_CRASH = 9
FLOURS_TO_COLLECT_ON_CRASH = 7


class CrashLevel(Level):

    def __init__(self):
        super().__init__()
        self.crash_wheat_added = 0
        self.flourCollected = 0
        self.sprites = pygame.sprite.Group()
        self.spritesSecondary = pygame.sprite.Group()
        self.last_succeed = False

    def draw(self):
        super().draw()

        VisualizationService.draw_crash_level(
            GlobalState.SCREEN
        )
        VisualizationService.draw_flour_score(
            score=self.flourCollected
        )
        VisualizationService.draw_wheat_score(
            wheats=9 - self.crash_wheat_added, y=150
        )
        for flour in self.sprites:
            flour.draw()
        for wheat in self.spritesSecondary:
            wheat.draw()

        VisualizationService.draw_pause_btn()

    def update(self):
        super().update()

        if len(self.spritesSecondary) == 0:
            self.add_crash_wheat()

    def check_succes(self):
        if self.flourCollected == FLOURS_TO_COLLECT_ON_CRASH:
            return True
        return False

    def check_failed(self):
        if self.crash_wheat_added == WHEATS_TO_CRASH and not self.last_succeed and not self.flourCollected == FLOURS_TO_COLLECT_ON_CRASH:
            GlobalState.GAME.deathMsg = Reasons.wheatCrashOver
            return True
        return False

    def on_success(self):
        GlobalState.GAME.level = 2.5
        GlobalState.GAME.last_level_completed = 2

    def add_crash_wheat(self):
        position = (random.randint(750, 1350), 30)
        self.spritesSecondary.add(
            CrashWheat(
                position=position,
                wheat_to_end_harvest=WHEATS_TO_CRASH,
                game=self
            )
        )

    def send_flour(self):
        self.sprites.add(
            FlourBox(
                (1286, 693),
                game=self
            )
        )
