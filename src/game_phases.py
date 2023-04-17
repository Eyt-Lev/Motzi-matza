import sys

import pygame

from src.game_status import GameStatus
from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService
from game import Game


clock = pygame.time.Clock()
GlobalState.game = Game()


def main_menu_phase():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            start_game()
    VisualizationService.draw_main_menu(GlobalState.SCREEN, start_game)


def start_game():
    GlobalState.GAME_STATE = GameStatus.GAMEPLAY


def gameplay_phase():
    GlobalState.game.playLevel()


def exit_game_phase():
    pygame.quit()
    sys.exit()
