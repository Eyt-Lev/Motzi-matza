import pygame

from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from src.tools import is_img_mask_collide_with_mouse


class Wheat(pygame.sprite.Sprite):

    def __init__(self, position, wheat_to_end_harvest):
        super().__init__()
        self.image = VisualizationService.get_wheat_image()
        self.rect = self.image.get_rect()
        self.pos = position
        self.rect.left, self.rect.top = self.pos
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        self.alreadyPressed = self.hovered and pygame.mouse.get_pressed()[0]
        self.wheat_to_end_harvest = wheat_to_end_harvest

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not self.alreadyPressed:
                if is_img_mask_collide_with_mouse(self.image, self.rect):
                    self.on_wheat_collection()

    def on_wheat_collection(self):
        GlobalState.music.play_wheat_break_sound()
        self.kill()
        GlobalState.GAME.wheatsCollected += 1
        if GlobalState.GAME.wheatsCollected == self.wheat_to_end_harvest:
            GlobalState.GAME.finishLevel()

    def draw(self):
        GlobalState.SCREEN.blit(self.image, self.rect)
