#!/usr/bin/python3.4

import pygame

def var(self):
    ## Define screen size
    self.WIDTH = 1300
    self.HEIGHT = 1000

def color(self):
    ## Define some colors
    self.BLACK    = (   0,   0,   0)
    self.WHITE    = ( 255, 255, 255)
    self.BLUE     = (   0,   0, 255)
    self.GREEN    = (   0, 255,   0)
    self.RED      = ( 255,   0,   0)

class Player(pygame.sprite.Sprite):

    def __init__(self, skin):
        # Call the parent class (Sprite) constructor
        super().__init__()

        if skin == "male" :
            self.image = pygame.image.load("PNG/Players/bunny1_ready.png").convert()
            self.image.set_colorkey(color.BLACK)
        elif skin == "femal" :
            self.image = pygame.image.load("PNG/Players/bunny2_ready.png").convert()
            self.image.set_colorkey(color.BLACK)

        self.rect = self.image.get_rect()

        self.width = 120
        self.height = 191
        self.jump = 0
        self.speed = 0
        self.rect.y = var.HEIGHT - 32 - 94 - self.height
        self.rect.x = 32

class Ground(pygame.sprite.Sprite):
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("PNG/Environment/ground_grass.png").convert()
        self.image.set_colorkey(color.BLACK)

        self.rect = self.image.get_rect()

        self.width = 380
        self.height = 94
        self.jump = 0
        self.speed = 0
        self.rect.y = var.HEIGHT - 16 - 94
        self.rect.x = 32

class Buton(pygame.sprite.Sprite):

    def __init__(self, text, color):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load("PNG/Environment/ground_grass.png").convert()
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.width = 380
        self.height = 94
        self.jump = 0
        self.speed = 0
        self.rect.x = (var.width/2 - self.width/2)
        self.rect.y = 32

        self.text = text
        self.color = color
        self.font = pygame.font.SysFont("Ubuntu", 25)
        self.textSurf = font.render(self.text, 1, self.color)
        self.text_width = self.textSurf.get_width()
        self.text_height = self.textSurf.get_height()
        self.image.blit(self.textSurf, ((self.width/2 - self.text_width/2), (self.height/2 - self.text_height/2)))

