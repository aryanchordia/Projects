import pygame
import random
import time

window = pygame.display.set_mode((800, 600))



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, swing, left, right):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = None
        self.team = None
        #lets me know if the bat is upright or not
        self.swing = swing
        #lets me know if i have swung left 
        #(self.swing will also be true in this case.)
        self.left = left
        #lets me know if i have swung right 
        #(self.swing will also be true in this case.)
        self.right = right
        #the images of the bat (one is rotated 90 left and one 90 right
        #and the other is upright)
        self.image = [(pygame.transform.smoothscale \
                      (pygame.image.load('bs.png'), \
                      (self.width, self.height))), \
                      (pygame.transform.smoothscale \
                      (pygame.image.load('br.png'), \
                      (self.width, self.height))), \
                      (pygame.transform.smoothscale \
                      (pygame.image.load('bl.png'), \
                      (self.width, self.height)))] 



    def draw(self, window):
        if self.swing == False:
            window.blit(self.image[0], (self.x, self.y))
            
        else:
            if self.left == True:
                window.blit(self.image[2], (self.x, self.y))
            if self.right == True:
                window.blit(self.image[1], (self.x, self.y))

     