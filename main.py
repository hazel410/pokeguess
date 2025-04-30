import asyncio
import pygame
import random

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
    pygame.event.set_blocked(None)
    pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
    pygame.event.set_allowed(pygame.QUIT)
    self.clock = pygame.time.Clock()
    self.GAME_LOGIC = logic.GAME_LOGIC()
    self.SFX = sfx.SFX()

    # loop vars
    self.reset_gamemode = False
    self.question_number = "Question: " + str(self.GAME_LOGIC.question_num)
    self.mon_number = "Pokémon Left: " + str(self.GAME_LOGIC.num_of_pokemon)
    self.question_text = self.GAME_LOGIC.best_question
    self.active_gif = functions.GIF(self.screen, c.GIF_LOCATION + c.GIF_LIST[random.randrange(0, c.GIF_COUNT - 1)] + '.gif', [c.WINDOW_WIDTH * .7, c.WINDOW_HEIGHT / 2])
    self.gamemode = 1
    self.active_buttons = []
    self.active_objects = []
    self.fps = self.clock.get_fps()
    self.quit = False
    self.spawn_tbh = True
    self.scroll_on_silly = False
    self.clicked_args = []
    self.mouse_pos = pygame.mouse.get_pos()
    self.is_muted = False
    
    asyncio.run(self.main())

  async def main(self):
    while True:
      pygame.display.flip()
      self.clock.tick(60)
      self.active_buttons = []
      self.clicked_args = []
      self.screen.fill(c.BACKGROUND_COLOR)
      self.fps = self.clock.get_fps()
      self.mouse_pos = pygame.mouse.get_pos()
      self.loadActiveScreen()
      
      if self.reset_gamemode and self.gamemode != 4:
        self.GAME_LOGIC = logic.GAME_LOGIC()
        self.reset_gamemode = False
      self.active_buttons.append(button.BUTTON(self.screen, "FPS: " + str(round(self.fps)), (50, 25, 72, 40), 0, font=c.FONT_24, back=False))
      self.active_buttons.append(button.BUTTON(self.screen, ':3', (30, c.WINDOW_HEIGHT - 25, 30, 30), -3, font=c.FONT_18))
      self.displayButtons()
      self.handleEvents()
      self.handleClickArgs()
      self.handlePhysics()
      
      if self.quit:
        return
      await asyncio.sleep(0)
  
  def loadActiveScreen(self):
    if self.gamemode == 1:
      self.loadHome()
    elif self.gamemode == 2:
      self.loadSettings()
    elif self.gamemode == 3:
      self.loadCredits()
    elif self.gamemode == 4:
      self.loadGameplay()
    elif self.gamemode == 5:
      self.loadRetry()

  def loadHome(self):
    self.active_gif.render()
    self.active_buttons = [
      button.BUTTON(self.screen, "PokéGuess V5", (c.WINDOW_WIDTH / 2, 32, -1, -1), 0, back=False, font=c.FONT_40),
      button.BUTTON(self.screen, "Play", (c.WINDOW_WIDTH / 5, c.WINDOW_HEIGHT * (1 / 5) + 16, 160, 70), 4),
      button.BUTTON(self.screen, "Settings", (c.WINDOW_WIDTH / 5, c.WINDOW_HEIGHT * (2 / 5) + 16, 160, 70), 2),
      button.BUTTON(self.screen, "Credits", (c.WINDOW_WIDTH / 5, c.WINDOW_HEIGHT * (3 / 5) + 16, 160, 70), 3),
      button.BUTTON(self.screen, "Exit", (c.WINDOW_WIDTH / 5, c.WINDOW_HEIGHT * (4 / 5) + 16, 160, 70), -1)
    ]

  def loadSettings(self):
    self.active_gif.render()
    mute_text = "Unmute SFX" if self.is_muted else "Mute SFX"
    silly_text = "Blåhaj" if self.spawn_tbh else "TBH"
    scroll_text = "No Scroll" if self.scroll_on_silly else "Scroll on :3"
    self.active_buttons = [
      button.BUTTON(self.screen, "Settings", (c.WINDOW_WIDTH / 2, 32, -1, -1), 0, font=c.FONT_40),
      button.BUTTON(self.screen, "Home", (c.WINDOW_WIDTH - 36 - 5, 20 + 5, 72, 40), 1, font=c.FONT_24),
      button.BUTTON(self.screen, mute_text, (c.WINDOW_WIDTH / 5, c.WINDOW_HEIGHT * (1 / 5) + 16, 160, 70), -7, font=c.FONT_24),
      button.BUTTON(self.screen, silly_text, (c.WINDOW_WIDTH / 5, c.WINDOW_HEIGHT * (2 / 5) + 16, 160, 70), -10),
      button.BUTTON(self.screen, scroll_text, (c.WINDOW_WIDTH / 5, c.WINDOW_HEIGHT * (3 / 5) + 16, 160, 70), -8, font=c.FONT_24)
    ]
    if c.RUNNING_LOCALLY:
      self.active_buttons.append(button.BUTTON(self.screen, "Export", (c.WINDOW_WIDTH / 5, c.WINDOW_HEIGHT * (4 / 5) + 16, 160, 70), -9))

  def loadCredits(self):
    self.screen.blit(pygame.image.load(c.ROOTDIR + 'files/trevenaunt.png'), (50, 50))
    self.screen.blit(pygame.image.load(c.ROOTDIR + 'files/grafaiai.png'), (50, 150))
    self.active_buttons = [
      button.BUTTON(self.screen, "Credits", (c.WINDOW_WIDTH / 2, 32, -1, -1), 0, font=c.FONT_40),
      button.BUTTON(self.screen, "Home", (c.WINDOW_WIDTH - 36 - 5, 20 + 5, 72, 40), 1, font=c.FONT_24),
      button.BUTTON(self.screen, "thanks for helping me design the ux of this game! :]", (c.WINDOW_WIDTH / 2, 120, 275, 10), 0, font=c.FONT_24, wrap=True, back=False),
      button.BUTTON(self.screen, "thanks for helping me learn python! :D", (c.WINDOW_WIDTH / 2, 240, 275, 10), 0, font=c.FONT_24, wrap=True, back=False)
    ]

  def loadGameplay(self):
    color_undo = c.LIGHT_CORNFLOWER_BLUE_1 if self.GAME_LOGIC.can_undo else c.GRAY
    question_number = "Question: " + str(self.GAME_LOGIC.question_num)
    pokemon_number = "Pokémon Left: " + str(self.GAME_LOGIC.num_of_pokemon)
    question_text = self.GAME_LOGIC.best_question
    self.reset_gamemode = True
    self.active_buttons = [
      button.BUTTON(self.screen, "Home", (c.WINDOW_WIDTH - 36 - 5, 20 + 5, 72, 40), 1, font=c.FONT_24),
      button.BUTTON(self.screen, '', (c.WINDOW_WIDTH * (23 / 32), c.WINDOW_HEIGHT * .17, 250, 2), 0, button_color=c.WHITE, hover_color=c.WHITE),
      button.BUTTON(self.screen, "No", (c.WINDOW_WIDTH * (13 / 16), c.WINDOW_HEIGHT * .75, 120, 75), -14, font=c.FONT_40),
      button.BUTTON(self.screen, "Yes", (c.WINDOW_WIDTH * (10 / 16), c.WINDOW_HEIGHT * .75, 120, 75), -13, font=c.FONT_40),
      button.BUTTON(self.screen, "Undo", (c.WINDOW_WIDTH * (23 / 32), c.WINDOW_HEIGHT * .9, 252, 50), -15, hover_color=color_undo),
      button.BUTTON(self.screen, question_number, (c.WINDOW_WIDTH * (23 / 32), c.WINDOW_HEIGHT * .08, -1, -1), 0),
      button.BUTTON(self.screen, pokemon_number, (c.WINDOW_WIDTH * (23 / 32), c.WINDOW_HEIGHT * .14, -1, -1), 0, font=c.FONT_24),
      button.BUTTON(self.screen, question_text, (c.WINDOW_WIDTH * (23 / 32), c.WINDOW_HEIGHT * (2 / 5), 252, 200), 0, font=c.FONT_24, wrap=True, button_color=c.GRAY, hover_color=c.GRAY)
    ]

  def loadRetry(self):
    self.loadGameplay()
    self.gamemode = 4
    self.GAME_LOGIC = logic.GAME_LOGIC()

  def displayButtons(self):
    for button in self.active_buttons:
      button.checkOverlapping(self.mouse_pos)
      button.draw()
      button.hover()
    
  def handleEvents(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.quit = True
      elif event.type == pygame.MOUSEBUTTONDOWN:
        for button in self.active_buttons:
          if button.mouse_overlapping:
            self.clicked_args.append(button.click_arg)
      
      """The comment doesn't work because buttons are initialized
         every frame. you'd need to change that to have the mouse
         function better :/"""


            # button.mouse_down = True
      # elif event.type == pygame.MOUSEBUTTONUP:
      #   for button in self.active_buttons:
      #     if button.mouse_overlapping and button.mouse_down:
      #       print("good mouse up")
      #       button.mouse_down = False
      #       self.clicked_args.append(button.click_arg)
  
  def handleClickArgs(self):
    for argument in self.clicked_args:
      if pygame.mouse.get_pressed()[0]: # left click
        if argument == 0:
          pass
        elif argument > 0:
          self.gamemode = argument
          self.active_gif = functions.GIF(self.screen, c.GIF_LOCATION + c.GIF_LIST[random.randrange(0, c.GIF_COUNT - 1)] + '.gif', [c.WINDOW_WIDTH * .7, c.WINDOW_HEIGHT / 2])
          if argument != 5:
            pygame.mixer.pause()
        elif argument == -1:
          self.quit = True
        elif argument == -3:
          self.active_objects.append(physics.OBJECT(self.screen, self.spawn_tbh))
        elif argument == -7:
          self.SFX.toggle_mute(self.is_muted)
          self.is_muted = not self.is_muted
        elif argument == -8:
          self.scroll_on_silly = not self.scroll_on_silly
        elif argument == -9:
          if logic.export(self.screen, logic.GAME_LOGIC()) == -1:
            return -1
        elif argument == -10:
          self.spawn_tbh = not self.spawn_tbh
        elif argument == -13:
          self.handleGameplay(1)
        elif argument == -14:
          self.handleGameplay(0)
        elif argument == -15:
          self.handleGameplay(-1)
      elif pygame.mouse.get_pressed()[2]: # right click
        if argument == -3:
          self.active_objects = []
          pygame.mixer.pause()
      elif self.scroll_on_silly: # scrolling
        if argument == -3:
          self.active_objects.append(physics.OBJECT(self.screen, self.spawn_tbh))

  def handlePhysics(self):
    for object in self.active_objects:
      object.position_update()
      object.draw()
      if object.dead:
        self.active_objects.remove(object)
        pygame.mixer.find_channel(True).play(self.SFX.bye)
    
  def handleGameplay(self, player_input):
    if player_input == 1: # YES
      self.GAME_LOGIC.input(1)
      if self.GAME_LOGIC.num_of_pokemon == 1:
        self.gamemode = 5
        pygame.mixer.pause()
    elif player_input == 0: # NO
      self.GAME_LOGIC.input(0)
      if self.GAME_LOGIC.num_of_pokemon == 1:
        self.gamemode = 1
        pygame.mixer.pause()
    elif player_input == -1: # UNDO
      self.GAME_LOGIC.input(-1)
    
    self.GAME_LOGIC.upkeep()
    if self.GAME_LOGIC.num_of_pokemon == 1 and self.GAME_LOGIC.is_win and self.gamemode == 4:
      pygame.mixer.find_channel(True).play(self.SFX.che)
      self.GAME_LOGIC.is_win = False
    
    self.GAME_LOGIC.question()
  
MAIN()