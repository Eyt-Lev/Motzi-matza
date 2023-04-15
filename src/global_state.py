import pygame

from src.game_status import GameStatus
from config import Config
from src.services.timer_service import TimerService


class GlobalState:
    game = None
    GAME_STATE = GameStatus.MAIN_MENU
    SCREEN = None
    timer = TimerService()

    @staticmethod
    def load_main_screen():
        screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        screen.fill((0, 255, 255))
        GlobalState.SCREEN = screen
