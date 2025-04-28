import math
import numpy as np
import asyncio
import pygame
import time
import random
import pandas as pd
from PIL import Image

pygame.mixer.init()
pygame.init()

import constants as c
import sounds as sfx
import functions
import logic
import physics
import button

class MAIN():
  def __init__(self):
    # pygame stuffs
    if c.RUNNING_LOCALLY:
      self.screen = pygame.display.set_mode((c.WINDOW_WIDTH, c.WINDOW_HEIGHT), flags=pygame.SCALED, vsync=1)
    else:
      self.screen = pygame.display.set_mode((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))
    pygame.display.set_caption('PokéGuess V5')
    self.clock = pygame.time.Clock()
    
    # classes
    self.PHYSICS = physics.PHYSICS()
    self.GAME_LOGIC = logic.GAME_LOGIC()

    # loop vars
    self.reset_gamemode = False
    self.question_number = "Question: " + str(self.GAME_LOGIC.qnum)
    self.mon_number = "Pokémon Left: " + str(self.GAME_LOGIC.pnum)
    self.question_text = self.GAME_LOGIC.bque
    self.active_gif = functions.GIF()
    self.gamemode = 1
    self.active_buttons = []
    self.mouse = pygame.mouse.get_pos()
    self.fps = self.clock.get_fps()
    self.quit = False
    asyncio.run(self.main())

  async def main(self):
    while True:
      pygame.display.flip()
      self.clock.tick(60)
      self.mouse = pygame.mouse.get_pos()
      self.active_buttons = []
      self.screen.file(c.BACKGROUND_COLOR)
      self.fps = self.clock.get_fps()
      
      if self.gamemode == 1:
        self.handleHome()
      elif self.gamemode == 2:
        self.handleSettings()
      elif self.gamemode == 3:
        self.handleCredits()
      elif self.gamemode == 4:
        self.handleGameplay()
      elif self.gamemode == 5:
        self.handleRetry()
      
      if self.reset_gamemode and self.gamemode != 4:
        self.GAME_LOGIC = logic.GAME_LOGIC()
        self.reset_gamemode = False
      self.active_buttons.append(button.BUTTON("FPS: " + str(round(self.fps)), (50, 25, 72, 40), 0, font=c.FONT_24, back=False))
      self.active_buttons.append(button.BUTTON('Silly', (30, c.WINDOW_HEIGHT - 25, 50, 30), -3, font=c.FONT_18, hide=True))

      self.handleButtons()
      self.handlePhysics()
      if self.quit:
        return
      await asyncio.sleep(0)
  
  def handleHome(self):
    self.active_gif.render()
    self.active_buttons = [
      button.BUTTON("PokéGuess V4", (c.WINDOW_WIDTH / 2, 32, -1, -1), 0, back=False, font=c.FONT_40),
      button.BUTTON("Play", (c.WINDOW_WIDTH / 5, c.WINDOW_HEIGHT * (1 / 5) + 16, 160, 70), 4),
      button.BUTTON("Settings", (c.WINDOW_WIDTH / 5, c.WINDOW_HEIGHT * (2 / 5) + 16, 160, 70), 2),
      button.BUTTON("Credits", (c.WINDOW_WIDTH / 5, c.WINDOW_HEIGHT * (3 / 5) + 16, 160, 70), 3),
      button.BUTTON("Exit", (c.WINDOW_WIDTH / 5, c.WINDOW_HEIGHT * (4 / 5) + 16, 160, 70), -1)
    ]

  def handleSettings(self):
    self.active_gif.render()
    self.active_buttons = [
      button.BUTTON("Settings", (c.WINDOW_WIDTH / 2, 32, -1, -1), 0, font=c.FONT_40),
      button.BUTTON("DEV: exp", (c.WINDOW_WIDTH / 5, c.WINDOW_HEIGHT * (2 / 5) + 16, 160, 70), -9),
      button.BUTTON("Home", (c.WINDOW_WIDTH - 36 - 5, 20 + 5, 72, 40), 1, font=c.FONT_24)
    ]
    # RESUME DYNAMIC BUTTONS HERE


  def handleCredits(self):
    pass

  def handleGameplay(self):
    pass

  def handleRetry(self):
    pass

  def handleButtons(self):
    pass

  def handlePhysics(self):
    pass
    
