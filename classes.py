import pygame
import variables
pygame.font.init()

class button:
    def __init__(self, color, highcolor, textcolor, startpos, wh, text=''):
        self.highcolor = highcolor
        self.ocolor = color
        self.color = color
        self.x = startpos[0]
        self.y = startpos[1]
        self.width = wh[0]
        self.height = wh[1]
        self.text = text
        self.textcolor = textcolor

    def draw(self, win, outline=None):
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = variables.buttonF
            text = font.render(self.text, True, self.textcolor) #TODO change button text color
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        if (pos[0] > self.x) and (pos[0] < (self.x + self.width)) and (pos[1] > self.y) and (pos[1] < (self.y + self.height)):
            self.color = self.highcolor
            return True
        self.color = self.ocolor
        return False