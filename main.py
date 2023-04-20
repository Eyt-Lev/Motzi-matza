import pygame

from config import Config
from src.game_phases import main_menu_phase, exit_game_phase, gameplay_phase, failed_phase
from src.game_status import GameStatus
from src.global_state import GlobalState

pygame.init()
FramePerSec = pygame.time.Clock()


def update_game_display():
    pygame.display.update()
    FramePerSec.tick(Config.FPS)


state_functions = {
    GameStatus.MAIN_MENU: main_menu_phase,
    GameStatus.GAMEPLAY: gameplay_phase,
    GameStatus.GAME_FAILED: failed_phase,
    GameStatus.GAME_END: exit_game_phase
}


def main():
    while True:
        state_functions[GlobalState.GAME_STATE]()
        update_game_display()
        GlobalState.music.start_background_music()


if __name__ == "__main__":
    main()
