import pygame
import pygame.freetype

from paths import IMAGES_DIR, FONT_DIR, EXPLAIN_DIR
from src.components.button import Button
from src.game_status import GameStatus
from src.global_state import GlobalState
from src.services.music_service import MusicService
from src.tools import sine, is_close_app_event
from config import Config


class VisualizationService:
    GlobalState.load_main_screen()

    # Main menu
    @staticmethod
    def load_main_game_displays():
        pygame.display.set_caption("Motzi Matza")
        # title = VisualizationService.get_player_image()
        # pygame.display.set_icon(title)

    @staticmethod
    def draw_main_menu_background(screen):
        title = VisualizationService.get_main_menu_background()
        rect = title.get_rect()
        rect.top, rect.left = (0, 0)
        screen.blit(title, rect)

    @staticmethod
    def draw_moving_logo(screen):
        logo = VisualizationService.get_logo()
        y = sine(200.0, 12680, 10.0, 70)
        screen.blit(logo, (530, y))

    @staticmethod
    def draw_main_menu_start_btn(onClick):
        btn = Button(
            GlobalState.SCREEN, x=977, y=580,
            img=VisualizationService.get_main_menu_start_btn(),
            hoverImage=VisualizationService.get_main_menu_start_btn_hovered(),
            onclickFunction=onClick,
            onHoverFunction=VisualizationService.on_btns_hover
        )
        for event in pygame.event.get():
            if is_close_app_event(event):
                GlobalState.GAME_STATE = GameStatus.GAME_END
            btn.handleEvent(event)

        btn.draw()

    @staticmethod
    def draw_main_menu(screen, onClick):
        screen.fill((255, 255, 255))
        VisualizationService.draw_main_menu_background(screen)
        VisualizationService.draw_moving_logo(screen)
        VisualizationService.draw_main_menu_start_btn(onClick)

    @staticmethod
    def draw_explain_box(level):
        box = VisualizationService.get_explain_box_image()
        rect = box.get_rect()
        rect.center = Config.WIDTH / 2, Config.HEIGHT / 2
        GlobalState.SCREEN.blit(box, rect)
        text = VisualizationService.get_explains(int(level))
        GlobalState.SCREEN.blit(text, text.get_rect())
        VisualizationService.draw_explain_box_btn()

    @staticmethod
    def draw_explain_box_btn():
        btn = Button(
            x=960, y=541, screen=GlobalState.SCREEN,
            img=VisualizationService.get_explain_box_btn(),
            hoverImage=VisualizationService.get_explain_box_btn_hovered(),
            onHoverFunction=VisualizationService.on_btns_hover,
            onclickFunction=GlobalState.game.nextLevel,
            onePress=True
        )
        for event in pygame.event.get():
            if is_close_app_event(event):
                GlobalState.GAME_STATE = GameStatus.GAME_END
            btn.handleEvent(event)
        btn.draw()

    @staticmethod
    def draw_explain_bg(bg):
        rect = bg.get_rect()
        rect.top, rect.left = (0, 0)
        GlobalState.SCREEN.blit(bg, rect)

    # harvest
    @staticmethod
    def draw_harvest_level(screen):
        bg = VisualizationService.get_harvest_level_bg()
        screen.blit(bg, bg.get_rect())

    @staticmethod
    def draw_crash_level(screen):
        bg = VisualizationService.get_crash_level_background()
        screen.blit(bg, bg.get_rect())

    @staticmethod
    def draw_score_background(y):
        bg = VisualizationService.get_score_background()
        rect = bg.get_rect()
        rect.top, rect.right = y, 1920
        GlobalState.SCREEN.blit(bg, rect)

    @staticmethod
    def draw_wheat_score(wheats, y):
        VisualizationService.draw_score_background(y)
        wheat = VisualizationService.get_wheat_score_image()
        rect = wheat.get_rect()
        rect.topright = (1900, y + 25)
        GlobalState.SCREEN.blit(wheat, rect)
        font = VisualizationService.get_mc_font()
        font.render_to(
            GlobalState.SCREEN, (1760, y + 30),
            str(wheats),
            (0, 0, 0), None, size=80
        )

    @staticmethod
    def draw_flour_score(score, y=30):
        VisualizationService.draw_score_background(10)
        flour = VisualizationService.get_flour_score_image()
        rect = flour.get_rect()
        rect.topright = (1900, y)
        GlobalState.SCREEN.blit(flour, rect)
        font = VisualizationService.get_mc_font()
        font.render_to(
            GlobalState.SCREEN, (1760, y + 10),
            str(score),
            (0, 0, 0), None, size=80
        )

    @staticmethod
    def draw_dough_score(score, y=30):
        VisualizationService.draw_score_background(y-15)
        dough = VisualizationService.get_dough_image()
        rect = dough.get_rect()
        rect.topright = (1900, y)
        GlobalState.SCREEN.blit(dough, rect)
        font = VisualizationService.get_mc_font()
        font.render_to(
            GlobalState.SCREEN, (1760, y + 10),
            str(score),
            (0, 0, 0), None, size=80
        )

    @staticmethod
    def draw_crash_wheat_handler(x):
        handler = VisualizationService.get_crash_wheat_handler_image()
        rect = handler.get_rect()
        rect.centerx, rect.top = x, 0
        GlobalState.SCREEN.blit(handler, rect)

    @staticmethod
    def draw_watering_bg():
        bg = VisualizationService.get_watering_bg_image()
        GlobalState.SCREEN.blit(bg, bg.get_rect())

    # Other
    @staticmethod
    def get_logo():
        return pygame.image.load(IMAGES_DIR / "logo.png").convert_alpha()

    @staticmethod
    def get_main_menu_start_btn_hovered():
        return pygame.image.load(IMAGES_DIR / "start screen btn hoverd.png").convert_alpha()

    @staticmethod
    def get_main_menu_start_btn():
        return pygame.image.load(IMAGES_DIR / "start screen btn.png").convert_alpha()

    @staticmethod
    def on_btns_hover():
        MusicService.play_click_sound()

    @staticmethod
    def get_main_menu_background():
        return pygame.image.load(IMAGES_DIR / "start_screen_bg.png").convert()

    @staticmethod
    def get_crash_wheat_handler_image():
        return pygame.image.load(IMAGES_DIR / "crash_wheat_handler.png").convert_alpha()

    @staticmethod
    def get_harvest_level_bg():
        return pygame.image.load(IMAGES_DIR / "harvest_lvl_bg.png").convert_alpha()

    @staticmethod
    def get_wheat_image():
        return pygame.image.load(IMAGES_DIR / "wheat.png").convert_alpha()

    @staticmethod
    def get_score_background():
        return pygame.image.load(IMAGES_DIR / "score_bg.png").convert_alpha()

    @staticmethod
    def get_wheat_score_image():
        return pygame.image.load(IMAGES_DIR / "wheat_score.png").convert_alpha()

    @staticmethod
    def get_flour_score_image():
        return pygame.image.load(IMAGES_DIR / "flour_score.png").convert_alpha()

    @staticmethod
    def get_explain_box_image():
        return pygame.image.load(EXPLAIN_DIR / "explain box.png").convert_alpha()

    @staticmethod
    def get_explain_box_btn():
        return pygame.image.load(EXPLAIN_DIR / "next btn.png").convert_alpha()

    @staticmethod
    def get_watering_bg_image():
        return pygame.image.load(IMAGES_DIR / "watering_bg.png").convert()

    @staticmethod
    def get_explain_box_btn_hovered():
        return pygame.image.load(EXPLAIN_DIR / "next btn hovered.png").convert_alpha()

    @staticmethod
    def get_font():
        return pygame.freetype.Font(FONT_DIR / "HEEBO-BLACK.ttf", 20)

    @staticmethod
    def get_mc_font():
        return pygame.freetype.Font(FONT_DIR / "Minecraft.ttf", 20)

    @staticmethod
    def get_explain_backgrounds():
        return [
            EXPLAIN_DIR / "bg1.png",
            EXPLAIN_DIR / "bg2.png",
            EXPLAIN_DIR / "bg3.png",
            EXPLAIN_DIR / "bg4.png",
        ]

    @staticmethod
    def get_explains(level):
        return pygame.image.load(EXPLAIN_DIR / f"ex{level}.png").convert_alpha()

    @staticmethod
    def get_flour_box_img():
        return pygame.image.load(IMAGES_DIR / "flour box.png").convert_alpha()

    @staticmethod
    def get_crash_level_background():
        return pygame.image.load(IMAGES_DIR / "crash_lvl_bg.png").convert_alpha()

    @staticmethod
    def get_mixer_images():
        return [
            pygame.image.load(IMAGES_DIR / "mixerTop.png").convert_alpha(),
            pygame.image.load(IMAGES_DIR / "mixerBottom.png").convert_alpha()
        ]

    @staticmethod
    def get_dough_image():
        return pygame.image.load(IMAGES_DIR / "dough.png").convert_alpha()
