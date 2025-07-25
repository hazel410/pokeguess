import constants as c
import functions as func
import pygame
import time
import numpy as np

class GAME_LOGIC:
  def __init__(self):
    with open(c.CSV_LOCATION) as CSV:
      self.file_list = CSV.read()
    self.file_list = self.file_list.split("\n")
    



  def input(self, user_input):
    pass

  def upkeep(self):
    pass

  def question(self):
    pass

  def reset(self):
    pass

### No Longer Game Class

def export(screen, staticgame):
  pass

def monsolver(pokemon_number):
  pass

if __name__=='__main__':
  GAME_LOGIC()