import pygame
from pygame.locals import *
import math


def is_close_app_event(event):
    return (
            (event.type == QUIT)
            or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE)
    )


def is_img_mask_collide_with_mouse(img, rect):
    mask = pygame.mask.from_surface(img)
    pos = pygame.mouse.get_pos()
    pos_in_mask = pos[0] - rect.x, pos[1] - rect.y
    return rect.collidepoint(*pos) and mask.get_at(pos_in_mask)


def sine(speed: float, time: int, how_far: float, overall_y: int) -> float:
    t = pygame.time.get_ticks() / 2 % time
    y = math.sin(t / speed) * how_far + overall_y
    return y
