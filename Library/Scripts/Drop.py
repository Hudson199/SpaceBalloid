import pygame
def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

class Drop (object):

    def __init__(self, Name, Pos):

        self.Name = Name
        self.x = Pos[0]
        self.y = Pos[1]
        self.size = 64
        self.speed = 3
        self.rotating = 4
        self.angle = 0
        self.Fimg = pygame.image.load('Library\\Images\\Drops\\'+Name + 'F.png').convert_alpha()
        self.Bimg = pygame.image.load('Library\\Images\\Drops\\'+Name + 'B.png').convert_alpha()
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
##        print(('''
##Drop info:
##Name: {0}
##x : {1}
##y : {2}
##speed: {3}
##self.Fimg : {4}
##self.Bimg : {5}
##self.rect : {6}''').format(self.Name, self.x, self.y, self.speed, self.Fimg, self.Bimg, self.rect))

    def Update(self, Display):
        self.rect.y += self.speed
        self.angle += self.rotating
        if self.angle >= 360:
            self.angle -= 360
        self.BimgNew = pygame.transform.rotate(self.Bimg, self.angle).convert_alpha()
        self.BrectNew = self.BimgNew.get_rect()
        self.BrectNew.center = self.rect.center
        Display.blit(self.BimgNew, self.BrectNew)
        Display.blit(self.Fimg, self.rect)
