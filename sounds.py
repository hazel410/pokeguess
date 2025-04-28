import pygame
from constants import ROOTDIR
pygame.mixer.music.load(ROOTDIR + 'files/mps/HGSS - Pewter City.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(loops=-1)
pop = pygame.mixer.Sound(ROOTDIR + 'files/mps/pop.mp3')
yip = pygame.mixer.Sound(ROOTDIR + 'files/mps/yippee.mp3')
bye = pygame.mixer.Sound(ROOTDIR + 'files/mps/roblox-bye.mp3')
che = pygame.mixer.Sound(ROOTDIR + 'files/mps/children-cheering.mp3')
cor = pygame.mixer.Sound(ROOTDIR + 'files/mps/correct.mp3')
pip = pygame.mixer.Sound(ROOTDIR + 'files/mps/metal-pipe-clang.mp3')
pop.set_volume(.1)
yip.set_volume(.1)
bye.set_volume(.1)
che.set_volume(.1)
cor.set_volume(.1)
pip.set_volume(.05)
mute = False