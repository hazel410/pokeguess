import constants as c
import random
import numpy as np
import pygame
import functions as funcs

class OBJECT:
  def __init__(self, spawn_tbh):
    self.spawn_tbh = True
    self.draw_bounds = False
    self.active_objects = []
    self.init_angle = random.randrange(c.PHYSICS_ANGLES[0], c.PHYSICS_ANGLES[1]) * (np.pi / 180)
    self.is_tbh = spawn_tbh
    if spawn_tbh:
      self.image = pygame.image.load(c.TBH_LOCATION)
    else:
      self.image = funcs.GIF(c.BLAHAJ_LOCATION, scale=1)
    self.size = self.image.get_size()
    self.xpos = random.randrange(0, round(c.WINDOW_WIDTH - (self.size[0] / 2)))
    self.ypos = random.randrange(0, round(c.WINDOW_HEIGHT - (self.size[1] / 2)))
    self.xvel = c.PHYSICS_MAGNITUDE * np.cos(self.init_angle)
    self.yvel = c.PHYSICS_MAGNITUDE * np.sin(self.init_angle)
    self.collision_limit = random.randrange(c.PHYSICS_MAX_COLLISIONS[0], c.PHYSICS_MAX_COLLISIONS[1])
    self.times_collided = 0
    self.dead = False
  
  def position_update(self):
    self.xvel *= (1 - c.PHYSICS_AIR_RESISTANCE)
    self.yvel = self.yvel + c.PHYSICS_GRAVITY
    self.xpos = self.xpos + self.xvel
    self.yvel = self.ypos + self.yvel
    if self.times_collided <= self.collision_limit:
      if self.xpos > c.WINDOW_WIDTH - self.size[0] or self.xpos < 0:
        self.xpos = min([0, c.WINDOW_WIDTH - self.size[0]], key=lambda z: abs(z - self.xpos))
        self.xvel = self.xvel * c.PHYSICS_ELASTICITY * -1
        self.times_collided += 1
      if self.ypos > c.WINDOW_HEIGHT - self.size[1] or self.ypos < 0:
        self.ypos = min([0, c.WINDOW_HEIGHT - self.size[1]], key=lambda z: abs(z - self.ypos))
        self.times_collided += 1
    elif self.xpos > c.WINDOW_WIDTH or self.xpos < 0 - self.size[0] or self.ypos > c.WINDOW_HEIGHT:
      self.dead = True
  
  def draw(self):
    pass
    