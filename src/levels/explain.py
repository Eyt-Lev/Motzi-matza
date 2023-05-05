import pygame
import random

from src.level import Level
from src.services.visualization_service import VisualizationService
from src.global_state import GlobalState


class ExplainLevel(Level):

    def __init__(self):
        super().__init__()
        self.bg = pygame.image.load(random.choice(VisualizationService.get_explain_backgrounds()))

    def draw(self):
        VisualizationService.draw_explain_bg(
            self.bg
        )
        VisualizationService.draw_explain_box(
            GlobalState.GAME.level + 0.5
        )

    def update(self):
        super().update()