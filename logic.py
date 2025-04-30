import pandas as pd
import constants as c
import functions as func
import pygame
import sounds as sfx
import time

class GAME_LOGIC:
  def __init__(self):
    # basic inits
    self.response_is_short = False
    self.question_num = 1
    self.main_df = pd.read_csv(c.CSV_LOCATION, skiprows=1)
    self.main_dict = pd.DataFrame.to_dict(self.main_df, orient='list')
    self.category_list = list(self.main_dict.keys())
    self.question_dict = pd.DataFrame.to_dict(pd.read_csv(c.CSV_LOCATION, nrows=0), orient='list')
    self.question_list = list(self.question_dict.keys())
    self.num_of_pokemon = len(self.main_df)
    self.df_vect = []
    self.smart_type_vec = []
    self.smart_gen_vec = []
    self.num_of_category = len(self.question_list)
    self.category_sums = [0]
    for category in range(self.num_of_category - 1):
      self.category_sums.append(sum(self.main_dict[self.category_list[category + 1]]))
    
    # Smart Stuff
    self.type_begin_index = self.category_list.index('Normal')
    self.gen_begin_index = self.category_list.index('G1')
    self.smart_type_output = [1] * c.NUMBER_OF_POKEMON_TYPES
    self.smart_gen_output = [1] * c.NUMBER_OF_POKEMON_GENS
    self.smart_type_sum = self.category_sums[self.type_begin_index:(self.type_begin_index + 17)]
    self.smart_gen_sum = self.category_sums[self.gen_begin_index:(self.gen_begin_index + 8)]
    
    # Rename these later
    self.ssit = list(map(lambda x, y: x * y, self.smart_type_output, self.smart_type_sum))
    self.ssig = list(map(lambda x, y: x * y, self.smart_gen_output, self.smart_gen_sum))
    self.ssvt = func.ssp3(self.ssit, self.num_of_pokemon / 2)
    self.ssvg = func.ssp3(self.ssig, self.num_of_pokemon / 2)
    self.ssct = (self.category_list[self.ssvt[1][0] + self.type_begin_index], self.category_list[self.ssvt[1][1] + self.type_begin_index],
                  self.category_list[self.ssvt[1][2] + self.type_begin_index])
    self.sscg = (self.category_list[self.ssvg[1][0] + self.gen_begin_index], self.category_list[self.ssvg[1][1] + self.gen_begin_index],
                  self.category_list[self.ssvg[1][2] + self.gen_begin_index])
    self.ssqt = "Is your pokemon " + self.ssct[0] + " " + self.ssct[1] + " or " + self.ssct[2] + " type?"
    self.ssqg = ("Was your pokemon introduced in  gens " + str(self.ssvg[1][0] + 1) + " " +
                  str(self.ssvg[1][1] + 1) + " or " + str(self.ssvg[1][2] + 1)) + "?"
    
    self.category_sums.append(self.ssvt[0])
    self.category_sums.append(self.ssvg[0])
    self.category_list.append(c.SMART_TYPE_HEADER)
    self.category_list.append(c.SMART_GEN_HEADER)
    
    # Best Values and booleuser_input
    self.best_value = min(self.category_sums, key=lambda x: abs(x - self.num_of_pokemon / 2))
    self.best_category = self.category_list[self.category_sums.index(self.best_value)]
    self.is_stalemate = self.best_value == 0 or self.best_value == self.num_of_pokemon
    self.can_undo = len(self.df_vect) >= 2
    self.is_win = True
    
    # Questions
    if self.best_category == c.SMART_TYPE_HEADER:
        self.best_question = self.ssqt
        self.smart_type_output[self.ssvt[1][0]] = 0
        self.smart_type_output[self.ssvt[1][1]] = 0
        self.smart_type_output[self.ssvt[1][2]] = 0
    elif self.best_category == c.SMART_GEN_HEADER:
        self.best_question = self.ssqg
        self.smart_gen_output[self.ssvg[1][0]] = 0
        self.smart_gen_output[self.ssvg[1][1]] = 0
        self.smart_gen_output[self.ssvg[1][2]] = 0
    elif self.best_category in self.category_list[0:(len(self.category_list) - 2)]:
        self.best_question = self.question_list[self.category_sums.index(self.best_value)]

  def input(self, user_input):
          if user_input == -1:
              if self.can_undo:
                  offset = 2 if self.num_of_pokemon > 1 else 1
                  self.main_df = self.df_vect[self.question_num - offset]
                  self.smart_type_output = self.smart_type_vec[self.question_num - offset]
                  self.smart_gen_output = self.smart_gen_vec[self.question_num - offset]
                  del self.df_vect[self.question_num - offset]
                  del self.smart_type_vec[self.question_num - offset]
                  del self.smart_gen_vec[self.question_num - offset]
                  self.question_num += (1 - offset)
                  self.response_is_short = False
          elif user_input == 1:
              self.df_vect.append(self.main_df)
              self.smart_type_vec.append(list(self.smart_type_output))
              self.smart_gen_vec.append(list(self.smart_gen_output))
              self.question_num += 1
              if self.num_of_pokemon == 1:
                  pass
              elif self.is_stalemate:
                  self.response_is_short = True
                  self.main_df = (self.main_df.drop(self.main_df[self.main_df['Category'] !=
                                  self.main_df['Category'][self.main_df.first_valid_index()]].index))
              elif self.best_category == c.SMART_TYPE_HEADER:
                  self.smart_type_output[self.ssvt[1][0]] = 0
                  self.smart_type_output[self.ssvt[1][1]] = 0
                  self.smart_type_output[self.ssvt[1][2]] = 0
                  msk = (self.main_df[self.ssct[0]].eq(0) &
                        self.main_df[self.ssct[1]].eq(0) &
                        self.main_df[self.ssct[2]].eq(0))
                  self.main_df = self.main_df.drop(self.main_df.index[msk])
              elif self.best_category == c.SMART_GEN_HEADER:
                  self.smart_gen_output[self.ssvg[1][0]] = 0
                  self.smart_gen_output[self.ssvg[1][1]] = 0
                  self.smart_gen_output[self.ssvg[1][2]] = 0
                  msk = (self.main_df[self.sscg[0]].eq(0) &
                        self.main_df[self.sscg[1]].eq(0) &
                        self.main_df[self.sscg[2]].eq(0))
                  self.main_df = self.main_df.drop(self.main_df.index[msk])
              elif self.best_category in self.category_list[0:(len(self.category_list) - 2)]:
                  self.main_df = self.main_df.drop(self.main_df[self.main_df[self.best_category] == 0].index)
          elif user_input == 0:
              self.df_vect.append(self.main_df)
              self.smart_type_vec.append(list(self.smart_type_output))
              self.smart_gen_vec.append(list(self.smart_gen_output))
              self.question_num += 1
              if self.num_of_pokemon == 1:
                  pass
              elif self.is_stalemate:
                  self.main_df = (self.main_df.drop(self.main_df[self.main_df['Category'] ==
                                                        self.main_df['Category'][self.main_df.first_valid_index()]].index))
              elif self.best_category == c.SMART_TYPE_HEADER:
                  self.smart_type_output[self.ssvt[1][0]] = 0
                  self.smart_type_output[self.ssvt[1][1]] = 0
                  self.smart_type_output[self.ssvt[1][2]] = 0
                  self.main_df = self.main_df.drop(self.main_df[self.main_df[self.ssct[0]] == 1].index)
                  self.main_df = self.main_df.drop(self.main_df[self.main_df[self.ssct[1]] == 1].index)
                  self.main_df = self.main_df.drop(self.main_df[self.main_df[self.ssct[2]] == 1].index)
              elif self.best_category == c.SMART_GEN_HEADER:
                  self.smart_gen_output[self.ssvg[1][0]] = 0
                  self.smart_gen_output[self.ssvg[1][1]] = 0
                  self.smart_gen_output[self.ssvg[1][2]] = 0
                  self.main_df = self.main_df.drop(self.main_df[self.main_df[self.sscg[0]] == 1].index)
                  self.main_df = self.main_df.drop(self.main_df[self.main_df[self.sscg[1]] == 1].index)
                  self.main_df = self.main_df.drop(self.main_df[self.main_df[self.sscg[2]] == 1].index)
              elif self.best_category in self.category_list[0:(len(self.category_list) - 2)]:
                  self.main_df = self.main_df.drop(self.main_df[self.main_df[self.best_category] == 1].index)

  def upkeep(self):
      # basic items
      self.main_dict = pd.DataFrame.to_dict(self.main_df, orient='list')
      self.num_of_pokemon = len(self.main_df)
      # ending fix
      if self.num_of_pokemon == 1:
          self.question_num -= 1
      # resums qvalues
      self.category_sums = [0]
      loopvar = 1
      while loopvar < self.num_of_category:
          self.category_sums.append(sum(self.main_dict[self.category_list[loopvar]]))
          loopvar += 1
      # calculates subset sum vals, cats, ques, and appends sums
      self.smart_type_sum = self.category_sums[self.type_begin_index:(self.type_begin_index + 17)]
      self.ssit = list(map(lambda x, y: x * y, self.smart_type_output, self.smart_type_sum))
      self.ssvt = func.ssp3(self.ssit, self.num_of_pokemon / 2)
      self.ssct = (self.category_list[self.ssvt[1][0] + self.type_begin_index], self.category_list[self.ssvt[1][1] + self.type_begin_index],
                    self.category_list[self.ssvt[1][2] + self.type_begin_index])
      self.ssqt = "Is your pokemon " + self.ssct[0] + " " + self.ssct[1] + " or " + self.ssct[2] + " type?"
      self.category_sums.append(self.ssvt[0])
      self.smart_gen_sum = self.category_sums[self.gen_begin_index:(self.gen_begin_index + 17)]
      self.ssig = list(map(lambda x, y: x * y, self.smart_gen_output, self.smart_gen_sum))
      self.ssvg = func.ssp3(self.ssig, self.num_of_pokemon / 2)
      self.sscg = (self.category_list[self.ssvg[1][0] + self.gen_begin_index], self.category_list[self.ssvg[1][1] + self.gen_begin_index],
                    self.category_list[self.ssvg[1][2] + self.gen_begin_index])
      self.ssqg = ("Was your pokemon introduced in  gens " + str(self.ssvg[1][0] + 1) + " " +
                    str(self.ssvg[1][1] + 1) + " or " + str(self.ssvg[1][2] + 1)) + "?"
      self.category_sums.append(self.ssvg[0])
      # Refreshes best val, cat, and stale / undo
      self.best_value = min(self.category_sums, key=lambda x: abs(x - self.num_of_pokemon / 2))
      self.best_category = self.category_list[self.category_sums.index(self.best_value)]
      self.is_stalemate = self.best_value <= 1 or self.best_value >= self.num_of_pokemon - 1
      self.can_undo = len(self.df_vect) >= 1

  def question(self):
      if self.num_of_pokemon == 1 & self.response_is_short:
          self.best_question = "Yippee!! Do you want to play again?"
      elif self.num_of_pokemon == 1:
          self.best_question = 'Your pokemon is ' + self.main_dict[self.category_list[0]][0] + "!! Do you want to play again?"
      elif self.is_stalemate:
          self.best_question = "Is your pokemon " + self.main_dict[self.category_list[0]][0] + "?"
      elif self.best_category == c.SMART_TYPE_HEADER:
          self.best_question = self.ssqt
      elif self.best_category == c.SMART_GEN_HEADER:
          self.best_question = self.ssqg
      elif self.best_category in self.category_list[0:(len(self.category_list) - 2)]:
          self.best_question = self.question_list[self.category_sums.index(self.best_value)]

def export(screen):
  """
  a function that solves every pokemon and exports that data

  :return: 0 if succesful, -1 elsewise
  """

  staticgame = GAME_LOGIC()
  numberomon = len(staticgame.main_df)
  csvinterme = {}
  t0 = time.perf_counter()
  for pokemon in range(numberomon):
    csvinterme[staticgame.main_df.iloc[pokemon]['Category']] = monsolver(pokemon)
    percent = round((pokemon / numberomon) * 100, 2)
    t1 = time.perf_counter()
    te = t1 - t0
    pygame.draw.rect(screen, c.BACKGROUND_COLOR, (c.WINDOW_WIDTH * (2 / 5), c.WINDOW_HEIGHT / 4, 1000, 1000))
    pygame.draw.rect(screen, c.GRAY, ((c.WINDOW_WIDTH / 2) - 50, (c.WINDOW_HEIGHT / 2), 200, 50))
    pygame.draw.rect(screen, c.WHITE, ((c.WINDOW_WIDTH / 2) - 50, (c.WINDOW_HEIGHT / 2), round(percent * 2), 50))
    perrend = c.FONT_24.render(str(percent) + "%", True, c.WHITE)
    monrend = c.FONT_24.render('mons left: ' + str(numberomon - pokemon), True, c.WHITE)
    timrend = c.FONT_24.render('time spent: ' + str(round(te)) + ' secs', True, c.WHITE)
    perrect = perrend.get_rect(topleft=[(c.WINDOW_WIDTH / 2) + 175, (c.WINDOW_HEIGHT / 2) + 12])
    monrect = monrend.get_rect(topleft=[(c.WINDOW_WIDTH / 2) - 45, (c.WINDOW_HEIGHT / 2) - 40])
    timrect = timrend.get_rect(topleft=[(c.WINDOW_WIDTH / 2) - 45, (c.WINDOW_HEIGHT / 2) + 75])
    screen.blit(perrend, perrect)
    screen.blit(monrend, monrect)
    screen.blit(timrend, timrect)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return -1
    pygame.display.flip()
  file = pd.DataFrame(dict([(key, pd.Series(value)) for key, value in csvinterme.items()]))
  filetrans = file.transpose()
  filetrans.to_csv(c.ROOTDIR + 'out.csv')
  pygame.mixer.find_channel(True).play(sfx.cor)
  return 0

def monsolver(pokemon_number):
  """
  solves a given pokemon and returns data

  :param pokemon_number: int; the number of the pokemon being solved for
  :return: list; data yk
  """

  driver = GAME_LOGIC()
  monu = pokemon_number
  info = driver.main_df.iloc[monu]
  val = 0
  if driver.is_stalemate:
    val = 1 if info['Category'] == driver.main_dict[driver.category_list[0]][0] else 0
  elif driver.best_category == c.SMART_TYPE_HEADER:
    val = info[driver.ssct[0]] + info[driver.ssct[1]] + info[driver.ssct[2]]
  elif driver.best_category == c.SMART_GEN_HEADER:
    val = info[driver.sscg[0]] + info[driver.sscg[1]] + info[driver.sscg[2]]
  elif driver.best_category in driver.category_list[0:(len(driver.category_list) - 2)]:
    val = info[driver.best_category]
  ans = 1 if val > 0 else 0
  output = ['Question ' + str(driver.question_num), driver.num_of_pokemon, driver.best_category, ans, driver.category_sums]
  while driver.num_of_pokemon > 1:
    if driver.is_stalemate:
      val = 1 if info['Category'] == driver.main_dict[driver.category_list[0]][0] else 0
    elif driver.best_category == c.SMART_TYPE_HEADER:
      val = info[driver.ssct[0]] + info[driver.ssct[1]] + info[driver.ssct[2]]
    elif driver.best_category == c.SMART_GEN_HEADER:
      val = info[driver.sscg[0]] + info[driver.sscg[1]] + info[driver.sscg[2]]
    elif driver.best_category in driver.category_list[0:(len(driver.category_list) - 2)]:
      val = info[driver.best_category]
    ans = 1 if val > 0 else 0
    driver.input(ans)
    driver.upkeep()
    if driver.is_stalemate and driver.num_of_pokemon > 1:
      output.append('Question ' + str(driver.question_num))
      output.append(driver.num_of_pokemon)
      output.append('Stalemate')
      output.append(ans)
      output.append(driver.category_sums)
    elif driver.best_category == c.SMART_TYPE_HEADER:
      output.append('Question ' + str(driver.question_num))
      output.append(driver.num_of_pokemon)
      output.append(driver.ssct)
      output.append(ans)
      output.append(driver.category_sums)
    elif driver.best_category == c.SMART_GEN_HEADER:
      output.append('Question ' + str(driver.question_num))
      output.append(driver.num_of_pokemon)
      output.append(driver.sscg)
      output.append(ans)
      output.append(driver.category_sums)
    elif driver.best_category != 'Category':
      output.append('Question ' + str(driver.question_num))
      output.append(driver.num_of_pokemon)
      output.append(driver.best_category)
      output.append(ans)
      output.append(driver.category_sums)
    else:
      pass

  return output  
