import datetime

import pygame
import pygame.freetype

from paths import IMAGES_DIR, FONT_DIR

pygame.freetype.init()
font = pygame.freetype.Font(FONT_DIR / "Minecraft.ttf", 20)


class TimerService:
    def __init__(self):
        self.ticking = False
        self.time = 0
        self.fixedTime = "00:00"

    def update(self):
        self.time += 0.75

    def showTime(self, screen):
        self.fixedTime = TimerService.get_fixedTime(self.time)
        bg = pygame.image.load(IMAGES_DIR / "timer_bg.png").convert_alpha()
        rect = bg.get_rect()
        rect.top, rect.left = 10, 0
        screen.blit(bg, rect)
        font.render_to(
            screen, (90, 38),
            self.fixedTime,
            (0, 0, 0), None, size=80
        )

    @staticmethod
    def get_fixedTime(time):
        time_fixed = list(str(datetime.timedelta(minutes=time)))
        del time_fixed[-3:]
        return "".join(time_fixed)

    def resetTimer(self):
        self.ticking = False
        self.time = 0
        self.fixedTime = ""
