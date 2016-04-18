#!/usr/bin/python3.4

import pygame
import json

class Var():
    def __init__(self):
        ## Define screen size
        self.width = 1200
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
        ## Call the parent class (Sprite) constructor
        super().__init__()
        ## Import diferents classes
        color = Color()
        var = Var()

        ## Skin choice
        if skin == "male" :
            self.image = pygame.image.load("PNG/Players/bunny1_stand.png").convert()
            self.image.set_colorkey(color.BLACK)
        elif skin == "femal" :
            self.image = pygame.image.load("PNG/Players/bunny2_ready.png").convert()
            self.image.set_colorkey(color.BLACK)
        
        ## Get sprite position
        self.rect = self.image.get_rect()

        ## Get sprite width and height
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        #self.height_diff = 0
        ## Set diferents variables
        self.jump = 0
        self.speed_base = 5
        self.speed = 0
        self.run_time = 0
        ## Set player default position
        self.rect.y = var.height - 32 - 94 - self.height
        self.rect.x = 32

    def update(self, run) :
        ## Import diferents classes
        color = Color()
    
        ## Player animation
        if run == "right" :
            ## Each images alternate every 20 frames
            if self.run_time < 20: 
                self.image = pygame.image.load("PNG/Players/bunny1_walk1_r.png").convert()
                self.run_time += 1
            elif self.run_time < 40 :
                self.run_time += 1
                self.image = pygame.image.load("PNG/Players/bunny1_walk2_r.png").convert()
            else :
                self.run_time = 0
        elif run == "stand" :
            self.image = pygame.image.load("PNG/Players/bunny1_stand.png").convert()
            self.run_time = 0
        elif run == "left" :
            ## Each images alternate every 20 frames
            if self.run_time < 20: 
                self.image = pygame.image.load("PNG/Players/bunny1_walk1_l.png").convert()
                self.run_time += 1
            elif self.run_time < 40 :
                self.run_time += 1
                self.image = pygame.image.load("PNG/Players/bunny1_walk2_l.png").convert()
            else :
                self.run_time = 0
        
        self.image.set_colorkey(color.BLACK)
        #self.height_diff = (self.image.get_height() - self.height)
        #self.width_diff = (self.image.get_width() - self.width)
        #self.rect.y -= self.height_diff
        #self.rect.x -= self.height_diff
        #self.width = self.image.get_width()
        #self.height = self.image.get_height()

class Ground(pygame.sprite.Sprite):
    
    def __init__(self):
        ## Call the parent class (Sprite) constructor
        super().__init__()
        ## Import diferents classes
        color = Color()
        var = Var()

        ## Import picture
        self.image = pygame.image.load("PNG/Environment/ground_grass.png").convert()
        ## Set the background to transparent
        self.image.set_colorkey(color.BLACK)

        ## Get sprite position
        self.rect = self.image.get_rect()
        ## Get sprite width and height
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.y = var.height - 16 - 94
        self.rect.x = 32

class Buton(pygame.sprite.Sprite):

    def __init__(self, text, color_txt):
        ## Call the parent class (Sprite) constructor
        super().__init__()
        ## Import diferents classes
        color = Color()
        var = Var()

        ## Import picrure
        self.image = pygame.image.load("PNG/Environment/ground_grass.png").convert()
        ## Set the background to transparent
        self.image.set_colorkey(color.BLACK)

        ## Get sprite position
        self.rect = self.image.get_rect()
        ## Get sprite width and height
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect.x = (var.width/2 - self.width/2)
        self.rect.y = 32

        ## Set text content
        self.text = text
        ## Set text color
        self.color = color_txt
        ## Set font and font size
        self.font = pygame.font.SysFont("Ubuntu", 25)
        ## Creat text object
        self.textSurf = self.font.render(self.text, 1, self.color)
        ## Get the text object width and height
        self.text_width = self.textSurf.get_width()
        self.text_height = self.textSurf.get_height()
        ## Fuse text object with the buton
        self.image.blit(self.textSurf, ((self.width/2 - self.text_width/2), (self.height/2 - self.text_height/2)))
    def update(self, text, color_txt):
        ## Import diferents classes
        color = Color()
        var = Var()

        ## Update text
        self.text = text
        ## Update text color
        self.color = color_txt
        ## Set font and font size
        self.font = pygame.font.SysFont("Ubuntu", 25)
        ## Creat text object
        self.textSurf = self.font.render(self.text, 1, self.color)
        ## Get the text object width and height
        self.text_width = self.textSurf.get_width()
        self.text_height = self.textSurf.get_height()
        ## Fuse text object with the buton
        self.image.blit(self.textSurf, ((self.width/2 - self.text_width/2), (self.height/2 - self.text_height/2)))

class Pointer(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        ## Import diferents classes
        color = Color()
        var = Var()

        ## Create a surface of 1x1 px
        self.image = pygame.Surface((1, 1))
        ## Set color to white
        self.image.fill(color.WHITE)
        ## Get sprite position
        self.rect = self.image.get_rect()
        ## Set default sprite position
        self.rect.x = 1
        self.rect.y = 1

class Background() :
    def __init__(self) :
        ## Import diferents classes
        var = Var()
        color = Color()

        ## Import background pictures (don't convert picture to pygame format to keep transarence)
        self.bg1_base = pygame.image.load("PNG/Background/bg_layer1.png")#.convert()
        self.bg2_base = pygame.image.load("PNG/Background/bg_layer2.png")#.convert()
        self.bg3_base = pygame.image.load("PNG/Background/bg_layer3.png")#.convert()
        self.bg4_base = pygame.image.load("PNG/Background/bg_layer4.png")#.convert()

        ## Creat background surface
        self.bg = pygame.Surface([var.width, var.height])

        ## Resize background pictures
        self.bg1 = pygame.transform.scale(self.bg1_base, (var.width, var.height))
        self.bg2 = pygame.transform.scale(self.bg2_base, (var.width, var.height))
        self.bg3 = pygame.transform.scale(self.bg3_base, (var.width, var.height))
        self.bg4 = pygame.transform.scale(self.bg4_base, (var.width, var.height))
        
        ## Fuse background onto background surface
        self.bg.blit(self.bg1, [0, 0])
        self.bg.blit(self.bg2, [0, 0])
        self.bg.blit(self.bg3, [0, 0])
        self.bg.blit(self.bg4, [0, 0])

    def update(self, screen) :
        ## Print background on screen
        screen.blit(self.bg, [0, 0])

class Game :
    def menu():
        ## Init pygame
        pygame.init()
        ## Import diferents classes
        var = Var()
        color = Color()
        ## Init screen
        screen = pygame.display.set_mode([var.width, var.height])
        ## Init windows title
        pygame.display.set_caption("JUMPER !!!")
        ## Init clock
        clock = pygame.time.Clock()
        ## Menu loop stat
        done_menu = False
        ## Game start stat
        game_start = False
        ## Set background
        background = Background()
        ## Create menu sprite group
        buton_list = pygame.sprite.Group()
        all_menu_sprites_list = pygame.sprite.Group()
        ## Create pointer sprite
        pointer = Pointer()
        ## Add pointer to menu sprite's group
        all_menu_sprites_list.add(pointer)
        ## Create butons
        buton1 = Buton("Play", color.WHITE)
        buton2 = Buton("Options", color.WHITE)
        ## Set buton1 pos
        buton1.rect.x = (var.width/2 - buton1.width/2)
        buton1.rect.y = (var.height/2 - buton1.height/2 - 100)
        ## Set buton2 pos
        buton2.rect.x = (var.width/2 - buton2.width/2)
        buton2.rect.y = (var.height/2 - buton2.height/2 + 100)
        ## Add butons to buton list
        buton_list.add(buton1)
        buton_list.add(buton2)
        ## Add butons to menu sprite's group
        all_menu_sprites_list.add(buton1)
        all_menu_sprites_list.add(buton2)
    
        ## Start loop
        while not done_menu :
            
            ########## EVENT ZONE ##########
        
            ## For every events, filter event and refresh screen
            for event in pygame.event.get() :
        
                ## Filter events
                ## If the cross is pressed, quit game
                if event.type == pygame.QUIT :
                    done_menu = True
                ## If any mouse buton is pressed 
                if event.type == pygame.MOUSEBUTTONDOWN :
                    ## Update mouse pos
                    pos = pygame.mouse.get_pos()
                    pointer.rect.x = pos[0]
                    pointer.rect.y = pos[1]
                    ## If pointer is on buton1, start game
                    if (event.button == 1) and (pointer.rect.x >= buton1.rect.x) and (pointer.rect.x <= (buton1.rect.x + buton1.width)) and (pointer.rect.y >= buton1.rect.y) and (pointer.rect.y <= (buton1.rect.y + buton.height)) :
                        game_start = True
                        
        
            ########## LOGIC CODE ZONE ##########
            
            ## Update mouse pos
            pos = pygame.mouse.get_pos()
            pointer.rect.x = pos[0]
            pointer.rect.y = pos[1]
            
            ## Detect colision between pointer and buton group
            buton_pointer_list = pygame.sprite.spritecollide(pointer, buton_list, True)
            
            ## If a colision is detected
            if buton_pointer_list != [] :
                ## For each buton who are in colision with pointer
                for buton in buton_pointer_list :
                    ## Update text color to red
                    buton.update(buton.text , color.RED)
                    ## Re-add buton to sprite list
                    buton_list.add(buton)
                    all_menu_sprites_list.add(buton)
            ## If not
            else :
                ## For all butons 
                for buton in buton_list :
                    ## Update text color to white
                    buton.update(buton.text, color.WHITE)
            
            ## If game have to start
            if game_start == True :
                ## Start game
                Game.game()
                ## Reset game_start variable
                game_start = False
        
            ########## CLEAR SCREEN ZONE ##########
        
            ## Set the entier screnn to white
            #screen.fill(color.BLACK)
            background.update(screen)
        
            ########## DRAWING CODE ZONE ##########
            
            ## Draw all sprites to the screen
            all_menu_sprites_list.draw(screen)
        
            ########## REFRESH SCREEN ZONE ##########
        
            ## Refresh screen
            pygame.display.flip()
        
            ## Set game tick (per second)
            clock.tick(60)
    
    def game() :
        ## Init values
        JUMP = 0
        C_base = -109
        C = C_base
        GROUND = 0
        ## Import diferents classes
        var = Var()
        color = Color()
        ## Init screen        
        screen = pygame.display.set_mode([var.width, var.height])
        ## Init clock
        clock = pygame.time.Clock()
        ## Set background
        background = Background()
        ## Set game loop stat
        done_game = False
        ## Create game sprite groups
        player_list = pygame.sprite.Group()
        ground_list = pygame.sprite.Group()
        movable_list = pygame.sprite.Group()
        all_game_sprites_list = pygame.sprite.Group()
        ## Create player and set player direction
        player = Player("male")
        direction = "stand"
        ## Add player to gamesprite's group
        movable_list.add(player)
        ## Add player to movable group
        all_game_sprites_list.add(player)

        json_data = open("map.json")
        map_data = json.load(json_data)

        i = 0
        for blocks in map_data["Level_1"][0]["Block"] :
            x = map_data["Level_1"][0]["Block"][i]["x"]
            y = map_data["Level_1"][0]["Block"][i]["y"]
            ground0 = Ground()
            ground0.rect.x = x
            ground0.rect.y = y
            last_ground = ground0
            all_game_sprites_list.add(ground0)
            ground_list.add(ground0)
            movable_list.add(ground0)
            i += 1

        ## Create ground blocks
        #ground1 = Ground()
        #ground2 = Ground()
        ### Init value
        #last_ground = ground2
        ### Add ground blocks to game sprite's group
        #all_game_sprites_list.add(ground1)
        #all_game_sprites_list.add(ground2)
        ### Add ground blocks to ground group 
        #ground_list.add(ground1)
        #ground_list.add(ground2)
        ### Add ground blocks to movable group
        #movable_list.add(ground1)
        #movable_list.add(ground2)
        ### Set ground2 block position
        #ground2.rect.x += 400
        #ground2.rect.y -= 100
        #print(ground2.rect.x)
        #print(" " + str(ground2.rect.y))

        ## Start game loop
        while not done_game :
                
            ########## EVENT ZONE ##########
        
            ## For every events, filter event and refresh screen
            for event in pygame.event.get() :
        
                ## Filter events
                ## If the cross is pressed, quit game
                if event.type == pygame.QUIT :
                    done_game = True
                ## If any key is pressed
                elif event.type == pygame.KEYDOWN :
                    ## If right key is pressed
                    if event.key == pygame.K_RIGHT :
                        ## Move player to right
                        player.speed = player.speed_base
                        ## Change animation
                        direction = "right"
                    ## If left key is pressed
                    elif event.key == pygame.K_LEFT :
                        ## Move player to left
                        player.speed = -(player.speed_base)
                        ## Change animation
                        direction = "left"
                    ## If key up is pressed
                    elif event.key == pygame.K_UP :
                        ## Check if player in on the ground before jump
                        if GROUND == 1 :
                            last_player_y = player.rect.y
                            JUMP = 1
                ## If key is release
                elif event.type == pygame.KEYUP : 
                    ## If key right or key left is release 
                    if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_LEFT) :
                        ## Set player speed to 0
                        player.speed = 0
                        direction = "stand"
        
        
            ########## LOGIC CODE ZONE ##########
            
            ## Quit game if player is out of screen
            if player.rect.y > var.height :
                done_game = True
            
            if (player.rect.x + player.width) > (var.width - var.width/3) :
                for test in movable_list :
                    test.rect.x -= 5
            if player.rect.x < (var.width/16) :
                for test in movable_list :
                    test.rect.x += 5

            ## Jump process
            if (JUMP == 1) :
                if (C < -(C_base)) :
                    player.rect.y = (last_player_y - (-(C/10)**2+120))
                    C += 3
                    GROUND = 0
                else :
                    ## Reset var
                    JUMP = 0
                    C = C_base
                    GROUND = 0
                    player.rect.y += 9

            ## Update player position
            player.rect.x += player.speed
            
            ## Detect colisions between player and ground block
            ground_player_list = pygame.sprite.spritecollide(player, ground_list, True)
            ## If a colision is detected
            if ground_player_list != [] :
                ## For each blocks in colision
                for ground in ground_player_list :
                    ## If the player is enter into the block by the top
                    if (player.rect.y + player.height) <= (ground.rect.y + 3) :
                        ## Set ground vlue to true
                        GROUND = 1
                        ## Stop jump 
                        JUMP = 0
                        ## Reset jump counter
                        C = C_base
                        ## Set player pos to the top of the block
                        player.rect.y = ground.rect.y - player.height
                        last_ground = ground
                    ## If the player is enter into the block by the right side
                    elif (player.rect.x + player.width) >= (ground.rect.x) and (player.rect.x + player.width) <= (ground.rect.x + ground.width) :
                        ## Move the player out of the block
                        player.rect.x -= player.speed_base
                        ## Gravity
                        player.rect.y += 3
                    ## If the player is enter into the block by the left side
                    elif (player.rect.x) < (ground.rect.x + ground.width) and (player.rect.x) > (ground.rect.x) :
                        ## Move the player out of the block
                        player.rect.x = (ground.rect.x + ground.width)
                        ## Gravity
                        player.rect.y += 3
                    ## If the player is enter into the block by the bottom
                    elif (player.rect.y) <= (groung.rect.y + ground.height + 1) and player.rect.y > (ground.rect.y + ground.height + 10) :
                        ## Move the player out of the block
                        player.rect.y = (ground.rect.y + ground.height)
                        ## Gravity
                        player.rect.y += 3
                    ## Re-add block to default group
                    movable_list.add(ground)
                    ground_list.add(ground)
                    all_game_sprites_list.add(ground)
            ## If the player isn't on the block or down the block
            elif (player.rect.x + player.width) <= (last_ground.rect.x) or (player.rect.x) >= (last_ground.rect.x + last_ground.width) or (player.rect.y) >= (last_ground.rect.y + last_ground.height) : 
                ## Set groud val to 0
                GROUND = 0
                ## Gravity
                player.rect.y += 3

            ## Update player animation
            player.update(direction)
        
            ########## CLEAR SCREEN ZONE ##########
        
            ## Set the entier screnn to white
            #screen.fill(color.BLACK)
            background.update(screen)
        
            ########## DRAWING CODE ZONE ##########
            
            ## Draw all sprites to the screen
            all_game_sprites_list.draw(screen)
        
            ########## REFRESH SCREEN ZONE ##########
        
            ## Refresh screen
            pygame.display.flip()
        
            ## Set game tick (per second)
            clock.tick(120)

Game.menu()
