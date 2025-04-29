import pygame
from constants import MP3_LOCATION

pygame.mixer.music.load(MP3_LOCATION + 'HGSS - Pewter City.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=-1)
pop = pygame.mixer.Sound(MP3_LOCATION + 'pop.mp3')
yip = pygame.mixer.Sound(MP3_LOCATION + 'yippee.mp3')
bye = pygame.mixer.Sound(MP3_LOCATION + 'roblox-bye.mp3')
che = pygame.mixer.Sound(MP3_LOCATION + 'children-cheering.mp3')
cor = pygame.mixer.Sound(MP3_LOCATION + 'correct.mp3')
pip = pygame.mixer.Sound(MP3_LOCATION + 'metal-pipe-clang.mp3')
pop.set_volume(.1)
yip.set_volume(.1)
bye.set_volume(.1)
che.set_volume(.1)
cor.set_volume(.1)
pip.set_volume(.05)

def toggle_mute(is_muted):
  if is_muted:
    pop.set_volume(.1)
    yip.set_volume(.1)
    bye.set_volume(.1)
    che.set_volume(.1)
    cor.set_volume(.1)
    pip.set_volume(.05)
  else:
    pop.set_volume(0)
    yip.set_volume(0)
    bye.set_volume(0)
    che.set_volume(0)
    cor.set_volume(0)
    pip.set_volume(0)