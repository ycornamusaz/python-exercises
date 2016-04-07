#!/usr/bin/python3.4

import pygame

########## DEFINE ZONE ##########

## Define screen size
LARGEUR = 700
HAUTEUR = 500

## Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

## Define loop status
done = False

speed = 3
player_x_speed = 0
player_y_speed = 0
player_x = 200
player_y = 200

########## INIT ZONE ##########

## Init pygame
pygame.init()

## Set window's size and open window
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))

## Set window's name
pygame.display.set_caption("My first window !!")

## Init clock
clock = pygame.time.Clock()

player_image = pygame.image.load("player.png").convert()
player_image.set_colorkey(BLACK)
background = pygame.image.load("Sample.png").convert()

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
            if event.key == pygame.K_w :
                player_y_speed = -speed
            elif event.key == pygame.K_s :
                player_y_speed = speed
            elif event.key == pygame.K_a :
                player_x_speed = -speed
            elif event.key == pygame.K_d :
                player_x_speed = speed
        elif event.type == pygame.KEYUP :
            if (event.key == pygame.K_w) or (event.key == pygame.K_s) :
                player_y_speed = 0
            elif (event.key == pygame.K_a) or (event.key == pygame.K_d) :
                player_x_speed = 0
        
    
    ########## LOGIC CODE ZONE ##########

    player_x += player_x_speed
    player_y += player_y_speed

    ########## CLEAR SCREEN ZONE ##########

    ## Set the entier screnn to white
    screen.fill(WHITE)


    ########## DRAWING CODE ZONE ##########
    
    screen.blit(background, [0,0])
    screen.blit(player_image, [player_x, player_y])

    ########## REFRESH SCREEN ZONE ##########

    ## Refresh screen
    pygame.display.flip()

    ## Set max framerate
    clock.tick(60)



























