import pygame

from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from src.tools import is_img_mask_collide_with_mouse


class FlourBox(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()
        self.image = VisualizationService.get_flour_box_img()
        self.rect = self.image.get_rect()
        self.x, self.y = position
        self.rect.left, self.rect.top = self.x, self.y
        self.alreadyPressed = False

    def handle_event(self):
        if pygame.mouse.get_pressed()[0]:
            if not self.alreadyPressed:
                if is_img_mask_collide_with_mouse(self.image, self.rect):
                    self.alreadyPressed = True
                    self.on_flour_collection()

    def on_flour_collection(self):
        GlobalState.music.play_flour_pick_up_sound()
        GlobalState.GAME.flourCollected += 1
        self.kill()
        GlobalState.GAME.last_succeed = False

    def draw(self):
        self.handle_event()
        self.x += 28
        self.rect.left, self.rect.top = self.x, self.y
        if self.rect.right >= 1920:  # if it goes off-screen
            GlobalState.music.play_fail_sound()
            self.kill()
            GlobalState.GAME.last_succeed = False

        GlobalState.SCREEN.blit(self.image, self.rect)
