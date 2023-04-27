import random

import pygame

from src.components.Oven.matza import Matza
from src.components.crash.crash_wheat import CrashWheat
from src.components.crash.flourBox import FlourBox
from src.components.endScreen import Reasons
from src.components.harvest.wheat import Wheat
from src.components.watering.dough import Dough
from src.components.watering.flourBox import WaterFlourBox
from src.components.watering.mixer import Mixer
from src.game_status import GameStatus
from src.global_state import GlobalState
from src.services.score_service import ScoreService
from src.services.visualization_service import VisualizationService

sprites = pygame.sprite.Group()
spritesSecondary = pygame.sprite.Group()
spritesThird = pygame.sprite.Group()
time = 0
wheat_positions = [
    (3, 213),
    (7, 510),
    (275, 510),
    (16, 742),
    (1330, 506),
    (1800, 348),
]
mixer = None
INTERVAL_BETWEEN_WHEAT_SPAWNS = 20
WHEAT_TO_END_HARVEST = 9
FLOURS_TO_COLLECT_ON_CRASH = 7
DOUGH_TO_COLLECT_ON_WATERING = 5
saved = False


class Game:

    def __init__(self):
        self.level = 5
        self.crash_wheat_added = 0
        self.wheatsCollected = 0
        self.flourCollected = 0
        self.bg = None
        self.last_succeed = False
        self.water_flours_added = 1
        self.doughCollected = 0
        self.deathMsg = Reasons.ranOutOfTime
        self.last_level_completed = self.level + 0.5
        self.pause = False
        self.matzaCollected = 0

    def playLevel(self):
        if self.pause:
            self.pauseMenu()
            return
        if self.level == 1:  # harvest
            self.play_harvest()
        elif self.level == 2:  # crash
            self.play_crash()
        elif self.level == 3:  # watering
            self.play_watering()
        elif self.level == 4:  # rolling
            self.play_rolling()
        elif self.level == 5:  # cooking
            self.play_cooking()
        elif self.level > 5:
            self.finishGame()
            return
        else:  # explanation
            self.explain()

        if self.level != 0 and self.level % 1 == 0:  # if playing (not explain)
            VisualizationService.draw_pause_btn()
            GlobalState.TIMER.update()
            GlobalState.TIMER.showTime(GlobalState.SCREEN)
            # check if timer is 18
            if GlobalState.TIMER.fixedTime == "18:00":
                self.deathMsg = Reasons.ranOutOfTime
                GlobalState.GAME_STATE = GameStatus.GAME_FAILED

    def pauseMenu(self):
        VisualizationService.draw_pos(
            int(self.level)
        )

    def explain(self):
        # Just for testing
        if self.level == 3.5:
            self.level = 5
            self.last_level_completed += 2
            return
        if self.bg is None:
            self.bg = pygame.image.load(random.choice(VisualizationService.get_explain_backgrounds()))
        VisualizationService.draw_explain_bg(
            self.bg
        )
        VisualizationService.draw_explain_box(
            self.level + 0.5
        )

    def play_harvest(self):
        global sprites, time, wheat_positions
        time += 1

        # drawing
        VisualizationService.draw_harvest_level(
            GlobalState.SCREEN
        )
        VisualizationService.draw_wheat_score(
            wheats=self.wheatsCollected,
            y=10
        )
        for wheat in sprites:
            wheat.draw()

        # Wheat spawn mechanism
        if time == INTERVAL_BETWEEN_WHEAT_SPAWNS:
            position = random.choice(wheat_positions)
            sprites.empty()
            sprites.add(
                Wheat(
                    position=position,
                    wheat_to_end_harvest=WHEAT_TO_END_HARVEST
                )
            )
            GlobalState.music.play_wheat_grow_sound()
            time = 0

    @staticmethod
    def add_crash_wheat():
        position = (random.randint(750, 1350), 30)
        spritesSecondary.add(
            CrashWheat(
                position=position,
                wheat_to_end_harvest=WHEAT_TO_END_HARVEST
            )
        )

    @staticmethod
    def send_flour():
        sprites.add(FlourBox((1286, 693)))

    def play_crash(self):
        # drawing
        VisualizationService.draw_crash_level(
            GlobalState.SCREEN
        )
        VisualizationService.draw_flour_score(
            score=self.flourCollected
        )
        for flour in sprites:
            flour.draw()
        for wheat in spritesSecondary:
            wheat.draw()
        # Check if next level
        if self.flourCollected == FLOURS_TO_COLLECT_ON_CRASH:
            self.finishLevel()
            return
        # Check lose
        if self.crash_wheat_added == WHEAT_TO_END_HARVEST:
            if (
                    not self.last_succeed
                    and not self.flourCollected == FLOURS_TO_COLLECT_ON_CRASH
            ):
                self.deathMsg = Reasons.wheatCrashOver
                GlobalState.GAME_STATE = GameStatus.GAME_FAILED
        # On start of level
        elif len(spritesSecondary) == 0:
            self.add_crash_wheat()
        # Score
        VisualizationService.draw_wheat_score(
            wheats=9 - self.crash_wheat_added, y=150
        )

    def play_watering(self):
        global time, mixer

        # Check if next level
        if self.doughCollected == DOUGH_TO_COLLECT_ON_WATERING:
            self.finishLevel()
            return

        # Check lose
        if self.water_flours_added == FLOURS_TO_COLLECT_ON_CRASH + 1:  # Adding 1 because of the flour box sending mechanism
            self.deathMsg = Reasons.flourBoxesOver
            GlobalState.GAME_STATE = GameStatus.GAME_FAILED

        # Drawing
        VisualizationService.draw_watering_bg()
        if len(sprites) == 0:
            mixer = Mixer()
            sprites.add(mixer)

        mixer.draw()

        for sprite in spritesSecondary:
            sprite.draw()
        for sprite in spritesThird:
            sprite.draw()

        if self.water_flours_added < 8 and not self.last_succeed:
            if time == 80:
                spritesSecondary.add(
                    WaterFlourBox()
                )
                time = 0
        # When made dough
        if mixer.check_collision(spritesSecondary):
            spritesThird.add(
                Dough((mixer.rect.centerx, mixer.rect.bottom + 10))
            )
            if self.water_flours_added == 7:
                self.last_succeed = True

        # Score
        VisualizationService.draw_flour_score(
            score=8 - self.water_flours_added,
        )

        VisualizationService.draw_dough_score(
            score=self.doughCollected,
            y=160
        )
        time += 1

    def play_rolling(self):
        pass

    def play_cooking(self):
        global time
        VisualizationService.draw_oven_bg()

        if self.matzaCollected == 3:
            self.nextLevel()
            return

        if self.matzaCollected == -3:
            self.deathMsg = Reasons.wrongMatzot
            GlobalState.GAME_STATE = GameStatus.GAME_FAILED
            return

        if len(sprites) == 0:
            time += 1
            if time == 10:
                time = 0
                sprites.add(Matza())

        for sprite in sprites:
            sprite.draw()

        VisualizationService.draw_matza_score(self.matzaCollected)

    def nextLevel(self):
        global time, sprites, spritesSecondary, spritesThird
        if self.level <= self.last_level_completed:
            self.bg = None
            time = 0
            sprites.empty()
            spritesSecondary.empty()
            spritesThird.empty()
            self.level += 0.5
            self.last_succeed = False
            if not self.level % 1 == 0:
                GlobalState.TIMER.ticking = False
            else:
                GlobalState.TIMER.ticking = True

    def finishGame(self):
        global saved
        VisualizationService.draw_win_screen(GlobalState.TIMER.fixedTime)
        if not saved:
            saved = True
            ScoreService.update_max_score(
                GlobalState.TIMER.time
            )
        self.reset()

    def failed(self):
        if self.level != 0.5:
            GlobalState.music.play_end_sound()
            self.reset()

    def reset(self):
        if self.level != 0.5:
            global time, sprites, spritesSecondary, spritesThird, saved
            time = 0
            sprites.empty()
            spritesSecondary.empty()
            spritesThird.empty()
            self.level = 0.5
            self.crash_wheat_added = 0
            self.wheatsCollected = 0
            self.flourCollected = 0
            self.bg = None
            saved = False
            self.pause = False
            self.last_succeed = False
            self.water_flours_added = 1
            self.doughCollected = 0
            self.matzaCollected = 0
            GlobalState.TIMER.resetTimer()

    @staticmethod
    def retry():
        GlobalState.GAME = Game()
        GlobalState.GAME.level = 0.5
        GlobalState.GAME.last_level_completed += 0.5
        GlobalState.GAME_STATE = GameStatus.GAMEPLAY

    def finishLevel(self):
        self.last_level_completed += 1
        self.nextLevel()
