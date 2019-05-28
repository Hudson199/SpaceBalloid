import pygame
import math
import random
from Library.Scripts import Drop, Particle
pygame.init()
#14*10 board, 84*32 px blocks

class Block (object):

    def __init__(self,Pos,BlockType,size):
        self.BlockType = BlockType
        self.Left = 45
        self.Top = 128
        self.Width = size[0]
        self.Height = size[1]
##        print(Pos)
        self.x = self.Left+(self.Width*Pos[0])
        self.y = self.Top+(self.Height*Pos[1])
        self.rect = pygame.Rect(self.x, self.y, self.Width, self.Height)
        BlockDict = {
            'W' : ['White',1,100,4], #Name, HP, Points, ParColor
            'Y' : ['Yellow',1,200,5],
            'N' : ['LightBlue',2,250,1],
            'B' : ['Blue',3,450,1],
            'H' : ['LightGreen',2,300,2],
            'G' : ['Green',3,500,2],
            'R' : ['Red',3,100,3],
            'L' : ['Black',20,1000,6]
            }
        self.t = 1
##        print(self.BlockType)
##        print(BlockDict.get(BlockType))
        self.pcolor = BlockDict.get(BlockType)[3]
        self.Name = BlockDict.get(BlockType)[0] + '_f1'
        self.HP = BlockDict.get(BlockType)[1]
        self.Points = BlockDict.get(BlockType)[2]
##        print('BlockType:', BlockType)
        self.img = pygame.image.load('Library\\Images\\Blocks\\Img_Block_'+self.Name+'.png').convert_alpha()
##        print(self.rect.x)

##    def CheckCollide(self, Ball, Blocks):
##        print(self, '\n', Ball, '\n', Blocks)
##        if self.rect.colliderect(Ball.rect) == 1:
##            Blocks.remove(self)
##            if Ball.xVel > 0:
##                Ball.BounceRight()
##            if Ball.xVel < 0:
##                Ball.BounceLeft()
##            if Ball.yVel > 0:
##                Ball.BounceBottom()
##            if Ball.yVel < 0:
##                Ball.BounceTop()
    def GetPoints(self, Score):
##        print('Block',Score, type(Score), self.BlockType)
##        print(Score, self.Points)
        return Score+self.Points

    def RemoveBlock(self, Blocks, Score, drops, damage, Pad, parts):
        
##        print('RemoveBlockScore: ' + str(Score))
        if self.BlockType != 'R':
            self.HP -= damage
        else:
            self.HP -=1
        if self.HP <= 0:
            for x in range(0,50,1): parts.append(Particle.Particle(self.rect.center,size=5,col=self.pcolor,speed=[500,2000]))
            Blocks.remove(self)
            Score = self.GetPoints(Score)
            roll = random.randint(0,100)
            if roll <=50: # 5% ?maybe less - 2%
                nameroll = random.randint (0,1000)
                if nameroll <= 50:
                    name = 'Extend'
                elif nameroll <= 100:
                    name = 'Health'
                elif nameroll <= 200:
                    name = 'Damage'
                else:
                    name = 'null'
                if not name == 'null':
                    drops.append(Drop.Drop(name,self.rect.center))
            if self.BlockType == 'R':
                Pad.Health -= 1
##            print('RemoveBlockScoreAfterHit: ' + str(Score))    
        elif self.HP > 0 and self.BlockType != 'L':
            CurrentFrame = int(self.Name[-1])
            TempName = self.Name[0:-1]
            if self.BlockType != 'R':
                CurrentFrame += damage
            else: CurrentFrame += 1
            NewName = TempName + str(CurrentFrame)
            self.Name = NewName
            self.img = pygame.image.load('Library\\Images\\Blocks\\Img_Block_'+self.Name+'.png').convert_alpha()
        return Score
        

    def Update(self, Display, Clock, Ball, Blocks, Score):
##        print('Start Block Update**********')
##        print(self, '\n', Display, '\n', Clock, '\n', Ball, '\n', Blocks)
##        self.CheckCollide(Ball, Blocks)
        Display.blit(self.img, self.rect)
        if self.BlockType == 'L':
            if isinstance(self.t, float):
                if str(self.t)[-1] == '0':
                    self.t = int(self.t)
            if isinstance(self.t, int):
                self.img = pygame.image.load('Library\\Images\\Blocks\\Img_Block_Black_f'+str(self.t)+'.png').convert()
            self.t+=0.25
##            print(self.t)
            if self.t == 29:
                self.t = 1
        return Score
        
