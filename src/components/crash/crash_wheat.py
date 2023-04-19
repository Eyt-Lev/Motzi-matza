import pygame

from src.global_state import GlobalState
from src.services.music_service import MusicService
from src.services.visualization_service import VisualizationService


class CrashWheat(pygame.sprite.Sprite):

    def __init__(self, position, wheat_to_end_harvest):
        super().__init__()
        self.image = VisualizationService.get_wheat_image()
        self.rect = self.image.get_rect()
        self.x, self.y = position
        self.rect.centerx, self.rect.top = self.x, self.y
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        self.alreadyPressed = self.hovered and pygame.key.get_pressed()[pygame.K_SPACE]
        self.gotoRight = True
        self.moverToSide = True
        self.wheat_to_end_harvest = wheat_to_end_harvest

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if not self.alreadyPressed and self.y == 30:
                self.goDown()

    def goDown(self):
        self.y += 1

    def decideDirection(self):
        if self.y > 30:
            self.y += 30
            if self.y >= 300:
                self.y = 340
            self.moverToSide = False
        elif self.x <= 750:
            self.gotoRight = False
        elif self.x >= 1350:
            self.gotoRight = True

    def draw(self):
        # Drawing
        self.decideDirection()
        if self.moverToSide:  # If not dropped
            if self.gotoRight:
                self.x -= 22
            else:
                self.x += 22
        VisualizationService.draw_crash_wheat_handler(self.x)
        self.rect.centerx, self.rect.top = self.x, self.y
        GlobalState.SCREEN.blit(self.image, self.rect)

        # If dropped, Check collision with tube
        if self.y >= 340:
            touchingTube = self.rect.collidepoint((1025, 340)) and self.rect.collidepoint((995, 340))
            if touchingTube:
                self.on_success()
            else:
                self.on_fail()

    def on_success(self):
        self.kill()
        MusicService.play_success_sound()
        GlobalState.GAME.send_flour()
        GlobalState.GAME.crash_wheat_added += 1
        if GlobalState.GAME.crash_wheat_added == self.wheat_to_end_harvest:
            GlobalState.GAME.last_succeed = True
        else:
            GlobalState.GAME.add_crash_wheat()

    def on_fail(self):
        self.kill()
        MusicService.play_fail_sound()
        GlobalState.GAME.add_crash_wheat()
        GlobalState.GAME.crash_wheat_added += 1
