import random
import math
import pygame

class Particle(object):

    def __init__(self, pos, ransize=False , fac=(2,4), size=2, col=4, ran=False,speed=[1,2],deg=0):
        self.pos = pos
        self.radius = 400
        self.x = pos[0]
        self.y = pos[1]
        self.Gravity = .4
        self.bounce =0
        if ran:
            col = random.randint(1,6)
        imgdict = {
            1 : 'Blue',
            2 : 'Green',
            3 : 'Red',
            4 : 'White',
            5 : 'Yellow',
            6 : 'Purple'
            }
        suffix = imgdict.get(col)
        self.img = pygame.image.load('Library\\Images\\Particles\\Par_'+suffix+'.png').convert()
        if not ransize:
            if not size == 2:
                self.img = pygame.transform.scale(self.img,(size,size))
                self.rect = self.img.get_rect()
        elif ransize:
            size = random.randint(fac[0],fac[1])
            self.img = pygame.transform.scale(self.img,(size,size))
            self.rect = self.img.get_rect()
        self.Direction = random.uniform(0,math.pi*2)
        if deg==0:
            self.OSpeed = random.randint(speed[0],speed[1])/100
            self.Speed = self.OSpeed
            self.Component = [self.Speed*math.sin(self.Direction),self.Speed*math.cos(self.Direction)]
        elif deg == 1:
            self.OSpeed = speed[1]/200
            self.Speed = self.OSpeed
            self.Component = [self.Speed*math.sin(self.Direction),self.Speed*math.cos(self.Direction)]
            
    def ChangeDirection(self, mode):
        if mode[0] == 1:
            self.Direction += .1 #  try smaller number = bigger vortex
            self.Component = [self.Speed*math.sin(self.Direction),self.Speed*math.cos(self.Direction)]
        if mode[1] == 1:
            self.Direction = math.sin(self.Direction)
            self.Component = [self.Speed*math.sin(self.Direction),self.Speed*math.cos(self.Direction)]
        if mode[2] == 1:
            self.Direction = math.cos(self.Direction)
            self.Component = [self.Speed*math.sin(self.Direction),self.Speed*math.cos(self.Direction)]
        if mode[3] == 1:
            self.Direction = math.tan(self.Direction)
            self.Component = [self.Speed*math.sin(self.Direction),self.Speed*math.cos(self.Direction)]
        if mode[4] == 1:
            if self.Component[1] <15:
                self.Component[1] += self.Gravity
            if self.Component[1] >= 15:
                self.Component[1] *=0.95
            if not self.Component[0] > -7 or not self.Component[0] < 7:
                self.Component[0] *= 0.9
        if mode[5] == 1:
            self.Direction *= (self.Direction*.001)
            self.Component = [self.Speed*math.sin(self.Direction),self.Speed*math.cos(self.Direction)]
        if mode[6] == 1:
            self.Direction -= .2
            self.Component = [self.Speed*math.sin(self.Direction),self.Speed*math.cos(self.Direction)]
        if mode[7] == 1:
            self.Direction = math.pi
            self.Component = [self.Speed*math.sin(self.Direction),self.Speed*math.cos(self.Direction)]

    def Update(self, Display, particles, mode):
        '''mode format: [0,0,0,0,0,0,0,0,0], 1=on'''
        Display.blit(self.img,(self.x,self.y))
##        if not self.x in range(self.pos[0]-self.radius,self.pos[0]+self.radius) and not self.y in range(self.pos[1]-self.radius,self.pos[1]+self.radius):
##            particles.remove(self)
        if mode[8] == 0:
            self.Speed = self.OSpeed
            if self.x > Display.get_width() or self.y > Display.get_height() or self.x < 0 or self.y <0:
                particles.remove(self)
        elif mode[8] == 1:
            if self.x + self.Component[0] < 0:
                self.Speed*=.9
                AngleDiff = math.pi*1.5 - self.Direction
                self.Direction += math.pi+(2*AngleDiff)
                self.Component = [self.Speed*math.sin(self.Direction),self.Speed*math.cos(self.Direction)]
                self.bounce+=1
            if self.x + self.rect.bottom + self.Component[0] > Display.get_width():
                self.Speed*=.9
                AngleDiff = math.pi/2 - self.Direction
                self.Direction += math.pi+(2*AngleDiff)
                self.Component = [self.Speed*math.sin(self.Direction),self.Speed*math.cos(self.Direction)]
                self.bounce+=1
            if self.y  + self.Component[1] < 0:
                self.Speed*=.9
                AngleDiff = math.pi - self.Direction
                self.Direction += math.pi+(2*AngleDiff)
                self.Component = [self.Speed*math.sin(self.Direction),self.Speed*math.cos(self.Direction)]
                self.bounce+=1
            if self.y + self.rect.right + self.Component[1] > Display.get_height():
                self.Speed*=.9
                AngleDiff = math.pi - self.Direction
                self.Direction += math.pi+(2*AngleDiff)
                self.Component = [self.Speed*math.sin(self.Direction),self.Speed*math.cos(self.Direction)]
                self.bounce+=1
            if self.Speed < 0.2 and self.bounce > 100:
                particles.remove(self)
        if not mode[9] == 1:
            self.x+=self.Component[0]
            self.y+=self.Component[1]
            self.ChangeDirection(mode)
        
