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

y_vitesse = 0
x_vitesse = 0
direct_y = 0
direct_x = 0
rect_x = 50
rect_y = 50

########## INIT ZONE ##########

## Init pygame
pygame.init()

## Set window's size and open window
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))

## Set window's name
pygame.display.set_caption("My first window !!")

## Init clock
clock = pygame.time.Clock()

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
            if event.key == pygame.K_LEFT :
                x_vitesse = -3
            elif event.key == pygame.K_RIGHT :
                x_vitesse = 3
            elif event.key == pygame.K_UP :
                y_vitesse = -3
            elif event.key == pygame.K_DOWN :
                y_vitesse = 3
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_vitesse = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_vitesse = 0
    
    ########## LOGIC CODE ZONE ##########

    ########## CLEAR SCREEN ZONE ##########

    ## Set the entier screnn to white
    screen.fill(BLACK)


    ########## DRAWING CODE ZONE ##########
    
    
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    rect_x += x_vitesse
    rect_y += y_vitesse

    ########## REFRESH SCREEN ZONE ##########

    ## Refresh screen
    pygame.display.flip()

    ## Set max framerate
    clock.tick(60)



























