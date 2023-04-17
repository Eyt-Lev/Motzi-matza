import pygame

from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from src.tools import is_img_mask_collide_with_mouse
from src.services.music_service import MusicService
from src.game_status import GameStatus


class Dough(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()
        self.time = 0
        self.uglyTime = 0
        self.image = VisualizationService.get_dough_image()
        self.rect = self.image.get_rect()
        self.x, self.y = position
        self.rect.centerx, self.rect.top = position
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        self.alreadyPressed = self.hovered and pygame.mouse.get_pressed()[0]
        self.timeRect = pygame.Rect(
            self.rect.left - 10,
            self.rect.top - 12,
            self.rect.width + 15,
            25
        )

        self.pressRect = pygame.Rect(
            self.rect.left - 10,
            self.rect.top - 12,
            (self.rect.width + 15) / 10 * self.time,
            25
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not self.alreadyPressed:
                if is_img_mask_collide_with_mouse(self.image, self.rect):
                    self.onPress()

    def setPressed(self):
        self.alreadyPressed = self.hovered and pygame.mouse.get_pressed()[0]

    def onPress(self):
        self.kill()
        if self.time > 8:
            GlobalState.game.doughCollected += 1

    def draw(self):
        self.uglyTime += 0.25
        if self.uglyTime % 1 == 0:
            self.time += 1

        if self.time < 9:
            color = (255, 0, 0)
        elif self.time <= 10:
            color = (51, 204, 51)
        else:
            color = (255, 0, 0)
            self.kill()

        if self.alive():
            self.pressRect = pygame.Rect(
                self.rect.left - 10,
                self.rect.top - 12,
                (self.rect.width + 15) / 10 * self.time,
                25
            )
            GlobalState.SCREEN.blit(self.image, self.rect)
            pygame.draw.rect(
                GlobalState.SCREEN,
                (96, 96, 96),
                self.timeRect,
                3,
            )
            pygame.draw.rect(
                GlobalState.SCREEN,
                color,
                self.pressRect,
            )
