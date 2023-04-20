import pygame
from pygame.locals import *

from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService

vec = pygame.math.Vector2

left = 460
right = 1645


class Mixer(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.imageTop, self.image = VisualizationService.get_mixer_images()
        self.rectImgTop, self.rect = self.imageTop.get_rect(), self.image.get_rect()
        self.pos = vec((1700 + 420) / 2, 700)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.speed = 8
        self.friction = -0.3

        self.rectImgTop.centerx, self.rectImgTop.bottom = self.pos
        self.rect.centerx, self.rect.top = self.pos

    def check_collision(self, group):
        for sprite in group:
            if pygame.sprite.collide_mask(self, sprite):
                sprite.kill()
                GlobalState.music.play_success_sound()
                return True

    def draw(self):
        self.acc = vec(0, 0)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_d] or pressed_keys[K_RIGHT] and self.rect.right < right:
            self.acc.x += self.speed
        elif pressed_keys[K_a] or pressed_keys[K_LEFT] and self.rect.left > left:
            self.acc.x -= self.speed

        self.acc.x += self.vel.x * self.friction
        self.acc.y += self.vel.y * self.friction
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rectImgTop.center = self.pos
        self.rect.center = self.pos
        GlobalState.SCREEN.blit(self.imageTop, self.rectImgTop)
        GlobalState.SCREEN.blit(self.image, self.rect)
