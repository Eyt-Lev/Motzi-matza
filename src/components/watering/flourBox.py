import random
import pygame


from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService


class WaterFlourBox(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = VisualizationService.get_flour_box_img()
        self.rect = self.image.get_rect()
        self.x, self.y = (0, 119)
        self.rect.left, self.rect.top = self.x, self.y
        self.acc = random.randint(0, 33)

    def draw(self):
        self.rect.right, self.rect.top = self.x, self.y
        if self.y >= 750:   # Touching the floor
            self.kill()
        elif self.x >= 530:    # In the air
            self.y += 20
            self.x += self.acc
        else:                   # On the conveyor belt
            self.x += 18

        GlobalState.SCREEN.blit(self.image, self.rect)
