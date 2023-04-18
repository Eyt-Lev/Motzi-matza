import sys

import pygame

from src.game_status import GameStatus
from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from game import Game
from src.components.endScreen import EndScreen, Reasons

clock = pygame.time.Clock()
GlobalState.GAME = Game()


def main_menu_phase():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            start_game()
    VisualizationService.draw_main_menu(GlobalState.SCREEN, start_game)


def start_game():
    GlobalState.GAME_STATE = GameStatus.GAMEPLAY


def gameplay_phase():
    GlobalState.GAME.playLevel()


def failed_phase():
    GlobalState.GAME.reset()
    EndScreen.draw(
        GlobalState.GAME.deathMsg
    )


def exit_game_phase():
    pygame.quit()
    sys.exit()
