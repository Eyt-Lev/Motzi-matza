import pygame

from src.level import Level
from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from src.components.watering.flourBox import WaterFlourBox
from src.components.watering.dough import Dough
from src.components.endScreen import Reasons
from src.components.watering.mixer import Mixer

DOUGH_TO_COLLECT_ON_WATERING = 5
FLOURS_HAVE = 7


class WateringLevel(Level):

    def __init__(self):
        super().__init__()
        self.doughCollected = 0
        self.water_flours_added = 0
        self.sprites = pygame.sprite.Group()
        self.spritesSecondary = pygame.sprite.Group()
        self.spritesThird = pygame.sprite.Group()
        self.time = 0
        self.mixer = Mixer()
        self.last_succeed = False

    def draw(self):
        super().draw()

        VisualizationService.draw_watering_bg()
        for sprite in self.sprites:
            sprite.draw()
        for sprite in self.spritesSecondary:
            sprite.draw()
        for sprite in self.spritesThird:
            sprite.draw()
        self.mixer.draw()

        VisualizationService.draw_flour_score(
            score=7 - self.water_flours_added,
        )

        VisualizationService.draw_dough_score(
            score=self.doughCollected,
            y=160
        )

        VisualizationService.draw_pause_btn()

    def update(self):
        super().update()

        self.time += 1

        if len(self.sprites) == 0:
            mixer = Mixer()
            self.sprites.add(mixer)

        if self.water_flours_added < 7 and not self.last_succeed:
            if self.time == 80:
                self.spritesSecondary.add(
                    WaterFlourBox(
                        game=self
                    )
                )
                self.time = 0

        if self.mixer.check_collision(self.spritesSecondary):
            self.spritesThird.add(
                Dough(
                    (self.mixer.rect.centerx, self.mixer.rect.bottom + 10),
                    game=self
                      )
            )
            if self.water_flours_added == 6:
                self.last_succeed = True

    def check_succes(self):
        if self.doughCollected == DOUGH_TO_COLLECT_ON_WATERING:
            return True
        return False

    def check_failed(self):
        if self.water_flours_added == FLOURS_HAVE:
            GlobalState.GAME.deathMsg = Reasons.flourBoxesOver
            return True
        return False

    def on_success(self):
        GlobalState.GAME.level = 3.5
        GlobalState.GAME.last_level_completed = 3
