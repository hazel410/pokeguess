import constants as c
import pygame

class BUTTON:
  def __init__(self, screen, text, rect, arg, 
               hide=False, 
               back=True, 
               wrap=False,
               font=c.FONT_32, 
               text_color=c.WHITE, 
               button_color=c.LIGHT_CORNFLOWER_BLUE_2, 
               hover_color=c.LIGHT_CORNFLOWER_BLUE_1):
      """
        Initializes a Button for use in my game.

        :param text: string; the text present on the button
        :param draw: tuple; [center x position to brnd, center y position to brnd, width of button, height of button]
        :param mode: int; for handling mode changes from workingbuttons, see Button.click for more
        :param hide: boolean; if true, button is hidden until hovered
        :param back: boolean; if false, button is pure text. you can still click it
        :param font: pygame.font.Font; for specifying a font for the button outside from the preset
        :param text_color: tuple; for specifying a text color outside from the preset
        :param button_color: tuple; for specifying a button color outside from the preset
        :param hover_color: tuple; for specifying a button hover color outside from the preset
        :param wrap: boolean; if true, horizontally wraps the text to the width of the button
        """
      
      self.screen = screen
      self.text = text
      self.click_arg = arg
      self.hide = hide
      self.back = back
      self.wrap = wrap
      self.font = font
      self.text_color = text_color
      self.button_color = button_color
      self.hover_color = hover_color
      self.words = self.text.split()
      self.num_words = len(self.words)
      self.rect = rect
      self.x_center = rect[0]
      self.y_center = rect[1]
      self.xlen = rect[2]
      self.ylen = rect[3]
      self.render = self.font.render(self.text, True, self.text_color)
      self.render_rect = self.render.get_rect(center=[self.x_center, self.y_center])
      self.drawing_rect = [self.x_center - self.xlen / 2, self.y_center - self.ylen / 2, self.xlen, self.ylen]
      self.lower_x = self.drawing_rect[0]
      self.upper_x = self.drawing_rect[0] + self.drawing_rect[2]
      self.lower_y = self.drawing_rect[1]
      self.upper_y = self.drawing_rect[1] + self.drawing_rect[3]
      self.size = self.font.size(self.text)
      self.mouse_overlapping = False
      self.mouse_down = False
      self.wrap_index = 0
  
  def checkOverlapping(self, mouse_pos):
    self.mouse_overlapping = mouse_pos[0] >= self.lower_x and mouse_pos[0] <= self.upper_x and mouse_pos[1] >= self.lower_y and mouse_pos[1] <= self.upper_y

  def draw(self):
    if not self.hide:
      
      if self.back:
        pygame.draw.rect(self.screen, self.button_color, self.drawing_rect)
      
      if self.wrap:
        self.drawWrappedText()
      else:
        self.screen.blit(self.render, self.render_rect)
  
  def hover(self):
    if self.back and self.mouse_overlapping:
      pygame.draw.rect(self.screen, self.hover_color, self.drawing_rect)
      if self.wrap:
        self.drawWrappedText()
      else:
        self.screen.blit(self.render, self.render_rect)
  
  def drawWrappedText(self):
    wrapped_text = []
    current_line = ""
    current_row = 0
    for word in self.words:
      
      # for first word of first row, adds it immediately
      if len(current_line) < 1:
        current_line = word
      # else add it to current string
      else:
        current_line = current_line + ' ' + word
      
      # if this is the word that makes things too big, remove it and add it to the next
      if self.font.size(current_line)[0] > self.xlen + (2 * c.WRAP_X_PADDING):
        current_line = current_line[0:current_line.rfind(" ")]
        wrapped_text.append(current_line)
        current_row += 1
        current_line = word
    
    # adds whatever is leftover
    if current_line not in wrapped_text:
      wrapped_text.append(current_line)
    
    # words are now split into seperate lines, so draw them (centered)
    line_number = 0
    if len(wrapped_text) % 2 == 0:
      line_y_int = self.y_center - ((len(wrapped_text) * c.WRAP_Y_PADDING) + ((self.size[1] / 2) * (len(wrapped_text) - 1)))
    else:
      line_y_int = self.y_center - ((len(wrapped_text) - 1) * (c.WRAP_Y_PADDING + self.size[1]) * (1 / 2)) 
    for line in wrapped_text:
      line_render = self.font.render(line, True, self.text_color)
      self.screen.blit(line_render, line_render.get_rect(center=[self.x_center, line_y_int + ((self.size[1] + c.WRAP_Y_PADDING) * line_number)]))
      line_number += 1