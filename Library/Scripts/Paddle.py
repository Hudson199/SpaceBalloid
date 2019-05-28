import pygame
import math
pygame.init()

class Paddle(object):
    
    def __init__(self,Center, Segs=2, Health=3):
        self.img = pygame.image.load('Library\\Images\\Paddle\\Img_Paddle1.png').convert_alpha()
        self.Segimg = pygame.image.load('Library\\Images\\Paddle\\Img_Paddle_Segment.png').convert_alpha()
        self.xVel = 0
        self.MaxVel = 50
        self.Dead = False
        self.Health = Health
        self.Accel = 1.5
        self.Decel = -2
        self.Height = 0 #35
        self.Segs = Segs
        self.Width = self.Segs*32 #+65
        self.x = Center[0]-self.Width/2
        self.y = (Center[1]*1.75)-self.Height/2
        self.rect = pygame.Rect(self.x, self.y, self.Width, self.Height)
        self.HitWall = False

    def MoveLeft(self):
        if self.xVel - self.Accel > -self.MaxVel :
            if self.xVel > 0 :
                self.xVel -= self.Accel*1.75
            else:
                self.xVel -= self.Accel

    def MoveRight(self):
        if self.xVel + self.Accel < self.MaxVel :
            if self.xVel < 0:
                self.xVel += self.Accel*1.75
            else:
                self.xVel += self.Accel

    def NoMove(self):
        if self.xVel > 0:
            self.xVel += self.Decel
        if self.xVel < 0:
            self.xVel -= self.Decel
        if -2 <= self.xVel <= 2:
            self.xVel = 0

    def Activate(self, Name):
        if Name == 'Extend':
            self.Extend()
        elif Name == 'Health':
            self.AddHealth()
        else:
            print('Error: No listed powerup for paddle')
            
    def Extend(self):
        if self.Segs < 13:
            self.Segs += 1
            self.Width += 32
            self.rect.width += 32
        
    def AddHealth(self):
        if self.Health < 10:
            self.Health +=1

    def Update(self, Display, clock):
##        print( ( '''
##paddle xVel: {0}
##paddle xPos: {1}
##paddle MaxVel: {2}
##paddle Width: {3}
##Paddle Segments: {4} ''').format( self.xVel, self.rect.x, self.MaxVel, self.Width, self.Segs))
        #'Display.blit(self.img,self.rect)
        for seg in range(0,self.Segs,1):
            Display.blit(self.Segimg,(self.rect.x+seg*32, self.rect.y))
        for health in range(0,self.Health,1):
            Display.blit(pygame.transform.scale(self.img,(32,16)),(1240-120-(health*40),700))
        if (self.rect.x + self.xVel + self.Width < 1240) and (self.rect.x + self.xVel > 0):
            self.rect.x += self.xVel
        elif (self.rect.x + self.xVel + self.Width > 1240):
            self.rect.x = 1240 - self.Width
            self.xVel = -self.xVel/2
        elif (self.rect.x + self.xVel < 0):
            self.rect.x = 0
            self.xVel = -self.xVel/2
