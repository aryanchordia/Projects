import pygame 
import random
from Player import Player
import math


window = pygame.display.set_mode((800, 600))



class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y, width, height, isCaught):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isBowled = False
        self.velXR = random.randint(7, 45)
        self.velXL = random.randint(-45, -7)
        self.velY = random.randint(6, 11)        
        self.image = pygame.transform.smoothscale \
                    (pygame.image.load('ball.png'), \
                     (self.width, self.height))
        self.isCaught = isCaught
        #all the condiditons needed for when it 
        #collides with a specific fielder. 
        #They are set to true if yes
        #in the main loop
        self.isMovingBack1 = False
        self.isMovingBack2 = False
        self.isMovingBack3 = False
        self.isMovingBack4 = False
        self.isMovingBack5 = False
        self.isMovingBack6 = False

        
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        


    def update(self):
        #this is the bowling fucntion
        if self.y < 340 and self.isCaught == False:
            self.y += self.velY



    def hitLeft(self):
    #for when i swing left 
        self.x += self.velXL
        self.y -= self.velY

    def hitRight(self):
    #for when i swing right
        self.x += self.velXR
        self.y -= self.velY

    
    



