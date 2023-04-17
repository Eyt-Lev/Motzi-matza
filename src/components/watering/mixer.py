import pygame
from pygame.locals import *

from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from src.services.music_service import MusicService
vec = pygame.math.Vector2


class Mixer(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.imageTop, self.image = VisualizationService.get_mixer_images()
        self.rectImgTop, self.rect = self.imageTop.get_rect(), self.image.get_rect()
        self.pos = vec((1700 + 420)/2, 700)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rectImgTop.centerx, self.rectImgTop.bottom = self.pos
        self.rect.centerx, self.rect.top = self.pos
        self.player_position = vec(0, 0)

    def check_collision(self, group):
        for sprite in group:
            if pygame.sprite.collide_mask(self, sprite):
                sprite.kill()
                MusicService.play_success_sound()
                return True

    def draw(self):
        self.acc = vec(0, 0)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_d] or pressed_keys[K_RIGHT] and self.rect.right < 1680:
            self.acc.x += 6
        elif pressed_keys[K_a] or pressed_keys[K_LEFT] and self.rect.left > 420:
            self.acc.x -= 6

        self.acc.x += self.vel.x * -0.3
        self.acc.y += self.vel.y * -0.3
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.player_position = self.pos.copy()

        self.rectImgTop.center = self.pos
        self.rect.center = self.pos
        GlobalState.SCREEN.blit(self.imageTop, self.rectImgTop)
        GlobalState.SCREEN.blit(self.image, self.rect)
