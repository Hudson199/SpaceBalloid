import pygame
import math
import random
import datetime
from Library.Scripts import Block
pygame.init()

class Ball (object):

    def __init__(self, Center, Score, startspeed, maxspeed, drops):
##        print(self, '\n', Center)
        self.drops = drops
        self.Score = int(Score)
##        print('S0: '+str(self.Score))
##        print(self.Score, type(self.Score))
        self.poslist = []
        self.Delay = 2
        self.SpawnTime = datetime.datetime.now()
        self.MoveTime = datetime.timedelta(seconds=self.SpawnTime.second+self.Delay)
        self.CheckTime = self.MoveTime.seconds
        self.Moving = False
        self.DamageUp = False
##        print(self.SpawnTime)
##        print(self.MoveTime)
        self.img = pygame.image.load('Library\\Images\\Ball\\Img_Ball.png').convert_alpha()
        self.xVel = 0
        self.yVel = 0
        self.Damage = 1
        self.Direction = 0#random.uniform(-math.pi/4,math.pi/4)
        self.speedmax = maxspeed#25
        self.startspeed = startspeed
        self.speed = self.startspeed
##        print('Ball speed : ', self.speed)
        self.Width = 32
        self.Height = 32
        self.x = Center[0] - self.Width/2
        self.y = Center[1]*1.5 - self.Height/2
        self.rect = pygame.Rect(self.x, self.y, self.Width, self.Height)

    def FindSpeed(self):
        self.xVel = math.sin(self.Direction)*self.speed
        self.yVel = math.cos(self.Direction)*self.speed

    def BounceTop(self):
        if self.speed < self.speedmax:
            self.speed+=1
##        print('Ball speed : ', self.speed)
        AngleDiff = math.pi - self.Direction
        self.Direction += math.pi+(AngleDiff*2)
        self.FindSpeed()
    def BounceRight(self):
        if self.speed < self.speedmax:
            self.speed+=1
##        print('Ball speed : ', self.speed)
        AngleDiff = math.pi/2 - self.Direction
        self.Direction += math.pi+(AngleDiff*2)
        self.FindSpeed()
    def BounceLeft(self):
        if self.speed < self.speedmax:
            self.speed+=1
##        print('Ball speed : ', self.speed)
        AngleDiff = math.pi*1.5 - self.Direction
        self.Direction += math.pi+(AngleDiff*2)
        self.FindSpeed()
    def BounceBottom(self):
        if self.speed < self.speedmax:
            self.speed+=1
##        print('Ball speed : ', self.speed)
        AngleDiff = math.pi - self.Direction
        self.Direction += math.pi+(AngleDiff*2)
        self.FindSpeed()

    def MoveX(self, Blocks, Pad, parts):
        self.rect.x += self.xVel
        self.CollideBlocksX(Blocks, Pad, parts)
    def MoveY(self, Blocks, Pad, parts):
        self.rect.y += self.yVel
        self.CollideBlocksY(Blocks, Pad, parts)

    def CollideBlocksY(self, Blocks, Pad, parts):
        for block in Blocks:
            if self.rect.colliderect(block.rect):
                if self.yVel < 0  :
                    self.Score = block.RemoveBlock(Blocks, self.Score, self.drops, self.Damage, Pad, parts)
                    self.rect.top = block.rect.bottom
                    self.BounceBottom()
##                    print('Bounce Bottom')
                    break
                if self.yVel > 0  :
##                    print('S1:'+str(self.Score))
                    self.Score = block.RemoveBlock(Blocks, self.Score, self.drops, self.Damage, Pad, parts)
##                    print('S2:'+str(self.Score))
                    self.rect.bottom = block.rect.top
                    self.BounceTop()
##                    print('Bounce Top')
                    break
                    
    def CollideBlocksX(self, Blocks, Pad, parts):
        for block in Blocks:
            if self.rect.colliderect(block.rect):
                if self.xVel > 0   :
                    self.Score = block.RemoveBlock(Blocks, self.Score, self.drops, self.Damage, Pad, parts)
                    self.rect.right = block.rect.left
                    self.BounceRight()
##                    print('Bounce Right')
                    break
                if self.xVel < 0   :
                    self.Score = block.RemoveBlock(Blocks, self.Score, self.drops, self.Damage, Pad, parts)
                    self.rect.left = block.rect.right
                    self.BounceLeft()
##                    print('Bounce Left')
                    break

    def givedrops(self):
        return self.drops

    def Activate(self, name):
        if name == 'Damage':
            self.Damage *=  2
            self.stoptime = datetime.datetime.now().second + 15
            self.DamageUp = True
            self.img = pygame.image.load('Library\\Images\\Ball\\Img_Ball2.png').convert_alpha()
##            print('StopTime = '+str(self.stoptime))
            if self.stoptime >= 60:
                self.stoptime -= 60
            

    def Update(self, Display, clock, Pad, Blocks, parts):
##        print(datetime.datetime.now().second)
        self.poslist.append([self.rect.x, self.rect.y])
        if len(self.poslist) > 2:
            self.poslist.pop(0)
##        print(self, '\n', Display, '\n', clock, '\n', Pad, '\n', Blocks)
        self.SpawnTime = datetime.datetime.now()
        if self.MoveTime.seconds >= 60:
            self.CheckTime = int(self.MoveTime.seconds - 60)
##        print(self.SpawnTime.second, self.MoveTime.seconds)
        if int(self.SpawnTime.second) >= self.CheckTime:
            self.Moving = True
        if self.Moving == True:
            if self.DamageUp:
                if datetime.datetime.now().second == self.stoptime:
                    self.Damage = 1
                    self.img = pygame.image.load('Library\\Images\\Ball\\Img_Ball.png').convert_alpha()
                    self.DamageUp = False
                    self.stoptime = 62
            while self.Direction > math.pi*2 or self.Direction < 0:
                if self.Direction > math.pi*2:
                    self.Direction -= math.pi*2
                if self.Direction < 0:
                    self.Direction += math.pi*2
            self.FindSpeed()
            if self.rect.x + self.xVel + self.Width > 1240:
                self.BounceRight()
            if self.rect.y +self.yVel < 0:
                self.BounceTop()
            if self.rect.x + self.xVel < 0:
                self.BounceLeft()
            if self.rect.colliderect(Pad.rect) == 1:
                if self.speed < self.speedmax:
                    self.speed+=1
##                print('Ball speed : ', self.speed)
                self.rect.y = Pad.rect.y - self.Height - 4
                self.rect.bottom = Pad.rect.top
                AngleDiff = math.pi*2 - self.Direction
                BoardRange = Pad.Width/2
                SelfHitPoint = self.Width/2 + self.rect.x
                CollisionPoint = SelfHitPoint-(Pad.rect.x+Pad.Width/2)
                BoardBouncePercent = CollisionPoint/BoardRange
                if BoardBouncePercent<-1:
                    BoardBouncePercent = -1
                if BoardBouncePercent>1:
                    BoardBouncePercent = 1
                AngleAddHit = (math.pi/2)*BoardBouncePercent
    ##            print( AngleDiff, AngleAddHit, self.Direction)
                self.Direction += math.pi+(AngleDiff*2)-AngleAddHit
    ##            print(self.Direction)
                while self.Direction > math.pi*2 or self.Direction < 0:
                    if self.Direction > math.pi*2:
                        self.Direction -= math.pi*2
                    if self.Direction < 0:
                        self.Direction += math.pi*2
    ##            print(self.Direction)
                if self.Direction < -math.pi/2:
                    self.Direction += math.pi/2
                if self.Direction > math.pi*1.5:
                    self.Direction += math.pi/2
    ##            print(self.Direction)
                self.FindSpeed()
            if self.rect.y + self.yVel > 760:
                if Pad.Health == 0:
                    Pad.Dead = True
                self.speed = self.startspeed
                Pad.Health -= 1
                self.rect.y = self.y
                self.rect.x = self.x
                self.Direction = 0
                self.FindSpeed()
                self.MoveTime =  datetime.timedelta(seconds=self.SpawnTime.second+self.Delay)
                self.CheckTime = self.MoveTime.seconds
                self.Moving = False
##            print(self.poslist)
            if len(self.poslist) == 2:
                if self.poslist[0][1] == 0:
                    self.poslist[0][1] +=1
                elif self.poslist[1][1] == 0:
                    self.poslist[1][1] +=1
                if self.poslist[0][1]/self.poslist[1][1] == 1:
                    self.Direction+=0.01
            if self.xVel <= -9.99 or self.xVel >= 9.99 or self.Direction == math.pi/2 or self.Direction == math.pi*1.5:
                '''Turbulance'''
                self.Direction += 0.01
                self.FindSpeed()
            self.MoveX(Blocks, Pad, parts)
            self.MoveY(Blocks, Pad, parts)
##        print(('''
##xVel: {0}
##yVel: {1}
##Direction: {2}
##Rect: {3} ''').format( self.xVel, self.yVel, self.Direction, self.rect))
        Display.blit(self.img, self.rect)
