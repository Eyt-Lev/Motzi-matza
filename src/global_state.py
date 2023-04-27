import pygame
from pygame.locals import *

from config import Config
from paths import IMAGES_DIR
from src.game_status import GameStatus
from src.services.music_service import MusicService
from src.services.timer_service import TimerService


class GlobalState:
    GAME_STATE = GameStatus.MAIN_MENU
    SCREEN = None
    GAME = None
    TIMER = TimerService()
    music = MusicService()

    @staticmethod
    def load_main_screen():
        pygame.display.set_icon(pygame.image.load(IMAGES_DIR / "mini_logo.png"))
        screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT), HWSURFACE | DOUBLEBUF | RESIZABLE)
        screen.fill((0, 255, 255))
        GlobalState.SCREEN = screen
        pygame.display.set_caption("Motzi Matza")
