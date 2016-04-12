#!/usr/bin/python3.4

import pygame

class Var():
    def __init__(self):
        ## Define screen size
        self.width = 1300
        self.height = 1000

class Color():
    def __init__(self):
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
        color = Color()
        var = Var()

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
        self.rect.y = var.height - 32 - 94 - self.height
        self.rect.x = 32

class Ground(pygame.sprite.Sprite):
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        color = Color()
        var = Var()

        self.image = pygame.image.load("PNG/Environment/ground_grass.png").convert()
        self.image.set_colorkey(color.BLACK)

        self.rect = self.image.get_rect()

        self.width = 380
        self.height = 94
        self.jump = 0
        self.speed = 0
        self.rect.y = var.height - 16 - 94
        self.rect.x = 32

class Buton(pygame.sprite.Sprite):

    def __init__(self, text, color_txt):
        # Call the parent class (Sprite) constructor
        super().__init__()
        color = Color()
        var = Var()

        self.image = pygame.image.load("PNG/Environment/ground_grass.png").convert()
        self.image.set_colorkey(color.BLACK)

        self.rect = self.image.get_rect()
        self.width = 380
        self.height = 94
        self.jump = 0
        self.speed = 0
        self.rect.x = (var.width/2 - self.width/2)
        self.rect.y = 32

        self.text = text
        self.color = color_txt
        self.font = pygame.font.SysFont("Ubuntu", 25)
        self.textSurf = self.font.render(self.text, 1, self.color)
        self.text_width = self.textSurf.get_width()
        self.text_height = self.textSurf.get_height()
        self.image.blit(self.textSurf, ((self.width/2 - self.text_width/2), (self.height/2 - self.text_height/2)))
    def update(self, color_txt):
        color = Color()
        var = Var()

        self.color = color_txt
        self.font = pygame.font.SysFont("Ubuntu", 25)
        self.textSurf = self.font.render(self.text, 1, self.color)
        self.text_width = self.textSurf.get_width()
        self.text_height = self.textSurf.get_height()
        self.image.blit(self.textSurf, ((self.width/2 - self.text_width/2), (self.height/2 - self.text_height/2)))

class Pointer(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        color = Color()
        var = Var()

        self.image = pygame.Surface((1, 1))
        self.image.fill(color.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 1
        self.rect.y = 1

def menu():
    
    pygame.init()
    
    var = Var()
    color = Color()

    screen = pygame.display.set_mode([var.width, var.height])

    pygame.display.set_caption("JUMPER !!!")

    clock = pygame.time.Clock()

    done = False

    buton_list = pygame.sprite.Group()
    all_menu_sprites_list = pygame.sprite.Group()

    pointer = Pointer()
    
    all_menu_sprites_list.add(pointer)

    buton1 = Buton("Play", color.WHITE)
    buton2 = Buton("Options", color.WHITE)
    
    buton1.rect.x = (var.width/2 - buton1.width/2)
    buton1.rect.y = (var.height/2 - buton1.height/2 - 100)

    buton2.rect.x = (var.width/2 - buton2.width/2)
    buton2.rect.y = (var.height/2 - buton2.height/2 + 100)

    buton_list.add(buton1)
    buton_list.add(buton2)

    all_menu_sprites_list.add(buton1)
    all_menu_sprites_list.add(buton2)

    ## Start loop
    while not done :
        
        ########## EVENT ZONE ##########
    
        ## For every events, filter event and refresh screen
        for event in pygame.event.get() :
    
            ## Filter events
            if event.type == pygame.QUIT :
                done = True
    
        ########## LOGIC CODE ZONE ##########
        
        pos = pygame.mouse.get_pos()
        pointer.rect.x = pos[0]
        pointer.rect.y = pos[1]

        buton_pointer_list = pygame.sprite.spritecollide(pointer, buton_list, True)
        
        if buton_pointer_list != [] :
            for buton in buton_pointer_list :
                buton.update([255,0,0])
                
                buton_list.add(buton)
                all_menu_sprites_list.add(buton)
        else :
            for buton in buton_list :
                buton.update([255,255,255])
    
        ########## CLEAR SCREEN ZONE ##########
    
        ## Set the entier screnn to white
        screen.fill(color.BLACK)
    
    
        ########## DRAWING CODE ZONE ##########
        
        all_menu_sprites_list.draw(screen)
    
        ########## REFRESH SCREEN ZONE ##########
    
        ## Refresh screen
        pygame.display.flip()
    
        ## Set max framerate
        clock.tick(60)

menu()
