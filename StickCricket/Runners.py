import pygame

window = pygame.display.set_mode((800, 600))

#loading all the images	
runBack = [pygame.image.load('runBack1.png'), \
		   pygame.image.load('runBack2.png'), \
		   pygame.image.load('runBack3.png'), \
       	   pygame.image.load('runBack4.png'), \
       	   pygame.image.load('runBack5.png'), \
       	   pygame.image.load('runBack6.png'), \
       	   pygame.image.load('runBack7.png'), \
       	   pygame.image.load('runBack8.png'), \
       	   pygame.image.load('runBack9.png')]


class Runner(pygame.sprite.Sprite):

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.yChange = 5
		self.start = False
		self.rU = False
		self.rB = False
		self.runCount = 0

	def draw(self, window):
		#inherited directly from tech with tim - youtube
		if self.runCount + 1 >= 27:
			self.runCount = 0
		if self.rU:
			window.blit(runUp[self.runCount//3], (self.x, self.y))
			self.runCount += 1
		elif self.rB:
			self.start = True
			window.blit(runBack[self.runCount//3], (self.x, self.y))
			self.runCount += 1
		else:
			window.blit(runBack[0], (370, 180))


""" Citation - The way I made the images in a list and and then 
               integer divided by 3 as the window is runing
               at 27 frames per second, idea came from and 
               inherited directly from tech with tim - youtube channel
               also self.runCount all got from him."""