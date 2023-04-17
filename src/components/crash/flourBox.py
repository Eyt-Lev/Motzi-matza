import pygame


from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from src.tools import is_img_mask_collide_with_mouse
from src.services.music_service import MusicService
from src.game_status import GameStatus


class FlourBox(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()
        self.image = VisualizationService.get_flour_box_img()
        self.rect = self.image.get_rect()
        self.x, self.y = position
        self.rect.left, self.rect.top = self.x, self.y
        self.hovered = self.rect.collidepoint(pygame.mouse.get_pos())
        self.alreadyPressed = self.hovered and pygame.mouse.get_pressed()[0]

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not self.alreadyPressed:
                if is_img_mask_collide_with_mouse(self.image, self.rect):
                    self.on_flour_collection()

    def setPressed(self):
        self.alreadyPressed = self.hovered and pygame.mouse.get_pressed()[0]

    def on_flour_collection(self):
        MusicService.play_flour_pick_up_sound()
        self.kill()
        GlobalState.game.flourCollected += 1

        if GlobalState.game.crash_wheat_added > 9:
            if GlobalState.game.flourCollected < 7:
                GlobalState.GAME_STATE = GameStatus.GAME_END

    def draw(self):
        self.x += 28
        self.rect.left, self.rect.top = self.x, self.y
        if self.rect.right >= 1920:
            MusicService.play_fail_sound()
            self.kill()

            if GlobalState.game.crash_wheat_added == 9:
                GlobalState.GAME_STATE = GameStatus.GAME_END

        GlobalState.SCREEN.blit(self.image, self.rect)
