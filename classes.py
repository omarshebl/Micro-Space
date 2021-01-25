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
            text = font.render(self.text, True, self.textcolor)
            win.blit(text, (self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        if (pos[0] > self.x) and (pos[0] < (self.x + self.width)) and (pos[1] > self.y) and (pos[1] < (self.y + self.height)):
            self.color = self.highcolor
            return True
        self.color = self.ocolor
        return False

class Projectile:
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
        self.projectile_img = None
        self.projectiles = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for projectile in self.projectiles:
            projectile.draw(window)

    def move_projectiles(self, vel, obj):
        self.cooldown()
        for projectile in self.projectiles:
            projectile.move(vel)
            if projectile.off_screen(variables.Ygame1):
                self.projectiles.remove(projectile)
            elif projectile.collision(obj):
                if obj.get_armor():
                    obj.set_armor(False)
                else:
                    obj.health -= 10
                self.projectiles.remove(projectile)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            projectile = Projectile(self.x, self.y, self.projectile_img)
            self.projectiles.append(projectile)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = variables.mainplayerimg
        self.projectile_img = variables.missile
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health
        self.armor = False

    def move_projectiles(self, vel, objs):
        self.cooldown()
        for projectile in self.projectiles:
            projectile.move(vel)
            if projectile.off_screen(variables.Ygame1):
                self.projectiles.remove(projectile)
            else:
                for obj in objs:
                    if projectile.collision(obj):
                        objs.remove(obj)
                        if projectile in self.projectiles:
                            self.projectiles.remove(projectile)
                        return obj.get_var(), obj.get_ques()
        return [None,None]

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

    def __init__(self, x, y, var, ques, health=100):
        super().__init__(x, y, health)
        self.projectile_img = variables.bomb
        self.var = var
        self.ques = ques
        self.ship_img = self.variation[var]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel
        rando = random.randint(-1,1)
        if rando == -1:
            self.x -= vel*random.randint(1,3)
        elif rando == 1:
            self.x += vel*random.randint(1,3)

    def draw(self, window):
        super().draw(window)
        self.drawques(window)

    def drawques(self, window):
        if self.ques == 1:
            pygame.draw.circle(window, variables.RED, (self.x-1,self.y-1), 4)
        elif self.ques == 2:
            pygame.draw.circle(window, variables.OCEANBLUE, (self.x-1,self.y-1), 4)

    def get_ques(self):
        return self.ques

    def shoot(self):
        if self.cool_down_counter == 0:
            projectile = Projectile(self.x-20, self.y, self.projectile_img)
            self.projectiles.append(projectile)
            self.cool_down_counter = 1

    def get_var(self):
        return self.var


