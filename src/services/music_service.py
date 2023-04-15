import random

import pygame

from paths import AUDIO_DIR


class MusicService:
    @staticmethod
    def get_background_musics():
        return [
            AUDIO_DIR / "backgrond_music.MP3",
        ]

    @staticmethod
    def get_chop_musics():
        return [
            AUDIO_DIR / "chop.wav",
            AUDIO_DIR / "chop_2.wav",
            AUDIO_DIR / "chop_3.wav"
        ]

    @staticmethod
    def get_cheer_musics():
        return [
            AUDIO_DIR / "cheer.wav",
            AUDIO_DIR / "cheer_2.wav",
            AUDIO_DIR / "cheer_3.wav",
            AUDIO_DIR / "cheer_4.wav"
        ]

    @staticmethod
    def start_background_music():
        if pygame.mixer.music.get_busy():
            return

        musics = MusicService.get_background_musics()
        filename = random.choice(musics)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

    @staticmethod
    def play_chop_sound():
        musics = MusicService.get_chop_musics()
        filename = random.choice(musics)
        chop = pygame.mixer.Sound(filename)
        pygame.mixer.Sound.play(chop)

    @staticmethod
    def play_success_sound():
        score_sfx = pygame.mixer.Sound(AUDIO_DIR / "success.mp3")
        pygame.mixer.Sound.play(score_sfx)

    @staticmethod
    def play_flour_pick_up_sound():
        sfx = pygame.mixer.Sound(AUDIO_DIR / "flour pickup.mp3")
        pygame.mixer.Sound.play(sfx)

    @staticmethod
    def play_click_sound():
        click_sfx = pygame.mixer.Sound(AUDIO_DIR / "click.mp3")
        pygame.mixer.Sound.play(click_sfx)

    @staticmethod
    def play_fail_sound():
        crash_sfx = pygame.mixer.Sound(AUDIO_DIR / "fail.mp3")
        pygame.mixer.Sound.play(crash_sfx)

    @staticmethod
    def play_cheer_sound():
        musics = MusicService.get_cheer_musics()
        filename = random.choice(musics)
        cheer = pygame.mixer.Sound(filename)
        pygame.mixer.Sound.play(cheer)

    @staticmethod
    def play_wheat_grow_sound():
        sfx = pygame.mixer.Sound(AUDIO_DIR / "wheat_grow.mp3")
        pygame.mixer.Sound.play(sfx)

    @staticmethod
    def play_wheat_break_sound():
        sfx = pygame.mixer.Sound(AUDIO_DIR/ "wheat-break.ogg")
        pygame.mixer.Sound.play(sfx)