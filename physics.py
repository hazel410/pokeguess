import constants as c
import random
import numpy as np

class PHYSICS:
  def __init__(self):
    self.spawn_tbh = True
    self.draw_bounds = False
    self.active_objects = []
    self.angle = random.randrange(c.PHYSICS_ANGLES) * (np.pi / 180)
    self.image = 