import pygame
from Ball import Ball

#this is the class for all the fielders
class Opponents(pygame.sprite.Sprite):
    def __init__(self, image, x, y, width, height):
    	pygame.sprite.Sprite.__init__(self)
    	self.x = x
    	self.y = y
    	self.width = width
    	self.height = height
    	self.image = image


    def draw(self, window):
    	#images defined in main loop, image loads at the specific 
        #x, y attributes we defined in the main loop.
        window.blit(self.image, (self.x, self.y))
        

    