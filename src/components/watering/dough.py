import pygame

from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from src.tools import is_img_mask_collide_with_mouse


class Dough(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()
        self.time = 0
        self.uglyTime = 0
        self.image = VisualizationService.get_dough_image()
        self.rect = self.image.get_rect()
        self.x, self.y = position
        self.rect.centerx, self.rect.top = position
        self.alreadyPressed = False
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

    def handle_event(self):
        if pygame.mouse.get_pressed()[0]:
            if not self.alreadyPressed:
                if is_img_mask_collide_with_mouse(self.image, self.rect):
                    self.alreadyPressed = True
                    self.onPress()

    def onPress(self):
        self.kill()
        GlobalState.GAME.water_flours_added += 1
        if self.time > 8:
            GlobalState.GAME.doughCollected += 1
            GlobalState.music.play_success_sound()
        else:
            GlobalState.music.play_fail_sound()

    def draw(self):
        self.handle_event()
        # Adding to the time
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
            GlobalState.music.play_fail_sound()
            GlobalState.GAME.water_flours_added += 1

        if self.alive():
            self.pressRect = pygame.Rect(
                self.rect.left - 10,
                self.rect.top - 12,
                (self.rect.width + 15) / 10 * self.time,
                25
            )
            # Drawing
            GlobalState.SCREEN.blit(
                self.image,
                self.rect
            )
            # Drawing inner time rect
            pygame.draw.rect(
                GlobalState.SCREEN,
                color,
                self.pressRect,
            )
            # Drawing outer time rect
            pygame.draw.rect(
                GlobalState.SCREEN,
                (96, 96, 96),
                self.timeRect,
                3,
            )
