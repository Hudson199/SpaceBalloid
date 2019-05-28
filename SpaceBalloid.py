import pygame, sys
from pygame.locals import *
import random
import os , os.path
import math
import glob
import datetime
from Library.Scripts import (
    Paddle,
    Ball,
    Block
    )
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
clock = pygame.time.Clock()
Display = pygame.display.set_mode((1240,720))
Center = (620,360)
inittime = datetime.datetime.now()
pygame.display.set_caption('SpaceBalloid')
pygame.mouse.set_cursor(*pygame.cursors.tri_left)
blocksize = [84,32]
print ( len(glob.glob('*')) )
if blocksize != [84,32]:
    pass
##pygame.mixer.init()
##pygame.mixer.music.set_volume(.1)
##pygame.mixer.set_num_channels(4)

Colors    = [
(   0,   0,   0),#black  0
( 255, 255, 255),#white  1
(   0, 255,   0),#green  2
( 255,   0,   0),#red    3
( 150,   0, 150),#purple 4
( 100, 100, 100),#grey   5
( 205, 202,   0),#bright yellow 6
(  40,  40,  40),#dark grey 7
(  18, 188,  13),#light green 8
(  80,   0,   0),#dark red 9
(   0,  80,   0) #dark green 10

]

ImagesToLoad = [
    'MainBG1.png',
    'MainBG2.png'
    ]

fonts = [
    pygame.font.SysFont("Matura MT Script Capitals",32), #0
    pygame.font.SysFont("Britannic Bold",32),            #1
    pygame.font.SysFont("Imprint MT Shadow",32),         #2
    pygame.font.SysFont("Sitka Small",32),               #3
    pygame.font.SysFont("Magneto",64),                   #4
    pygame.font.SysFont("Georgia",64),                   #5
    pygame.font.SysFont("Georgia",48),                   #6
    pygame.font.SysFont("Georgia",32),                   #7
    pygame.font.SysFont("Castellar",64)                  #8
    ]

def LoadImages(ImageList):
    LoadedImages=[]
    for Image in ImageList:
        LoadedImg = LoadImage(Image).convert_alpha()
        LoadedImg.set_colorkey((0,0,0))
        LoadedImg.set_alpha(255)
        LoadedImages.append(LoadedImg)
        
    return LoadedImages
def LoadImage(ImageName):
    return pygame.image.load('Library\\Images\\BG\\' + ImageName)
Images = LoadImages(ImagesToLoad)

def TextToSprite(Text,Font,Color,Pos):
    TextSurf = fonts[Font].render(Text,1,(Colors[Color]))
    TextWidth = TextSurf.get_width()
    TextHeight = TextSurf.get_height()
    PosAlt = {
        'CornTopL' : (0,0),
        'MidTop' : (Center[0]-TextWidth/2,(Center[1]/2)-TextHeight/2),
        'CornTopR' : (1240-TextWidth,0),
        'MidMid' : (Center[0]-TextWidth/2,Center[1]-TextHeight/2),
        'CornBotL' : (0,720-TextHeight),
        'MidBot' : (Center[0]-TextWidth/2,(Center[1]*1.5)-TextHeight/2),
        'CornBotR' : (1240-TextWidth,720-TextHeight)
        }
    return [pygame.Rect(PosAlt.get(Pos)[0],PosAlt.get(Pos)[1],TextWidth,TextHeight),TextSurf]
    
    
def StartLoop(Sprites=0,Funcs=0,Params=0,BG=0):
    pyevents = pygame.event.get()
    if BG == 0:
        Display.fill((0,0,0))
    else:
        Display.blit(BG,(0,0))
    if Sprites !=0:
        for Sprite in Sprites:
            Display.blit(Sprite[1],(Sprite[0]))
    for event in pyevents: 
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            pos = pygame.mouse.get_pos()
            if Funcs != 0:
                Clicked = [s for s in (Sprites) if s[0].collidepoint(pos)]
                for Clickable in Sprites:
                    if Clickable in Clicked:
                        if Params == 0:
                            Funcs[Sprites.index(Clickable)]()
                        else:
##                            print(Params)
                            if Params[Sprites.index(Clickable)] == None:
                                Funcs[Sprites.index(Clickable)]()
                            else:
                                if isinstance(Params[Sprites.index(Clickable)],list or tuple):
##                                    print(len(Params[Sprites.index(Clickable)]))
##                                    print(Params[Sprites.index(Clickable)])
                                    if len(Params[Sprites.index(Clickable)])>1:
                                        Funcs[Sprites.index(Clickable)](Params[Sprites.index(Clickable)][0],Params[Sprites.index(Clickable)][1])
                                Funcs[Sprites.index(Clickable)](Params[Sprites.index(Clickable)])
                        
def EndLoop():
        pygame.display.update()
        clock.tick(60)
        pygame.display.flip()
        
def Main():
    UsedSprites = [
        TextToSprite('New',5,4,'MidTop'),
        TextToSprite('Continue',5,4,'MidMid'),
        TextToSprite('Exit',5,4,'MidBot')
        ]
    UsedFuncs = [
        StartNewGameSelect,
        StartOldGameSelect,
        Exit
        ]
    UsedParams = [
        ]
    while True:
        StartLoop(UsedSprites,UsedFuncs,Params = 0,BG=Images[0])
        EndLoop()
        
def Exit():
    pygame.quit()
    sys.exit()

def StartNewGameSelect():
    UsedSprites = [
        TextToSprite('Slot 1',5,4,'MidTop'),
        TextToSprite('Slot 2',5,4,'MidMid'),
        TextToSprite('Slot 3',5,4,'MidBot'),
        TextToSprite('Go Back',5,4,'CornBotL')
        ]
    UsedFuncs = [
        StartNewGame,
        StartNewGame,
        StartNewGame,
        Main
        ]
    UsedParams = [
        1,
        2,
        3,
        None
        ]
    while True:
        StartLoop(UsedSprites,UsedFuncs,UsedParams,BG=Images[0])
        EndLoop()
        
def StartNewGame(Save):
    File = open('Library\\Save\\'+str(Save)+'.txt','w')
    File.write('1-1'+'\n'+'0'+'\n'+'2'+'\n'+'3'+'\n'+'0'+'\n'+'0')
    File.close()
    StartGame('1-1',Save)
    
def StartOldGameSelect():
    UsedSprites = [
        TextToSprite('Slot 1',5,4,'MidTop'),
        TextToSprite('Slot 2',5,4,'MidMid'),
        TextToSprite('Slot 3',5,4,'MidBot'),
        TextToSprite('Go Back',5,4,'CornBotL')
        ]
    UsedFuncs = [
        StartOldGame,
        StartOldGame,
        StartOldGame,
        Main
        ]
    UsedParams = [
        1,
        2,
        3,
        None
        ]
    while True:
        StartLoop(UsedSprites,UsedFuncs,UsedParams,BG=Images[0])
        EndLoop()
def StartOldGame(Save):
    File = open('Library\\Save\\'+str(Save)+'.txt','r')
    Level = File.readline().rstrip('\n')
    File.close()
    StartGame(Level,Save)
        
def StartGame(Level, Save):
    Leveltext = Level
    SaveFile = open('Library\\Save\\'+str(Save)+'.txt')
    lines = [line.rstrip('\n') for line in SaveFile.readlines()]
    Score = int(lines[1])
    Segs = int(lines[2])
    Health = int(lines[3])
    Freeplay = int(lines[4])
##    print('Score = '+Score)
    SaveFile.close()
    Score = int(Score)
    ScoreText = fonts[5].render(str(Score),1,Colors[4])
##    print('Level:' , Level,'Save:', Save)
    if Freeplay != 1:
        LevelFile = open('Library\\Levels\\'+Level+'.txt')
        FileList = LevelFile.readlines()
        SortedList = []
        for line in FileList:
            SortedList.append(line.rstrip('\n'))
##      print(FileList,'\n',SortedList,'\n')
        LevelFile.close()
        x = y = 0
        blocks = []
        for Line in SortedList:
            for Char in Line:
                if not Char == '.':
##                    print(Char)
                    blocks.append(Block.Block((x,y),Char,blocksize))
                x+=1
            y+=1
            x=0
    else:
        dictblock = {
                1 : 'W',
                2 : 'Y',
                3 : 'N',
                4 : 'B',
                5 : 'H',
                6 : 'G',
                7 : 'R',
                8 : 'L'
            }
        x = y = 0
        blocks = []
        for line in range(0,10,1):#10
            for char in range(0,14,1):#14
                blocks.append(Block.Block((x,y),(dictblock.get(random.randint(1,8)))))
                x+=1
            y+=1
            x=0
        Leveltext = 'Freeplay'
##    print(blocks)
    PlayerPaddle = Paddle.Paddle(Center, Segs, Health)
    PlayerPaddle.Segs = Segs
    PlayerPaddle.Health = Health
    drops = []
    GameBall = Ball.Ball(Center, Score, int(Level[2])+4, int(Level[0])*3+6, drops)
##    print(str(GameBall.Score))
    UsedSprites = [
        TextToSprite('Go Back',5,4,'CornBotL'),
        TextToSprite(str(Leveltext),5,4,'CornTopR')
        ]
    UsedFuncs = [
        Main,
        Nothing
        ]
    PaddleUps = ['Extend', 'Health']
    BallUps = ['Damage']
    parts = []
    while True:
        StartLoop(UsedSprites,UsedFuncs,BG=Images[1])
        ScoreText = fonts[5].render(str(GameBall.Score),1,Colors[4])
        KeyDown = pygame.key.get_pressed()
        blocktypes = []
        for block in blocks:
            blocktypes.append(block.BlockType)
            block.Update(Display, clock, GameBall, blocks, Score)
##            print(block.BlockType, len(list(set(blocktypes))))
        if blocks == [] or (len(set(blocktypes))==1 and blocks[0].BlockType == 'R'):
            NextLevel(Level, Save, GameBall.Score, PlayerPaddle.Segs, PlayerPaddle.Health)
        GameBall.Update(Display, clock, PlayerPaddle, blocks, parts)
        drops = GameBall.givedrops()
        for part in parts:
            part.Update(Display,parts,[0,0,0,0,1,0,0,0,0,0])
        for drop in drops:
            drop.Update(Display)
            if drop.rect.colliderect(PlayerPaddle.rect):
                if drop.Name in PaddleUps:
                    PlayerPaddle.Activate(drop.Name)
                elif drop.Name in BallUps:
                    GameBall.Activate(drop.Name)
##                else:
##                    print('Error: powerup not listed in ups lists')
                drops.remove(drop)
            if drop.rect.y >= 760:
                drops.remove(drop)
        PlayerPaddle.Update(Display, clock)
        if PlayerPaddle.Health < 0:
            PlayerPaddle.Dead = True
        if PlayerPaddle.Dead:
            GameOver(str(Level),str(Score))
        if KeyDown[pygame.K_RIGHT]:
            PlayerPaddle.MoveRight()
        if KeyDown[pygame.K_LEFT]:
            PlayerPaddle.MoveLeft()
        if not 1 in pygame.key.get_pressed():
            PlayerPaddle.NoMove()
        Display.blit(ScoreText,(0,0))
        EndLoop()
        
def NextLevel(CurrentLevel, Save, Points, Segs, Health):
##    print(CurrentLevel, Save)
##    print(CurrentLevel[2])
##    print(str(int(CurrentLevel[2])+1))
##    print(CurrentLevel[0:2])
    File = open('Library\\Save\\'+str(Save)+'.txt', 'r')
    lines = [line.rstrip('\n') for line in File.readlines()]
##    print(lines)
    DoCongrats = False
    NextLevel = str(CurrentLevel[0:2]) + str( int(CurrentLevel[2])+1 ) 
    if NextLevel[2] == '6':
        NextLevel = str(int(NextLevel[0])+1) + '-1'
    if NextLevel == '6-1':
        if lines[5] == '0':
            DoCongrats = True
        NextLevel = '5-5'
    File = open('Library\\Save\\'+str(Save)+'.txt', 'w')
    if DoCongrats :
        File.write(str(NextLevel) + '\n' + str(Points) + '\n' + str(Segs) + '\n' + str(Health) + '\n' + '1' + '\n' + '1')
        File.close()
        Congrats()
    else:
        if lines[4] == '1':
            File.write(str(NextLevel) + '\n' + str(Points) + '\n' + str(Segs) + '\n' + str(Health) + '\n' + '1' + '\n' +'1')
        File.write(str(NextLevel) + '\n' + str(Points) + '\n' + str(Segs) + '\n' + str(Health) + '\n' + '0')
        File.close()
##    print(lines)
    StartGame(NextLevel, Save)

def Congrats():
    UsedSprites = [
        TextToSprite('Congratulations!',5,4,'MidTop'),
        TextToSprite('Freeplay Time! (Hard)',5,4,'MidMid'),
        TextToSprite('Okay',5,4,'MidBot')
        ]
    UsedFuncs = [
        Nothing,
        Nothing,
        StartGame
        ]
    UsedParams = [
        None,
        None,
        ['5-5', 1]
        ]
    while True:
        StartLoop(UsedSprites, UsedFuncs,UsedParams, BG=Images[0])
        EndLoop()

def GameOver(level,score):
    UsedSprites = [
        TextToSprite('Back',5,4,'MidBot'),
        TextToSprite(score,5,4,'MidMid'),
        TextToSprite(level,5,4,'MidTop')
        ]
    UsedFuncs = [
        Main,
        Nothing,
        Nothing
        ]
    while True:
        StartLoop(UsedSprites,UsedFuncs,BG=Images[0])
        Display.blit(fonts[5].render('Game Over!',1,Colors[4]),(Center[0]-fonts[5].render('Game Over!',1,Colors[4]).get_width()/2,0))
        EndLoop()

def Nothing(Nothing = None):
    pass

if __name__ == '__main__':    Main()
