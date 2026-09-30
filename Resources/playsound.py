from pathlib import Path
import pygame

pygame.mixer.init()

sounds_dir = Path(__file__).resolve().parent / "sounds"
cooljune = pygame.mixer.Sound(str(sounds_dir / "cooljune452-horror-game-ambiance-292952.mp3"))
tanweraman = pygame.mixer.Sound(str(sounds_dir / "tanweraman-dripping-water-stereo-sound-257182.mp3"))

cooljune.set_volume(0.25)
tanweraman.set_volume(0.50)

pygame.mixer.set_num_channels(3)
cooljune_channel = pygame.mixer.Channel(0)
tanweraman_channel = pygame.mixer.Channel(1)
sfx_channel = pygame.mixer.Channel(2)
_active_sfx = None


def stop_horror_background_music():
    """Stop the looping CoolJune and Tanweraman background tracks."""
    cooljune_channel.stop()
    tanweraman_channel.stop()


def play_horror_sfx(filename="freesound_community-horror-sfx-3-103708.mp3", volume=0.5):
    """Play one sound effect once; relative filenames are inside the sounds folder."""
    global _active_sfx

    sound_file = Path(filename)
    if not sound_file.is_absolute():
        sound_file = sounds_dir / sound_file
    if not sound_file.is_file():
        raise FileNotFoundError(f"Sound effect not found: {sound_file}")
    if not 0.0 <= volume <= 1.0:
        raise ValueError("volume must be between 0.0 and 1.0")

    _active_sfx = pygame.mixer.Sound(str(sound_file))
    _active_sfx.set_volume(volume)
    sfx_channel.play(_active_sfx)
    return sfx_channel


cooljune_channel.play(cooljune, loops=-1)
tanweraman_channel.play(tanweraman, loops=-1)

if __name__ == "__main__":
    try:
        while True:
            pygame.time.wait(1000)
    except KeyboardInterrupt:
        pygame.mixer.stop()
        pygame.quit()
