import pygame
import pygame.freetype

from config import Config
from paths import IMAGES_DIR, FONT_DIR, EXPLAIN_DIR
from src.components.button import Button
from src.game_status import GameStatus
from src.global_state import GlobalState
from src.services.score_service import ScoreService
from src.services.timer_service import TimerService
from src.tools import sine

en = False


def goHome():
    GlobalState.GAME_STATE = GameStatus.MAIN_MENU
    GlobalState.GAME.reset()


def change_lang():
    global en
    en = not en


def change_music():
    GlobalState.music.musicEnabled = not GlobalState.music.musicEnabled


def change_sound():
    GlobalState.music.soundEnabled = not GlobalState.music.soundEnabled


class VisualizationService:
    GlobalState.load_main_screen()

    @staticmethod
    def draw_main_menu(screen, onClick):
        screen.fill((255, 255, 255))
        # Background
        title = VisualizationService.get_main_menu_background()
        rect = title.get_rect()
        rect.top, rect.left = (0, 0)
        screen.blit(title, rect)
        # Moving logo
        logo = VisualizationService.get_logo()
        y = sine(200.0, 12680, 10.0, 140)
        screen.blit(logo, (640, y))
        # Best score
        bestScore = TimerService.get_fixedTime(
            ScoreService.get_max_score()
        )
        if bestScore == "0:00":
            bestScore = "You don't have best score"
        else:
            bestScore = "Best Score: " + bestScore
        text, textRect = VisualizationService.get_mc_font().render(
            bestScore,
            (255, 255, 255),
            size=40
        )
        textRect.center = (1005, 580)
        screen.blit(text, textRect)
        # Buttons
        mainMenuStartBtn.onclickFunction = onClick

        mainMenuLangBtn.img, mainMenuLangBtn.hoverImage = VisualizationService.get_lang_image()
        mainMenuMusicBtn.img, mainMenuMusicBtn.hoverImage = VisualizationService.get_music_btn_image()
        mainMenuNoteBtn.img, mainMenuNoteBtn.hoverImage = VisualizationService.get_note_btn_image()

        btns = [mainMenuStartBtn, mainMenuLangBtn, mainMenuMusicBtn, mainMenuNoteBtn]

        for btn in btns:
            if btn is not mainMenuStartBtn:
                btn.originalImg = btn.img
            btn.draw()

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
        explainBoxNextBtn.onclickFunction = GlobalState.GAME.nextLevel
        explainBoxNextBtn.draw()

    @staticmethod
    def draw_explain_bg(bg):
        rect = bg.get_rect()
        rect.top, rect.left = (0, 0)
        GlobalState.SCREEN.blit(bg, rect)

    @staticmethod
    def draw_pause_btn():
        pauseBtn.draw()

    @staticmethod
    def draw_pos(level):
        bg = pygame.image.load(VisualizationService.get_explain_backgrounds()[level])
        GlobalState.SCREEN.blit(bg, bg.get_rect())
        bg = VisualizationService.get_pause_bg()
        GlobalState.SCREEN.blit(bg, bg.get_rect())
        GlobalState.TIMER.showTime(GlobalState.SCREEN)

        posMenuLangBtn.img, posMenuLangBtn.hoverImage = VisualizationService.get_lang_image()
        posMenuMusicBtn.img, posMenuMusicBtn.hoverImage = VisualizationService.get_music_btn_image()
        posMenuNoteBtn.img, posMenuNoteBtn.hoverImage = VisualizationService.get_note_btn_image()

        btns = [continueBtn, pauseScreenHomeBtn]
        controls = [posMenuLangBtn, posMenuMusicBtn, posMenuNoteBtn, ]

        for btn in btns:
            btn.draw()
        for btn in controls:
            btn.originalImg = btn.img
            btn.draw()

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
        VisualizationService.draw_score_background(y - 15)
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
    def draw_matza_score(score, y=30):
        VisualizationService.draw_score_background(y - 15)
        dough = VisualizationService.get_matza_image(3)
        rect = dough.get_rect()
        rect.topright = (1900, y + 6)
        GlobalState.SCREEN.blit(dough, rect)
        font = VisualizationService.get_mc_font()
        font.render_to(
            GlobalState.SCREEN, (1750, y + 10),
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

    @staticmethod
    def draw_oven_bg():
        bg = VisualizationService.get_oven_bg()
        GlobalState.SCREEN.blit(bg, bg.get_rect())

    @staticmethod
    def draw_win_screen(time):
        bg = VisualizationService.get_win_screen_image()
        GlobalState.SCREEN.blit(bg, bg.get_rect())
        endScreenHomeBtn.draw()
        VisualizationService.get_mc_font().render_to(
            GlobalState.SCREEN,
            (980, 530), time,
            (0, 0, 0),
            size=80
        )

    @staticmethod
    def draw_end_screen(reason):
        screen = GlobalState.SCREEN
        VisualizationService.draw_end_screen_background(screen)
        VisualizationService.draw_end_screen_reason(screen, reason)
        VisualizationService.draw_end_screen_btn()

    @staticmethod
    def draw_end_screen_btn():
        endScreenRetryBtn.onclickFunction = GlobalState.GAME.retry
        endScreenRetryBtn.draw()
        endScreenHomeBtn.draw()

    @staticmethod
    def draw_end_screen_reason(screen, reason):
        pos = 0
        for line in reason:
            pos += 1
            VisualizationService.get_mc_font().render_to(
                screen,
                (Config.WIDTH / 2 - 80, Config.HEIGHT / 2 + 20 + (60 * pos)),
                line,
                (255, 255, 255),
                size=40
            )

    @staticmethod
    def draw_end_screen_background(screen):
        bg = VisualizationService.get_end_screen_image()
        screen.blit(bg, bg.get_rect())
        text = VisualizationService.get_end_screen_text()
        screen.blit(text, text.get_rect())

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
        GlobalState.music.play_click_sound()

    @staticmethod
    def get_end_btn_images():
        return [
            pygame.image.load(IMAGES_DIR / 'end_btn.png').convert_alpha(),
            pygame.image.load(IMAGES_DIR / 'end_btn_hovered.png').convert_alpha()
        ]

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
    def get_end_screen_text():
        return pygame.image.load(IMAGES_DIR / "failed_txt.png").convert_alpha()

    @staticmethod
    def get_win_screen_image():
        return pygame.image.load(IMAGES_DIR / "win_screen.png").convert_alpha()

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
    def get_mc_font():
        return pygame.freetype.Font(FONT_DIR / "Minecraft.ttf", 20)

    @staticmethod
    def get_matza_image(type):
        return pygame.image.load(IMAGES_DIR / f"matza_{type}.png").convert_alpha()

    @staticmethod
    def get_explain_backgrounds():
        return [
            EXPLAIN_DIR / "bg1.png",
            EXPLAIN_DIR / "bg2.png",
            EXPLAIN_DIR / "bg3.png",
            EXPLAIN_DIR / "bg4.png",
            EXPLAIN_DIR / "bg5.png",
            EXPLAIN_DIR / "bg7.png",
        ]

    @staticmethod
    def get_explains(level):
        global en
        if en:
            return pygame.image.load(EXPLAIN_DIR / f"ex{level}.png").convert_alpha()
        else:
            return pygame.image.load(EXPLAIN_DIR / f"אק{level}.png").convert_alpha()

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
    def get_home_btn_images():
        return [
            pygame.image.load(IMAGES_DIR / "home_btn.png").convert_alpha(),
            pygame.image.load(IMAGES_DIR / "home_btn_hovered.png").convert_alpha()
        ]

    @staticmethod
    def get_pause_btn_images():
        return [
            pygame.image.load(IMAGES_DIR / "pause_btn.png").convert_alpha(),
            pygame.image.load(IMAGES_DIR / "pause_btn_hovered.png").convert_alpha()
        ]

    @staticmethod
    def get_dough_image():
        return pygame.image.load(IMAGES_DIR / "dough.png").convert_alpha()

    @staticmethod
    def get_pause_bg():
        return pygame.image.load(IMAGES_DIR / "pause_bg.png").convert_alpha()

    @staticmethod
    def get_end_screen_image():
        return pygame.image.load(IMAGES_DIR / "end_bg.png").convert_alpha()

    @staticmethod
    def get_lang_image():
        if en:
            return [
                pygame.image.load(IMAGES_DIR / "lang-en.png").convert_alpha(),
                pygame.image.load(IMAGES_DIR / "lang-en-hovered.png").convert_alpha(),
            ]
        else:
            return [
                pygame.image.load(IMAGES_DIR / "lang-he.png").convert_alpha(),
                pygame.image.load(IMAGES_DIR / "lang-he-hovered.png").convert_alpha(),
            ]

    @staticmethod
    def get_music_btn_image():
        if GlobalState.music.musicEnabled:
            return [
                pygame.image.load(IMAGES_DIR / "music_btn.png").convert_alpha(),
                pygame.image.load(IMAGES_DIR / "music_btn-hovered.png").convert_alpha(),
            ]
        else:
            return [
                pygame.image.load(IMAGES_DIR / "music_btn_disabled.png").convert_alpha(),
                pygame.image.load(IMAGES_DIR / "music_btn_disabled_hovered.png").convert_alpha(),
            ]

    @staticmethod
    def get_note_btn_image():
        if GlobalState.music.soundEnabled:
            return [
                pygame.image.load(IMAGES_DIR / "note_btn.png").convert_alpha(),
                pygame.image.load(IMAGES_DIR / "note_btn_hovered.png").convert_alpha(),
            ]
        else:
            return [
                pygame.image.load(IMAGES_DIR / "note_btn_disabled.png").convert_alpha(),
                pygame.image.load(IMAGES_DIR / "note_btn_disabled_hovered.png").convert_alpha(),
            ]

    @staticmethod
    def get_oven_bg():
        return pygame.image.load(IMAGES_DIR / "5th_level_bg.png").convert()

    @staticmethod
    def get_continue_btn_images():
        return [
            pygame.image.load(IMAGES_DIR / "continue_btn.png").convert_alpha(),
            pygame.image.load(IMAGES_DIR / "continue_btn_hovered.png").convert_alpha(),
        ]


mainMenuStartBtn = Button(
    GlobalState.SCREEN, x=977, y=580,
    img=VisualizationService.get_main_menu_start_btn(),
    hoverImage=VisualizationService.get_main_menu_start_btn_hovered(),
    onHoverFunction=VisualizationService.on_btns_hover
)

langImg, langImgHover = VisualizationService.get_lang_image()
mainMenuLangBtn = Button(
    GlobalState.SCREEN, x=30, y=870,
    img=langImg, hoverImage=langImgHover,
    center=False, onHoverFunction=VisualizationService.on_btns_hover,
    onclickFunction=change_lang
)

musicImg, musicImgHovered = VisualizationService.get_music_btn_image()
mainMenuMusicBtn = Button(
    GlobalState.SCREEN, x=220, y=870,
    img=musicImg, hoverImage=musicImgHovered,
    center=False, onHoverFunction=VisualizationService.on_btns_hover,
    onclickFunction=change_music
)

noteImg, noteImgHovered = VisualizationService.get_note_btn_image()
mainMenuNoteBtn = Button(
    GlobalState.SCREEN, x=380, y=870,
    img=noteImg, hoverImage=noteImgHovered,
    center=False, onHoverFunction=VisualizationService.on_btns_hover,
    onclickFunction=change_sound
)

posMenuLangBtn = Button(
    GlobalState.SCREEN, x=480, y=670,
    img=langImg, hoverImage=langImgHover,
    center=False, onHoverFunction=VisualizationService.on_btns_hover,
    onclickFunction=change_lang
)

posMenuMusicBtn = Button(
    GlobalState.SCREEN, x=670, y=670,
    img=musicImg, hoverImage=musicImgHovered,
    center=False, onHoverFunction=VisualizationService.on_btns_hover,
    onclickFunction=change_music
)

posMenuNoteBtn = Button(
    GlobalState.SCREEN, x=830, y=670,
    img=noteImg, hoverImage=noteImgHovered,
    center=False, onHoverFunction=VisualizationService.on_btns_hover,
    onclickFunction=change_sound
)

explainBoxNextBtn = Button(
    x=960, y=541, screen=GlobalState.SCREEN,
    img=VisualizationService.get_explain_box_btn(),
    hoverImage=VisualizationService.get_explain_box_btn_hovered(),
    onHoverFunction=VisualizationService.on_btns_hover,
    onePress=True
)

img, hovered_img = VisualizationService.get_end_btn_images()
endScreenRetryBtn = Button(
    GlobalState.SCREEN,
    0, 0, img=img, hoverImage=hovered_img,
    center=False, onHoverFunction=VisualizationService.on_btns_hover,
)
img, hovered_img = VisualizationService.get_home_btn_images()

endScreenHomeBtn = Button(
    GlobalState.SCREEN, 130, 930, img=img, hoverImage=hovered_img,
    onHoverFunction=VisualizationService.on_btns_hover,
    onclickFunction=goHome
)

pauseScreenHomeBtn = Button(
    GlobalState.SCREEN, 1351, 776, img=img, hoverImage=hovered_img,
    onHoverFunction=VisualizationService.on_btns_hover,
    onclickFunction=goHome
)


def pauseGame():
    GlobalState.GAME.pause = True


def continue_game():
    GlobalState.GAME.pause = False


pauseBtnImg, pauseBtnImgHovered = VisualizationService.get_pause_btn_images()
pauseBtn = Button(
    GlobalState.SCREEN,
    380, 73.4, img=pauseBtnImg, hoverImage=pauseBtnImgHovered,
    onHoverFunction=VisualizationService.on_btns_hover,
    onclickFunction=pauseGame
)

continueBtnImg, continueBtnImgHovered = VisualizationService.get_continue_btn_images()
continueBtn = Button(
    GlobalState.SCREEN,
    566, 278, img=continueBtnImg, hoverImage=continueBtnImgHovered,
    onHoverFunction=VisualizationService.on_btns_hover,
    onclickFunction=continue_game
)
