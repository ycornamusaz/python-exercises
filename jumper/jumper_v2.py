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
            self.image = pygame.image.load("PNG/Players/bunny1_stand.png").convert()
            self.image.set_colorkey(color.BLACK)
        elif skin == "femal" :
            self.image = pygame.image.load("PNG/Players/bunny2_ready.png").convert()
            self.image.set_colorkey(color.BLACK)

        self.rect = self.image.get_rect()

        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.height_diff = 0
        self.jump = 0
        self.speed_base = 5
        self.speed = 0
        self.run_time = 0
        self.rect.y = var.height - 32 - 94 - self.height
        self.rect.x = 32

    def update(self, run) :
        color = Color()

        if run == "right" :
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
            if self.run_time < 20: 
                self.image = pygame.image.load("PNG/Players/bunny1_walk1_l.png").convert()
                self.run_time += 1
            elif self.run_time < 40 :
                self.run_time += 1
                self.image = pygame.image.load("PNG/Players/bunny1_walk2_l.png").convert()
            else :
                self.run_time = 0
        
        self.image.set_colorkey(color.BLACK)
        self.height_diff = (self.image.get_height() - self.height)
        self.width_diff = (self.image.get_width() - self.width)
        self.rect.y -= self.height_diff
        self.rect.x -= self.height_diff
        self.width = self.image.get_width()
        self.height = self.image.get_height()

class Ground(pygame.sprite.Sprite):
    
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        color = Color()
        var = Var()

        self.image = pygame.image.load("PNG/Environment/ground_grass.png").convert()
        self.image.set_colorkey(color.BLACK)

        self.rect = self.image.get_rect()

        self.width = self.image.get_width()
        self.height = self.image.get_height()
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
        self.width = self.image.get_width()
        self.height = self.image.get_height()
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

class Background() :
    def __init__(self) :
        var = Var()
        color = Color()

        self.bg1_base = pygame.image.load("PNG/Background/bg_layer1.png")#.convert()
        self.bg2_base = pygame.image.load("PNG/Background/bg_layer2.png")#.convert()
        self.bg3_base = pygame.image.load("PNG/Background/bg_layer3.png")#.convert()
        self.bg4_base = pygame.image.load("PNG/Background/bg_layer4.png")#.convert()

        self.bg = pygame.Surface([var.width, var.height])

        self.bg1 = pygame.transform.scale(self.bg1_base, (var.width, var.height))
        self.bg2 = pygame.transform.scale(self.bg2_base, (var.width, var.height))
        self.bg3 = pygame.transform.scale(self.bg3_base, (var.width, var.height))
        self.bg4 = pygame.transform.scale(self.bg4_base, (var.width, var.height))
        
        self.bg.blit(self.bg1, [0, 0])
        self.bg.blit(self.bg2, [0, 0])
        self.bg.blit(self.bg3, [0, 0])
        self.bg.blit(self.bg4, [0, 0])

    def update(self, screen) :
        screen.blit(self.bg, [0, 0])

class Game :
    def menu():
        
        pygame.init()
        
        var = Var()
        color = Color()
    
        screen = pygame.display.set_mode([var.width, var.height])
    
        pygame.display.set_caption("JUMPER !!!")
    
        clock = pygame.time.Clock()
    
        done_menu = False
    
        game_start = False
    
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
        while not done_menu :
            
            ########## EVENT ZONE ##########
        
            ## For every events, filter event and refresh screen
            for event in pygame.event.get() :
        
                ## Filter events
                if event.type == pygame.QUIT :
                    done_menu = True
                if event.type == pygame.MOUSEBUTTONDOWN :
                    pos = pygame.mouse.get_pos()
                    pointer.rect.x = pos[0]
                    pointer.rect.y = pos[1]
                    if (event.button == 1) and (pointer.rect.x >= buton1.rect.x) and (pointer.rect.x <= (buton1.rect.x + buton1.width)) and (pointer.rect.y >= buton1.rect.y) and (pointer.rect.y <= (buton1.rect.y + buton.height)) :
                        game_start = True
                        
        
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
    
            if game_start == True :
                Game.game()
                game_start = False
        
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
    
    def game() :
        
        JUMP = 0
        C_base = -109
        C = C_base
        GROUND = 0

        var = Var()
        color = Color()
        
        screen = pygame.display.set_mode([var.width, var.height])
        clock = pygame.time.Clock()
        background = Background()

        done_game = False
    
        player_list = pygame.sprite.Group()
        ground_list = pygame.sprite.Group()
        all_game_sprites_list = pygame.sprite.Group()
    
        player = Player("male")
        direction = "stand"
    
        all_game_sprites_list.add(player)
    
        ground1 = Ground()
        ground2 = Ground()

        last_ground = ground2
    
        all_game_sprites_list.add(ground1)
        all_game_sprites_list.add(ground2)
    
        ground_list.add(ground1)
        ground_list.add(ground2)
    
        ground2.rect.x += 600
        ground2.rect.y -= 100
    
        while not done_game :
                
            ########## EVENT ZONE ##########
        
            ## For every events, filter event and refresh screen
            for event in pygame.event.get() :
        
                ## Filter events
                if event.type == pygame.QUIT :
                    done_game = True
                elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RIGHT :
                        player.speed = player.speed_base
                        direction = "right"
                    elif event.key == pygame.K_LEFT :
                        player.speed = -(player.speed_base)
                        direction = "left"
                    elif event.key == pygame.K_UP :
                        if GROUND == 1 :
                            last_player_y = player.rect.y
                            JUMP = 1
        
                elif event.type == pygame.KEYUP : 
                    if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_LEFT) :
                        player.speed = 0
                        direction = "stand"
        
        
            ########## LOGIC CODE ZONE ##########
            
            if player.rect.y > var.height :
                done_game = True

            if (JUMP == 1) :
                if (C < -(C_base)) :
                    player.rect.y = (last_player_y - (-(C/10)**2+120))
                    C += 3
                else :
                    JUMP = 0
                    C = C_base
                    GROUND = 0
                    player.rect.y += 9

            player.rect.x += player.speed
        
            ground_player_list = pygame.sprite.spritecollide(player, ground_list, True)
            
            if ground_player_list != [] :
                for ground in ground_player_list :
                    if (player.rect.y + player.height) <= (ground.rect.y + 3) :
                        GROUND = 1
                        JUMP = 0
                        C = C_base
                        player.rect.y = ground.rect.y - player.height
                        last_ground = ground
                    elif (player.rect.x + player.width) >= (ground.rect.x) and (player.rect.x + player.width) <= (ground.rect.x + ground.width) :
                        player.rect.x -= player.speed_base
                        player.rect.y += 3
                    elif (player.rect.x) < (ground.rect.x + ground.width) and (player.rect.x) > (ground.rect.x) :
                        player.rect.x = (ground.rect.x + ground.width)
                        player.rect.y += 3
                    elif (player.rect.y) <= (groung.rect.y + ground.height + 1) and player.rect.y > (ground.rect.y + ground.height - 10) :
                        player.rect.y = (ground.rect.y + ground.height)
                        player.rect.y += 3
                    ground_list.add(ground)
                    all_game_sprites_list.add(ground)
            elif (player.rect.x + player.width) <= (last_ground.rect.x) or (player.rect.x) >= (last_ground.rect.x + last_ground.width) : 
                GROUND = 0
                player.rect.y += 3

            player.update(direction)
        
            ########## CLEAR SCREEN ZONE ##########
        
            ## Set the entier screnn to white
            #screen.fill(color.BLACK)
            background.update(screen)
        
            ########## DRAWING CODE ZONE ##########
            
            all_game_sprites_list.draw(screen)
        
            ########## REFRESH SCREEN ZONE ##########
        
            ## Refresh screen
            pygame.display.flip()
        
            ## Set max framerate
            clock.tick(120)

Game.game()
