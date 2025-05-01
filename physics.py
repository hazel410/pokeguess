import constants as c
import random
import numpy as np
import pygame
import functions as funcs

class OBJECT:
  def __init__(self, screen, spawn_tbh):
    self.screen = screen
    self.draw_bounds = False
    self.init_angle = random.randrange(1, 360) * (np.pi / 180)
    
    self.is_tbh = spawn_tbh
    if self.is_tbh:
      self.image = pygame.image.load(c.TBH_LOCATION)
    else:
      self.image = funcs.GIF(screen, c.BLAHAJ_LOCATION, [0, 0], scale=1, speed=2, orient='topleft')
    self.size = self.image.get_size()
    self.xpos = random.randrange(0, round(c.WINDOW_WIDTH - (self.size[0] / 2)))
    self.ypos = random.randrange(0, round(c.WINDOW_HEIGHT - (self.size[1] / 2)))
    self.xvel = c.PHYSICS_INIT_VELOCITY * np.cos(self.init_angle)
    self.yvel = c.PHYSICS_INIT_VELOCITY * np.sin(self.init_angle)
    if not self.is_tbh:
      self.image.updatePosition([self.xpos, self.ypos])
    
    
    self.collision_limit = random.randrange(c.PHYSICS_MAX_COLLISIONS[0], c.PHYSICS_MAX_COLLISIONS[1])
    self.times_collided = 0
    self.tick_limit = random.randrange(c.PHYSICS_TICK_TIMER[0], c.PHYSICS_TICK_TIMER[1])
    self.elapsed_ticks = 0
    
    self.is_offscreen = False
    self.is_currently_collision = False
    self.is_flashing = False
    self.is_dead = False
  
  def position_update(self):
    # updates position and velocity
    self.xvel *= (1 - c.PHYSICS_AIR_RESISTANCE)
    self.yvel = self.yvel + c.PHYSICS_GRAVITY
    self.xpos = self.xpos + self.xvel
    self.ypos = self.ypos + self.yvel
    self.is_currently_collision = False
    
    if c.PHYSICS_IS_TIMER_BASED:
      self.fix_position()
      self.elapsed_ticks += 1
      if self.elapsed_ticks < self.tick_limit - c.PHYSICS_TIMER_DESPAWN_WHEN:
        pass
      elif self.elapsed_ticks == self.tick_limit:
        self.is_dead = True
      else: 
        self.is_flashing = True

    else: # is Collision Based
      if self.collision_limit > self.times_collided:
        self.fix_position()
      elif self.xpos > c.WINDOW_WIDTH or self.xpos < 0 - self.size[0] or self.ypos > c.WINDOW_HEIGHT:
        self.is_dead = True
  
  def fix_position(self):
    if (self.xpos > c.WINDOW_WIDTH - self.size[0] or self.xpos < 0):
      self.xpos = min([0, c.WINDOW_WIDTH - self.size[0]], key=lambda z: abs(z - self.xpos))
      self.xvel = self.xvel * c.PHYSICS_ELASTICITY * -1
      self.times_collided += 1
      self.is_currently_collision = True
    if (self.ypos > c.WINDOW_HEIGHT - self.size[1] or self.ypos < 0):
      self.ypos = min([0, c.WINDOW_HEIGHT - self.size[1]], key=lambda z: abs(z - self.ypos))
      self.yvel = self.yvel * c.PHYSICS_ELASTICITY * -1
      self.times_collided += 1
      self.is_currently_collision = True
  
  def draw(self):
    if self.is_flashing and self.elapsed_ticks % (2 * c.PHYSICS_TIMER_FLASH_LENGTH) < c.PHYSICS_TIMER_FLASH_LENGTH:
      pass
    else:
      if self.is_tbh:
        self.screen.blit(self.image, [self.xpos, self.ypos])
      else:
        self.image.updatePosition([self.xpos, self.ypos])
        self.image.render()

      
    