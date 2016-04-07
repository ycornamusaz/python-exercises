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

vitesse = 5
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
    
    ########## LOGIC CODE ZONE ##########

    if (rect_x >= (LARGEUR-50)) :
        direct_x = 1
    elif (rect_x <= 0) :
        direct_x = 0
    if (rect_y >= (HAUTEUR-50)) :
        direct_y = 1
    elif (rect_y <= 0) :
        direct_y = 0
    ########## CLEAR SCREEN ZONE ##########

    ## Set the entier screnn to white
    screen.fill(BLACK)


    ########## DRAWING CODE ZONE ##########
    
    
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    if (direct_x == 0) :
        rect_x += vitesse
    else :
        rect_x -= vitesse
    if (direct_y == 0) :
        rect_y += vitesse
    else :
        rect_y -= vitesse

    ########## REFRESH SCREEN ZONE ##########

    ## Refresh screen
    pygame.display.flip()

    ## Set max framerate
    clock.tick(60)



























