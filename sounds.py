import pygame
from constants import MP3_LOCATION
from constants import RUNNING_LOCALLY

if RUNNING_LOCALLY:
  file_extension = '.mp3'
else:
  file_extension = '.ogg'

pygame.mixer.music.load(MP3_LOCATION + 'HGSS - Pewter City' + file_extension)
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(loops=-1)
pop = pygame.mixer.Sound(MP3_LOCATION + 'pop' + file_extension)
yip = pygame.mixer.Sound(MP3_LOCATION + 'yippee' + file_extension)
bye = pygame.mixer.Sound(MP3_LOCATION + 'roblox-bye' + file_extension)
che = pygame.mixer.Sound(MP3_LOCATION + 'children-cheering' + file_extension)
cor = pygame.mixer.Sound(MP3_LOCATION + 'correct' + file_extension)
pip = pygame.mixer.Sound(MP3_LOCATION + 'metal-pipe-clang' + file_extension)
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