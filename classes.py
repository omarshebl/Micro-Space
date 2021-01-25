import pygame
import random
import variables
from variables import collide
pygame.font.init()

class Button:
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

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(height >= self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(variables.Ygame1):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                if obj.get_armor:
                    obj.set_armor(False)
                else:
                    obj.health -= 10
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = variables.mainplayerimg
        self.laser_img = variables.missile
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.armor = False

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(variables.Ygame1):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)
                        return obj.get_var()

    def draw(self, window):
        self.drawarmor(window)
        super().draw(window)
        self.healthbar(window)

    def drawarmor(self, window):
        if self.armor:
            pygame.draw.circle(window, (192, 254, 255), (self.x+self.ship_img.get_width()/2,self.y+self.ship_img.get_height()/2), self.ship_img.get_width()+5)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0),
                         (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + 10,
                                               self.ship_img.get_width() * (self.health / self.max_health), 10))

    def get_armor(self):
        return self.armor

    def set_armor(self, state):
        self.armor = state

class Enemy(Ship):
    variation = (variables.alien, variables.alien1, variables.alien2)

    def __init__(self, x, y, var, health=100):
        super().__init__(x, y, health)
        self.laser_img = variables.bomb
        self.var = var
        self.ship_img = self.variation[var]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel
        rando = random.randint(-1,1)
        if rando == -1:
            self.x -= vel*random.randint(1,3)
        elif rando == 1:
            self.x += vel*random.randint(1,3)

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_var(self):
        return self.var


