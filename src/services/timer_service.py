import pygame
import pygame.freetype
import datetime

from paths import IMAGES_DIR, FONT_DIR

pygame.freetype.init()
font = pygame.freetype.Font(FONT_DIR / "Minecraft.ttf", 20)


class TimerService:
    def __init__(self):
        self.ticking = False
        self.time = 0
        self.fixedTime = ""

    def startTimer(self):
        self.time = 0

    def continueTimer(self):
        self.ticking = True

    def pauseTimer(self):
        self.ticking = False

    def update(self):
        if self.ticking:
            self.time += 1

    def showTime(self, screen):
        if self.ticking:
            time_fixed = list(str(datetime.timedelta(minutes=self.time)))
            del time_fixed[-3:]
            self.fixedTime = "".join(time_fixed)
            bg = pygame.image.load(IMAGES_DIR / "timer_bg.png").convert_alpha()
            rect = bg.get_rect()
            rect.top, rect.left = 20, 0
            screen.blit(bg, rect)
            font.render_to(
                screen, (90, 48),
                self.fixedTime,
                (0, 0, 0), None, size=80
            )

    def reset(self):
        self.ticking = False
        self.time = 0
        self.fixedTime = ""
