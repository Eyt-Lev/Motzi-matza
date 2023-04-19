import pygame

from paths import AUDIO_DIR

enabled = True


class MusicService:

    @staticmethod
    def start_background_music():
        if enabled:
            try:
                if pygame.mixer.music.get_busy():
                    return

                filename = MusicService.get_background_music()
                pygame.mixer.music.load(filename)
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play(-1)
            except pygame.error:
                pass

    @staticmethod
    def play_success_sound():
        if enabled:
            try:
                score_sfx = pygame.mixer.Sound(AUDIO_DIR / "success.mp3")
                pygame.mixer.Sound.play(score_sfx)
            except pygame.error:
                pass

    @staticmethod
    def play_flour_pick_up_sound():
        if enabled:
            try:
                sfx = pygame.mixer.Sound(AUDIO_DIR / "flour pickup.mp3")
                pygame.mixer.Sound.play(sfx)
            except pygame.error:
                pass

    @staticmethod
    def play_click_sound():
        if enabled:
            try:
                click_sfx = pygame.mixer.Sound(AUDIO_DIR / "click.mp3")
                pygame.mixer.Sound.play(click_sfx)
            except pygame.error:
                pass

    @staticmethod
    def play_fail_sound():
        if enabled:
            try:
                fail_sfx = pygame.mixer.Sound(AUDIO_DIR / "fail.mp3")
                pygame.mixer.Sound.play(fail_sfx)
            except pygame.error:
                pass

    @staticmethod
    def play_wheat_grow_sound():
        if enabled:
            try:
                sfx = pygame.mixer.Sound(AUDIO_DIR / "wheat_grow.mp3")
                pygame.mixer.Sound.play(sfx)
            except pygame.error:
                pass

    @staticmethod
    def play_wheat_break_sound():
        if enabled:
            try:
                sfx = pygame.mixer.Sound(AUDIO_DIR / "wheat-break.ogg")
                pygame.mixer.Sound.play(sfx)
            except pygame.error:
                pass

    @staticmethod
    def play_end_sound():
        if enabled:
            try:
                sfx = pygame.mixer.Sound(AUDIO_DIR / "end.mp3")
                pygame.mixer.Sound.play(sfx)
            except pygame.error:
                pass

    @staticmethod
    def get_background_music():
        return AUDIO_DIR / "backgrond_music.MP3"
