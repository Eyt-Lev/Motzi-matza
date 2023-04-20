import pygame

from paths import AUDIO_DIR


class MusicService:

    def __init__(self):
        self.musicEnabled = True
        self.soundEnabled = True

    def start_background_music(self):
        if self.musicEnabled:
            try:
                if pygame.mixer.music.get_busy():
                    return

                filename = MusicService.get_background_music()
                pygame.mixer.music.load(filename)
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play(-1)
            except pygame.error:
                pass
        else:
            pygame.mixer.music.stop()

    def play_success_sound(self):
        if self.soundEnabled:
            try:
                score_sfx = pygame.mixer.Sound(AUDIO_DIR / "success.mp3")
                pygame.mixer.Sound.play(score_sfx)
            except pygame.error:
                pass

    def play_flour_pick_up_sound(self):
        if self.soundEnabled:
            try:
                sfx = pygame.mixer.Sound(AUDIO_DIR / "flour pickup.mp3")
                pygame.mixer.Sound.play(sfx)
            except pygame.error:
                pass

    def play_click_sound(self):
        if self.soundEnabled:
            try:
                click_sfx = pygame.mixer.Sound(AUDIO_DIR / "click.mp3")
                pygame.mixer.Sound.play(click_sfx)
            except pygame.error:
                pass

    def play_fail_sound(self):
        if self.soundEnabled:
            try:
                fail_sfx = pygame.mixer.Sound(AUDIO_DIR / "fail.mp3")
                pygame.mixer.Sound.play(fail_sfx)
            except pygame.error:
                pass

    def play_wheat_grow_sound(self):
        if self.soundEnabled:
            try:
                sfx = pygame.mixer.Sound(AUDIO_DIR / "wheat_grow.mp3")
                pygame.mixer.Sound.play(sfx)
            except pygame.error:
                pass

    def play_wheat_break_sound(self):
        if self.soundEnabled:
            try:
                sfx = pygame.mixer.Sound(AUDIO_DIR / "wheat-break.ogg")
                pygame.mixer.Sound.play(sfx)
            except pygame.error:
                pass

    def play_end_sound(self):
        if self.soundEnabled:
            try:
                sfx = pygame.mixer.Sound(AUDIO_DIR / "end.mp3")
                pygame.mixer.Sound.play(sfx)
            except pygame.error:
                pass

    @staticmethod
    def get_background_music():
        return AUDIO_DIR / "backgrond_music.MP3"
