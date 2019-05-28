import pygame
import random
import os
import math
import sys
from Library.Scripts import Particle
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
clock = pygame.time.Clock()
Display = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
screensize = (pygame.display.Info().current_w,pygame.display.Info().current_h)
Display = pygame.display.set_mode((1240,720))
##Display = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
Center = (620,360)
pygame.display.set_caption('SpaceBalloid')
pygame.mouse.set_cursor(*pygame.cursors.tri_left)
pygame.mixer.init()
pygame.mixer.music.set_volume(.1)
pygame.mixer.set_num_channels(4)

def main():
    '''
Buttons:
A = Add particles 
R = Randoms size 
F = Fullscreen
C = Change colour
Buttons '1' to '-' = add mode (each toggle)

Sliders:
1 = size
2 = speed
3 = number

Modes:
1 = vortex
2 = sin()
2 = cos()
3 = tan()
5 = gravity
6 = shoot down
7 = revese vortex
8 = shoot up
9 = bounces
0 = freeze
- = random speed
'''
    global Display
    particles = []
    add = False
    mode = [0,0,0,0,0,0,0,0,0,0,0]
    print(Display)
    ran = True
    sizerect = pygame.Rect(0,16,4,16)
    speedrect = pygame.Rect(0,32,4,16)
    numrect = pygame.Rect(0,48,4,16)
    psize = 1
    full = False
    pfac = [1,2]
    pspeed= [1,2]
    num = 3
    colour = 1
    rancol = False
    imgdict = {
            1 : 'Blue',
            2 : 'Green',
            3 : 'Red',
            4 : 'White',
            5 : 'Yellow',
            6 : 'Purple',
            7 : 'Random'
            }
    while True:
        Display.fill((10,10,10))
        pyevents = pygame.event.get()
        for event in pyevents: 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
                pos = pygame.mouse.get_pos()
##                particles.append(Particle.Particle(pos, ransize=True, fac=(2,25),size=25, col=6,ran=False))
            if event.type == pygame.KEYDOWN and event.key == 32:
                particles = []
            if (event.type == pygame.KEYDOWN and event.unicode == 'a') or (event.type == pygame.KEYDOWN and event.unicode == 'A') :
                if add:
                    add = False
                else:
                    add = True
            if (event.type == pygame.KEYDOWN and event.unicode == 'f') or (event.type == pygame.KEYDOWN and event.unicode == 'F') :
                if full:
                    full = False
                    Display = pygame.display.set_mode((1240,720))
                else:
                    full = True
                    Display = pygame.display.set_mode((screensize),pygame.FULLSCREEN)
            if (event.type == pygame.KEYDOWN and event.unicode == 'r') or (event.type == pygame.KEYDOWN and event.unicode == 'R') :
                if ran:
                    ran = False
                else:
                    ran = True
            if (event.type == pygame.KEYDOWN and event.unicode == 'c') or (event.type == pygame.KEYDOWN and event.unicode == 'C') :
                colour+=1
                if colour == 7:
                    rancol = True
                if colour == 8:
                    colour = 1
                    rancol = False
            if event.type == pygame.KEYDOWN and event.unicode == '1':
                if mode[0] == 1:
                    mode[0] = 0
                else:
                    mode[0] = 1 #vortex
            if event.type == pygame.KEYDOWN and event.unicode == '2':
                if mode[1] == 1:
                    mode[1] = 0
                else:
                    mode[1] = 1 #sin
            if event.type == pygame.KEYDOWN and event.unicode == '3':
                if mode[2] == 1:
                    mode[2] = 0
                else:
                    mode[2] = 1 #cos
            if event.type == pygame.KEYDOWN and event.unicode == '4':
                if mode[3] == 1:
                    mode[3] = 0
                else:
                    mode[3] = 1 #tan
            if event.type == pygame.KEYDOWN and event.unicode == '5':
                if mode[4] == 1:
                    mode[4] = 0
                else:
                    mode[4] = 1 #gravity
            if event.type == pygame.KEYDOWN and event.unicode == '6':
                if mode[5] == 1:
                    mode[5] = 0
                else:
                    mode[5] = 1 #shoot down
            if event.type == pygame.KEYDOWN and event.unicode == '7':
                if mode[6] == 1:
                    mode[6] = 0
                else:
                    mode[6] = 1 #reverse vortex
            if event.type == pygame.KEYDOWN and event.unicode == '8':
                if mode[7] == 1:
                    mode[7] = 0
                else:
                    mode[7] = 1 #shoot up
            if event.type == pygame.KEYDOWN and event.unicode == '9':
                if mode[8] == 1:
                    mode[8] = 0
                else:
                    mode[8] = 1 #particles bounce
            if event.type == pygame.KEYDOWN and event.unicode == '0':
                if mode[9] == 1:
                    mode[9] = 0
                else:
                    mode[9] = 1 # freeze
            if event.type == pygame.KEYDOWN and event.unicode == '-':
                if mode[10] == 1:
                    mode[10] = 0
                else:
                    mode[10] = 1
        pos = pygame.mouse.get_pos()
        pygame.draw.line(Display,(100,100,100),(2,24),(302,24))
        pygame.draw.line(Display,(100,100,100),(2,40),(302,40))
        pygame.draw.line(Display,(100,100,100),(2,56),(302,56))
        if 0 < pos[0] < 300 and 16 <  pos[1] < 32:
            pygame.draw.rect(Display,(200,200,200),sizerect)
            if pygame.mouse.get_pressed()[0]:
                sizerect.left = pos[0]
                portion = (sizerect.left)/300
##                print(portion)
                psize = math.ceil(100*portion)
                pfac[0] = math.floor(psize/10)
                pfac[1] = math.ceil(psize)
                
        else:
            pygame.draw.rect(Display,(100,100,100),sizerect)
        if 0 < pos[0] < 300 and 32 <  pos[1] < 48:
             pygame.draw.rect(Display,(200,200,200),speedrect)
             if pygame.mouse.get_pressed()[0]:
                speedrect.left = pos[0]
                portion = math.e**(10*speedrect.left/300)
                pspeed[0] = math.ceil(portion/25)
                pspeed[1] = math.ceil(portion)
        else:
             pygame.draw.rect(Display,(100,100,100),speedrect)
        if 0 < pos[0] < 300 and 48 <  pos[1] < 64:
             pygame.draw.rect(Display,(200,200,200),numrect)
             if pygame.mouse.get_pressed()[0]:
                numrect.left = pos[0]
                portion = (1000*numrect.left)/300
##                print(portion)
                num = math.floor(portion)
        else:
             pygame.draw.rect(Display,(100,100,100),numrect)
        modetext = pygame.font.SysFont('Consolas',12).render(str(mode)+'  '+str(add) + '  ' + str(ran)+'  '+str(full) + '  '+str(imgdict.get(colour))+'  FPS: '+ str(clock.get_fps()) +'  Particles: ' + str(len(particles)),1,(100,100,100))
        Display.blit(modetext,(0,0))
        if add:
            for x in range(0,num,1):  particles.append(Particle.Particle(pos, ransize=ran, fac=pfac,size=psize, col=colour,ran=rancol,speed=pspeed,deg = mode[10]))
        for particle in particles:
            particle.Update(Display, particles, mode)
        pygame.display.update()
        clock.tick(60)
        pygame.display.flip()
main()
                
