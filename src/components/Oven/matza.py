import random

import pygame

from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from src.tools import is_img_mask_collide_with_mouse

alreadyPressed = False


class Matza(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.type = random.randint(0, 2)
        self.image = VisualizationService.get_matza_image(self.type)
        self.rect = self.image.get_rect()
        self.x, self.y = (970, 658)
        self.time = 0
        self.rect.left, self.rect.top = self.x, self.y

    def got_clicked(self):
        global alreadyPressed
        if not alreadyPressed:
            if is_img_mask_collide_with_mouse(self.image, self.rect) and pygame.mouse.get_pressed()[0]:
                alreadyPressed = True
                return True
        if pygame.mouse.get_pressed()[0] == 0:
            alreadyPressed = False

    def handle_click(self):
        if self.got_clicked():
            self.kill()
            if self.type == 0:
                GlobalState.GAME.matzaCollected += 1
                GlobalState.music.play_success_sound()
            else:
                GlobalState.GAME.matzaCollected -= 1
                GlobalState.music.play_fail_sound()

    def draw(self):
        self.time += 1
        self.handle_click()
        self.rect.right, self.rect.top = self.x, self.y
        GlobalState.SCREEN.blit(self.image, self.rect)
        self.x += 10
        if self.time == 10:
            self.kill()
            self.time = 0
