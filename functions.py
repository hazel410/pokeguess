import pygame
from PIL import Image
from math import floor

# subset sum function, for subset of len three
def ssp3(numbers, target):
    """
    A function I made that brute forces a specific subset sum problem

    Tries to grab 3 points of data that are closest to the target

    :returns a tuple of [sum of items, index of items]

    :param numbers: tuple/list; the set of numbers to be input. must contain at least four items
    :param target: int; the goal to achieve
    """

    arr = numbers
    tar = target
    smm = sum(numbers) * 2
    ind = []
    for i in range(len(arr)):
      if arr[i] > 0:
        for j in range(i + 1, len(arr)):
          if arr[j] > 0:
            for k in range(j + 1, len(arr)):
              if arr[k] > 0:
                if abs(tar - smm) > abs(tar - (arr[i] + arr[j] + arr[k])):
                  smm = arr[i] + arr[j] + arr[k]
                  ind = [i, j, k]
    if len(ind) != 3:
        ind = [0, 0, 0]
        smm = 0
    return smm, ind

class GIF:
  def __init__(self, screen, gif_location, position, speed=1, scale=3, orient='center', flipx=False):
    self.screen = screen
    self.position = position
    self.speed = speed
    self.orient = orient
    self.flipx = flipx
    self.active_image = Image.open(gif_location)
    self.num_frames = 1
    self.index = 0
    self.frame_list = []
    self.disp = [] # no idea what this does
    
    # finds number of frames
    while True:
      try:
        self.active_image.seek(self.num_frames)
        self.num_frames += 1
      except EOFError:
        break
    
    for frame in range(self.num_frames):
      self.active_image.seek(frame)
      frame_rgba = self.active_image.convert("RGBA")
      image = pygame.image.fromstring(frame_rgba.tobytes(), frame_rgba.size, "RGBA")
      image = pygame.transform.scale_by(image, scale)
      self.frame_list.append(image)
    self.size = self.frame_list[0].get_size()
  
  def get_size(self):
    return self.size
  
  def updatePosition(self, new_position):
    self.position = new_position
  
  def render(self):
    self.disp = self.frame_list[floor(self.index)]
    
    if self.orient == 'center':
      self.screen.blit(pygame.transform.flip(self.disp, self.flipx, False),
                       [self.position[0] - (self.size[0] / 2), self.position[1] - (self.size[1] / 2)])
    elif self.orient == 'topleft':
      self.screen.blit(pygame.transform.flip(self.disp, self.flipx, False), self.position)
    
    if self.index == len(self.frame_list) - 1:
      self.index = 0
    else:
      self.index += .25 * self.speed

