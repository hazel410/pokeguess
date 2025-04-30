import pygame
import asyncio
import constants as c

if c.RUNNING_LOCALLY:
  file_extension = '.mp3'
else:
  file_extension = '-pygbag.ogg'

class SFX:
  def __init__(self):
    pygame.mixer.music.load(c.MP3_LOCATION + 'HGSS - Pewter City' + file_extension)
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loops=-1)
    self.pop = pygame.mixer.Sound(c.MP3_LOCATION + 'pop' + file_extension)
    self.yip = pygame.mixer.Sound(c.MP3_LOCATION + 'yippee' + file_extension)
    self.bye = pygame.mixer.Sound(c.MP3_LOCATION + 'roblox-bye' + file_extension)
    self.che = pygame.mixer.Sound(c.MP3_LOCATION + 'children-cheering' + file_extension)
    self.cor = pygame.mixer.Sound(c.MP3_LOCATION + 'correct' + file_extension)
    self.pip = pygame.mixer.Sound(c.MP3_LOCATION + 'metal-pipe-clang' + file_extension)
    self.pop.set_volume(.1)
    self.yip.set_volume(.1)
    self.bye.set_volume(.1)
    self.che.set_volume(.1)
    self.cor.set_volume(.1)
    self.pip.set_volume(.05)

  def toggle_mute(self, is_muted):
    if is_muted:
      self.pop.set_volume(.1)
      self.yip.set_volume(.1)
      self.bye.set_volume(.1)
      self.che.set_volume(.1)
      self.cor.set_volume(.1)
      self.pip.set_volume(.05)
    else:
      self.pop.set_volume(0)
      self.yip.set_volume(0)
      self.bye.set_volume(0)
      self.che.set_volume(0)
      self.cor.set_volume(0)
      self.pip.set_volume(0)