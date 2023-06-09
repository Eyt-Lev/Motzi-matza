import pygame

from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from src.tools import is_img_mask_collide_with_mouse


class Wheat(pygame.sprite.Sprite):

    def __init__(self, position, wheat_to_end_harvest, game):
        super().__init__()
        self.image = VisualizationService.get_wheat_image()
        self.rect = self.image.get_rect()
        self.pos = position
        self.rect.left, self.rect.top = self.pos
        self.alreadyPressed = False
        self.wheat_to_end_harvest = wheat_to_end_harvest
        self.game = game

    def handle_event(self):
        if not self.alreadyPressed:
            if is_img_mask_collide_with_mouse(self.image, self.rect) and pygame.mouse.get_pressed()[0]:
                self.alreadyPressed = True
                self.on_wheat_collection()

    def on_wheat_collection(self):
        GlobalState.music.play_wheat_break_sound()
        self.kill()
        self.game.wheatsCollected += 1

    def draw(self):
        self.handle_event()
        GlobalState.SCREEN.blit(self.image, self.rect)
