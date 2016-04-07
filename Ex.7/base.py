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



    ########## CLEAR SCREEN ZONE ##########

    ## Set the entier screnn to white
    screen.fill(BLACK)


    ########## DRAWING CODE ZONE ##########
    
    

    ########## REFRESH SCREEN ZONE ##########

    ## Refresh screen
    pygame.display.flip()

    ## Set max framerate
    clock.tick(60)



























