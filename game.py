import random
import pygame
# hi!
from src.components.harvest.wheat import Wheat
from src.components.crash.crash_wheat import CrashWheat
from src.game_status import GameStatus
from src.global_state import GlobalState
from src.services.music_service import MusicService
from src.services.visualization_service import VisualizationService
from src.tools import is_close_app_event
from src.components.crash.flourBox import FlourBox
from src.components.watering.flourBox import WaterFlourBox
from src.components.watering.mixer import Mixer
from src.components.watering.dough import Dough


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


class Game:

    def __init__(self):
        self.level = 3
        self.crash_wheat_added = 0
        self.wheatsCollected = 0
        self.flourCollected = 0
        self.bg = None
        self.last_succeed = False
        self.water_flours_added = 1
        self.doughCollected = 0

    def finishLevel(self):
        self.nextLevel()

    def playLevel(self):
        if self.level == 1:
            self.play_harvest()
        elif self.level == 2:
            self.play_crash()
        elif self.level == 3:
            self.play_watering()
        elif self.level == 4:
            self.play_rolling()
        elif self.level == 5:
            self.play_cooking()
        else:
            self.explain()
        if self.level % 1 == 0:
            GlobalState.timer.update()
            GlobalState.timer.showTime(GlobalState.SCREEN)
            if GlobalState.timer.fixedTime == "18:00":
                GlobalState.GAME_STATE = GameStatus.GAME_END

    def explain(self):
        if self.bg is None:
            self.bg = pygame.image.load(random.choice(VisualizationService.get_explain_backgrounds()))
        VisualizationService.draw_explain_bg(self.bg)
        VisualizationService.draw_explain_box(self.level + 0.5)

    def play_harvest(self):
        global sprites, time, wheat_positions
        for event in pygame.event.get():
            if is_close_app_event(event):
                GlobalState.GAME_STATE = GameStatus.GAME_END
            for wheat in sprites:
                wheat.handle_event(event)

        # drawing
        VisualizationService.draw_harvest_level(GlobalState.SCREEN)
        VisualizationService.draw_wheat_score(self.wheatsCollected, 10)
        for wheat in sprites:
            wheat.draw()
        time += 1
        # Wheat spawn mechanism
        if time == 15:
            position = random.choice(wheat_positions)
            sprites.empty()
            sprites.add(
                Wheat(
                    position
                )
            )
            MusicService.play_wheat_grow_sound()
            time = 0

    @staticmethod
    def add_crash_wheat(): spritesSecondary.add(CrashWheat((random.randint(750, 1350), 30)))

    @staticmethod
    def send_flour(): sprites.add(FlourBox((1286, 693)))

    def play_crash(self):
        for event in pygame.event.get():
            if is_close_app_event(event):
                GlobalState.GAME_STATE = GameStatus.GAME_END
            for flour in sprites:
                flour.handle_event(event)
            for wheat in spritesSecondary:
                wheat.handle_event(event)

        # drawing
        VisualizationService.draw_crash_level(GlobalState.SCREEN)
        VisualizationService.draw_flour_score(
            self.flourCollected
        )
        # Visual points where the crash wheat need to touch:
        rect = pygame.Rect(
            0, 0, 4, 4
        )
        rect.center = (1025, 460)
        pygame.draw.rect(GlobalState.SCREEN, (255, 255, 255), rect, 4)
        rect.center = (995, 460)
        pygame.draw.rect(GlobalState.SCREEN, (255, 255, 255), rect, 4)

        for flour in sprites:
            flour.setPressed()
            flour.draw()
        for wheat in spritesSecondary:
            wheat.draw()

        if self.flourCollected >= 7:
            self.nextLevel()

        if self.crash_wheat_added > 9:
            if not self.last_succeed:
                GlobalState.GAME_STATE = GameStatus.GAME_END

        elif len(spritesSecondary) == 0:
            self.add_crash_wheat()
            self.crash_wheat_added += 1

        VisualizationService.draw_wheat_score(
            10 - self.crash_wheat_added,
            y= 150
        )

    def play_watering(self):
        global time, mixer
        for event in pygame.event.get():
            if is_close_app_event(event):
                GlobalState.GAME_STATE = GameStatus.GAME_END
            for sprite in spritesThird:
                sprite.handle_event(event)

        VisualizationService.draw_watering_bg()
        if len(sprites) == 0:
            mixer = Mixer()
            sprites.add(mixer)

        time += 1
        if self.water_flours_added < 8:
            if time == 80:
                spritesSecondary.add(
                    WaterFlourBox()
                )
                time = 0
                self.water_flours_added += 1

        mixer.draw()
        for sprite in spritesSecondary:
            sprite.draw()
        for sprite in spritesThird:
            sprite.draw()

        if mixer.check_collision(spritesSecondary):
            spritesThird.add(
                Dough((mixer.rect.centerx, mixer.rect.bottom + 10))
            )

        VisualizationService.draw_flour_score(
            score=8 - self.water_flours_added,
        )

        VisualizationService.draw_dough_score(
            score=self.doughCollected,
            y=160
        )

    def play_rolling(self):
        pass

    def play_cooking(self):
        pass

    def nextLevel(self):
        global time, sprites, spritesSecondary, spritesThird
        self.bg = None
        time = 0
        sprites.empty()
        spritesSecondary.empty()
        spritesThird.empty()
        self.level += 0.5
        if not self.level % 1 == 0:
            GlobalState.timer.pauseTimer()
        else:
            GlobalState.timer.continueTimer()
