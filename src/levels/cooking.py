import pygame

from src.level import Level
from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from src.components.endScreen import Reasons
from src.components.Oven.matza import Matza


class CookingLevel(Level):

    def __init__(self):
        super().__init__()
        self.time = 0
        self.matzaCollected = 0
        self.sprites = pygame.sprite.Group()

    def draw(self):
        super().draw()
        VisualizationService.draw_oven_bg()

        for sprite in self.sprites:
            sprite.draw()

        VisualizationService.draw_matza_score(self.matzaCollected)
        VisualizationService.draw_pause_btn()

    def update(self):
        super().update()

        if len(self.sprites) == 0:
            self.time += 1
            if self.time == 10:
                self.time = 0
                self.sprites.add(Matza(
                    self
                ))

    def check_succes(self):
        if self.matzaCollected == 3:
            return True
        return False

    def check_failed(self):
        if self.matzaCollected == -3:
            GlobalState.GAME.deathMsg = Reasons.wrongMatzot
            return True
        return False

    def on_success(self):
        GlobalState.GAME.level = 5.5
