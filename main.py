import pygame

from src.game_status import GameStatus
from config import Config
from src.game_phases import main_menu_phase, exit_game_phase, gameplay_phase
from src.global_state import GlobalState
from src.services.music_service import MusicService

pygame.init()
FramePerSec = pygame.time.Clock()


def update_game_display():
    pygame.display.update()
    FramePerSec.tick(Config.FPS)


MusicService.start_background_music()


def main():
    while True:
        if GlobalState.GAME_STATE == GameStatus.MAIN_MENU:
            main_menu_phase()
        elif GlobalState.GAME_STATE == GameStatus.GAMEPLAY:
            gameplay_phase()
        elif GlobalState.GAME_STATE == GameStatus.GAME_END:
            exit_game_phase()

        update_game_display()


if __name__ == "__main__":
    main()
