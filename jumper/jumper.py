#!/usr/bin/python3.4

import pygame

########## DEFINE ZONE ##########

## Define screen size
LARGEUR = 1300
HAUTEUR = 1000

## Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

SOL = 0
JUMP = 0
C = 0

## Define loop status
done = False

class Player(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, skin):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        if skin == "male" :
            self.image = pygame.image.load("PNG/Players/bunny1_ready.png").convert()
            self.image.set_colorkey(BLACK)
        elif skin == "femal" :
            self.image = pygame.image.load("PNG/Players/bunny2_ready.png").convert()
            self.image.set_colorkey(BLACK)
        elif skin == "male_run" :
            self.image = pygame.image.load("PNG/Players/bunny1_walk1.png").convert()
            self.image.set_colorkey(BLACK)
        elif skin == "femal_run" :
            self.image = pygame.image.load("PNG/Players/bunny2_walk1.png").convert()
            self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        
        self.width = 120
        self.height = 191
        self.jump = 0
        self.speed = 0
        self.rect.y = HAUTEUR - 32 - 94 - self.height 
        self.rect.x = 32

class Ground(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        # 380 x 94
        self.image = pygame.image.load("PNG/Environment/ground_grass.png").convert()
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        
        self.width = 380
        self.height = 94
        self.jump = 0
        self.speed = 0
        self.rect.y = HAUTEUR - 16 - 94
        self.rect.x = 32

########## INIT ZONE ##########

## Init pygame
pygame.init()

## Set window's size and open window
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))

## Set window's name
pygame.display.set_caption("My first window !!")

## Init clock
clock = pygame.time.Clock()

sol_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

player = Player("male")

terre1 = Ground()
terre2 = Ground()

all_sprites_list.add(terre1)
all_sprites_list.add(terre2)

sol_list.add(terre1)
sol_list.add(terre2)

terre2.rect.x += 450
terre2.rect.y -= 100

all_sprites_list.add(player)


########## LOOP ZONE ##########

## Start loop
while not done :
    
    ########## EVENT ZONE ##########

    ## For every events, filter event and refresh screen
    for event in pygame.event.get() :

        ## Filter events
        if event.type == pygame.QUIT :
            done = True
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                player.speed = 5
            elif event.key == pygame.K_LEFT :
                player.speed = -5
            elif event.key == pygame.K_UP :
                if SOL == 1 :
                    JUMP = 1

        elif event.type == pygame.KEYUP : 
            if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_LEFT) :
                player.speed = 0



    ########## LOGIC CODE ZONE ##########

    if player.rect.y > HAUTEUR :
        pygame.quit()

    if (JUMP == 1) :
        if (C < 34) :
            player.rect.y = player.rect.y - C
            C += 3
        else : 
            JUMP = 0
            C = 0
            SOL = 0
    
    player.rect.y += 3

    player.rect.x += player.speed

    terre_player_list = pygame.sprite.spritecollide(player, sol_list, True)
    
    for sol in terre_player_list :
        if (player.rect.y + player.height) <= (sol.rect.y + 3) :
            SOL = 1
            player.rect.y -= 3
        elif (player.rect.x + player.width) >= (sol.rect.x) and (player.rect.x + player.width) <= (sol.rect.x + sol.width) :
            player.rect.x -= 5
        elif (player.rect.x) <= (sol.rect.x + sol.width) and (player.rect.x) >= (sol.rect.x) :
            player.rect.x += 5
        sol_list.add(sol)
        all_sprites_list.add(sol)


    ########## CLEAR SCREEN ZONE ##########

    ## Set the entier screnn to white
    screen.fill(BLACK)


    ########## DRAWING CODE ZONE ##########
    
    all_sprites_list.draw(screen)

    ########## REFRESH SCREEN ZONE ##########

    ## Refresh screen
    pygame.display.flip()

    ## Set max framerate
    clock.tick(60)



























