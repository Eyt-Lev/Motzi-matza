import pygame
import random

from src.level import Level
from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from src.components.harvest.wheat import Wheat

wheat_positions = [
    (3, 213),
    (7, 510),
    (275, 510),
    (16, 742),
    (1330, 506),
    (1800, 348),
]
WHEAT_TO_END_HARVEST = 1
INTERVAL_BETWEEN_WHEAT_SPAWNS = 20


class HarvestLevel(Level):

    def __init__(self):
        super().__init__()
        self.wheatsCollected = 0
        self.sprites = pygame.sprite.Group()
        self.time = 0

    def draw(self):
        super().draw()

        VisualizationService.draw_harvest_level(
            GlobalState.SCREEN
        )

        VisualizationService.draw_wheat_score(
            wheats=self.wheatsCollected,
            y=10
        )
        for wheat in self.sprites:
            wheat.draw()

        VisualizationService.draw_pause_btn()

    def update(self):
        self.time += 1

        if self.time == INTERVAL_BETWEEN_WHEAT_SPAWNS:
            position = random.choice(wheat_positions)
            self.sprites.empty()
            self.sprites.add(
                Wheat(
                    position=position,
                    wheat_to_end_harvest=WHEAT_TO_END_HARVEST,
                    game=self
                )
            )
            GlobalState.music.play_wheat_grow_sound()
            self.time = 0

        super().update()

    def check_succes(self):
        if self.wheatsCollected >= WHEAT_TO_END_HARVEST:
            return True
        return False

    def on_success(self):
        GlobalState.GAME.level = 1.5
        GlobalState.GAME.last_level_completed = 1
