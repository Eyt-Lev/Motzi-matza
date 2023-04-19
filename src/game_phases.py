import sys

import pygame

from game import Game
from src.components.endScreen import EndScreen
from src.game_status import GameStatus
from src.global_state import GlobalState
from src.services.visualization_service import VisualizationService

GlobalState.GAME = Game()


def main_menu_phase(): VisualizationService.draw_main_menu(GlobalState.SCREEN, start_game)


def start_game(): GlobalState.GAME_STATE = GameStatus.GAMEPLAY


def gameplay_phase(): GlobalState.GAME.playLevel()


def failed_phase():
    GlobalState.GAME.reset()
    EndScreen.draw(
        GlobalState.GAME.deathMsg
    )


def exit_game_phase():
    pygame.quit()
    sys.exit()
