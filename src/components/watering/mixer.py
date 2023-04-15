import pygame
from pygame.locals import *

from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from src.services.music_service import MusicService
vec = pygame.math.Vector2


class Mixer(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = VisualizationService.get_mixer_image()
        self.rect = self.image.get_rect()
        self.pos = vec(800, 400)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.rect.center = self.pos
        self.player_position = vec(0, 0)
        self.gotoRight = True
        self.moverToSide = True

    def draw(self):
        self.acc = vec(0, 0)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
            self.acc.x += 6
        elif pressed_keys[K_a] or pressed_keys[K_LEFT]:
            self.acc.x -= 6

        self.acc.x += self.vel.x * -0.4
        self.acc.y += self.vel.y * -0.4
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.player_position = self.pos.copy()

        self.rect.center = self.pos
        GlobalState.SCREEN.blit(self.image, self.rect)
