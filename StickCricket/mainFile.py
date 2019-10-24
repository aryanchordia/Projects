#Aryan Chordia 15-112 TP mainfile

import pygame
import random
import time
from Player import Player
from Ball import Ball
from Opponents import Opponents
from Runners import Runner

#importing all the required classes (saved in same directory)


pygame.init()
#initializing pygame window


#setting these variables all here as they will be global
window = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()   
pygame.display.set_caption("TP3")
background = (pygame.image.load('finalPitch.jpg'))
image1 = (pygame.image.load('images.jpeg'))
score = 0
wickets = 0
ballsLeft = 42
oppScore = random.randint(100, 160)

#varibale to control the view of the 
#game screen and whether player wins or looses
initV = True
winGame = False
loseGame = False


#importing all the fielder images to be used

opp = [pygame.transform.smoothscale(pygame.image.load("f1.png"), (30, 30)), \
	   pygame.transform.smoothscale(pygame.image.load("f2.png"), (30, 30)), \
	   pygame.transform.smoothscale(pygame.image.load("f2.png"), (30, 30)), \
	   pygame.transform.smoothscale(pygame.image.load("f4.png"), (30, 30)), \
	   pygame.transform.smoothscale(pygame.image.load("f4.png"), (30, 30))]

#defining the fielders based on the opponents class
fielders = [Opponents(opp[0], 80, 155, 25, 25), \
		    Opponents(opp[1], 620, 290, 30, 30), \
            Opponents(opp[2], 640, 120, 25, 25), \
            Opponents(opp[3], 90, 270, 22, 22), \
            Opponents(opp[4], 270, 130, 25, 25), \
            Opponents(opp[4], 580, 185, 25, 25)]

#setting the running player
man = Runner(370, 180)

#main function to take care of what is drawn on the screen and when
def drawGameWindow():
	global score
	global wickets
	global initV
	global oppScore
	global ballsLeft
	if winGame == False and loseGame == False:
		if initV:
			window.blit(background, (0,0))
			man.x = 370
			man.y = 180
	    
		elif initV == False:
			window.fill((0,140, 0))
			pygame.draw.circle(window, (255, 255, 255), (400, 300), 350, 1)
			window.blit(image1, (353, 200))
			for field in fielders:
				field.draw(window)
				man.draw(window)
				for bbb in b:
					#this checks if whether the runner has reached the 
					#creases before or after the ball has reached
					#if yes then wickets increase by 1 and score stays the same
					#else score increases and man is reset to running 
					#start posn. and user can choose to run again or not
					if bbb.y > 360 and man.y < 377 and man.rB:
						oldScore = score
						wickets += 1
						b.remove(bbb) 
						man.rb = False
						initV = True
						newScore = score
						if oldScore != newScore:
							score = oldScore
					elif man.y > 360 and bbb.y < 360:
						score += 1
						man.y = 180
						man.rB = False
		#all the text displayed on screen 
		#so user knows what he needs to do to win
		text1 = font.render("Score: " + str(score), 1, (0,0,0))
		text2 = font.render("Wickets " + str(wickets) + "/10", 1, (0, 0, 0))
		text3 = font.render("Score to Beat: " + str(oppScore), 1, (0, 0, 0))
		text4 = font.render("Balls Left: " + str(ballsLeft), 1, (0, 0, 0))
		window.blit(text1, (20, 20))
		window.blit(text2, (20, 45))
		window.blit(text3, (500, 20))
		window.blit(text4, (500, 45))
		for balls in b:
			balls.draw(window)

		for swings in s:
			swings.draw(window)

	#wingame state
	if winGame == True and loseGame == False:

		window.fill((50, 255, 20))
		text5 = font2.render("You Won!!!", 1, (255, 255, 255))
		text6 = font.render("By: " + str(10 - wickets) + \
							" Wickets", 1, (255, 255, 255))
		window.blit(text5, (150, 100))
		window.blit(text6, (30, 500))

	#loosegame state
	if winGame == False and loseGame == True:
		window.fill((255, 20, 20))
		text7 = font2.render("You Lost :(", 1, (0, 0, 0))
		window.blit(text7, (277, 250))


	pygame.display.update()



font = pygame.font.SysFont('comicsans', 30, True)
font2 = pygame.font.SysFont('comicsans', 60, True)

b = []
s = []



#these functions check whether the ball once hit collides 
#with any of the fielders coordinates
#returns boolen value that will be used in main loop
#defining fielders as rectangles

def isCollisionBall1():
    for bal in b:
        if bal.x >= 63 and bal.x <= 122 and bal.y >= 137 and bal.y <= 197:
            return True
        else:
            return False




def isCollisionBall2():
    for bal in b:
        if (bal.x >= 603 and bal.x <= 667 and bal.y >= 273 and bal.y <= 337):
            return True
        else:
            return False

def isCollisionBall3():
    for bal in b:
        if (bal.x >= 623 and bal.x <= 682 and bal.y >= 103 and bal.y <= 162):
            return True
        else:
            return False


def isCollisionBall4():
    for bal in b:
        if bal.x >= 73 and bal.x <= 129 and bal.y>= 273 and bal.y <= 329:
            return True
        else:
            return False

def isCollisionBall5():
    for bal in b:
        if bal.x >= 253 and bal.x <= 312 and bal.y >= 113 and bal.y <= 172:
            return True
        else:
            return False

def isCollisionBall6():
    for bal in b:
        if bal.x >= 563 and bal.x <= 622 and bal.y >= 168 and bal.y <= 227:
            return True
        else:
            return False


#this fucntion is on the start and pause screen 
#and allows the user to click what the want to do
#this code was borrowed from 
#https://pythonprogramming.net/pygame-button-function-events/ 
#however I changed it to suit my needs 
#but the main structure is the same so credit to that website
def button(x, y, w, h, ic, ac, action = None):
    global s
    global b
    global initV
    global score
    global wickets
    pygame.init()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 560 > mouse[0] > 480 and 300 > mouse[1] > 250:
        pygame.draw.rect(window, (0, 255, 0),(480,250,80,50))
        if click[0] == 1:
            mainLoop()

    elif 360 > mouse[0] > 280 and 300 > mouse[1] > 250:
        pygame.draw.rect(window, ac,(280,250,80,50))
        if click[0] == 1:
            pygame.QUIT

    else:
        pygame.draw.rect(window, ic,(x,y,w,h))



#intro screen (calls button fucntions)
def intro():
    global s
    global b
    global initV
    global score
    global wickets
    intro = True
    window.fill((0,0,0))
    font = pygame.font.SysFont('comicsans', 80, True)
    caption = font.render("StickCricket!", 1, (255,255,255))
    window.blit(caption, (200,100))
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
        
        button(480, 250, 80, 50, (0,195,0), (0, 255, 0))
        button(280, 250, 80, 50, (195, 0,0), (255, 0,0))
        pygame.display.update()
        clock.tick(27)


#pause screen display (calls pause screen fucntion 
#which is similar to button fucntion)
def paused():
	pause = True
	window.fill((0,0,0))
	font = pygame.font.SysFont('comicsans', 55, True)
	caption = font.render("PAUSED - click green to Continue", 1, (255,255,255))
	window.blit(caption, (70, 100))
	while pause:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pause = False
                
        
		pauseScreen(480, 250, 80, 50, (0,195,0), (0, 255, 0))
		pauseScreen(280, 250, 80, 50, (195, 0,0), (255, 0,0))
		pygame.display.update()
		clock.tick(15)  

#like the button fucmtion. aloows user to click on 
#pause screen and green means continue 
#and red means intro screen 
def pauseScreen(x, y, w, h, ic, ac):
	global s
	global b
	global initV
	global score
	global wickets
	pygame.init()
	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()


	if 560 > mouse[0] > 480 and 300 > mouse[1] > 250:
		pygame.draw.rect(window, (0, 255, 0),(480,250,80,50))
		if click[0] == 1:
			mainLoop()

	elif 360 > mouse[0] > 280 and 300 > mouse[1] > 250:
		pygame.draw.rect(window, ac,(280,250,80,50))
		if click[0] == 1:
			intro()

	else:
		pygame.draw.rect(window, ic,(x,y,w,h))




def mainLoop():
	global s
	global b
	global initV
	global score
	global wickets
	global ballsLeft
	global oppScore
	global winGame
	global loseGame

	run = True
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False  

		#checks if player has won. if yes sets win state and 
		#drawGame fucntion updates drawing new screen 
		if score > oppScore and ballsLeft >= 0 and wickets <= 10:
			winGame = True

		#checks if player has lost. if yes sets lose state and 
		#drawGame fucntion updates drawing new screen

		if score < oppScore and (ballsLeft == 0 or wickets == 10):
			loseGame = True

		#keys stored as a list. credit to Tech with Tim 
		#(youtube) as I got this idea from him. Link is in
		#citations below
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			s = []
			s.append(Player(380, 260, 30, 220, False, False, False))
		if keys[pygame.K_LEFT]:
			s = []
			s.append(Player(370, 400, 80, 15, True, True, False))
		if keys[pygame.K_RIGHT]:
			s = []
			s.append(Player(370, 400, 80, 15, True, False, True))
		if keys[pygame.K_SPACE]:
			ballsLeft -= 1
			b.append(Ball(420 + (random.randint(-100, 40)), 140, 34, 40, False))
		if keys[pygame.K_p]:
			paused()
		if keys[pygame.K_b]:
			#sets the Runners class attributes so drawGameWindow gets updated
			man.y += man.yChange
			man.rU = False
			man.rB = True 

		else:
			man.rU = False
			man.rB = False
			man.runCount = 0
        

		for swings in s:
			swings.update()

        
		for swings in s:
			for balls in b:
				#iterating through each bat posn and ball
				 #bowled and checking if any of them
				#collided with any of the fielders.

				#setting an or statement so this fucntion keeps running
				#till ball is back at wickets
				#same for all coliiisons
				#balls.isMovingBackX is inherited from Ball class and
				#is different for each fielder so ball does not get
				#confused between two fielders and makes an error
				#while being thrown back
				
				if isCollisionBall1() or balls.isMovingBack1 == True:
					balls.isMovingBack1 = True
					balls.isCaught = True
					balls.x += 7
					balls.y += 6
					if balls.x > 385 and balls.y < 510:
						initV = True
						balls.isMovingBack1 = False
						b.remove(balls)

				elif isCollisionBall2() or balls.isMovingBack2 == True:
					balls.isMovingBack2 = True
					balls.isCaught = True
					balls.x -= 7
					balls.y += 3
					if balls.x < 400 and balls.y < 510:
						initV = True
						balls.isMovingBack2  = False
						b.remove(balls)
				        
                    

				elif isCollisionBall3() or balls.isMovingBack3 == True:
					balls.isMovingBack3 = True
					balls.isCaught = True
					balls.x -= 6
					balls.y += 6
					if balls.x < 400 and balls.y < 510:
						initV = True
						balls.isMovingBack3 = False
						b.remove(balls)

				elif isCollisionBall4() or balls.isMovingBack4 == True:
				    balls.isMovingBack4 = True
				    balls.isCaught = True
				    balls.x += 10
				    balls.y += 4
				    if balls.x > 385 and balls.y < 510:
				        initV = True
				        balls.isMovingBack4 = False
				        b.remove(balls)

				elif isCollisionBall5() or balls.isMovingBack5 == True:
				    balls.isMovingBack5 = True
				    balls.isCaught = True
				    balls.x += 2
				    balls.y += 5
				    if balls.x > 385 and balls.y < 510:
				        initV = True
				        balls.isMovingBack5 = False
				        b.remove(balls)

				elif isCollisionBall6() or balls.isMovingBack6 == True:
				    balls.isMovingBack6 = True
				    balls.isCaught = True
				    balls.x -= 9
				    balls.y += 8
				    if balls.x < 400 and balls.y < 510:
				        initV = True
				        balls.isMovingBack6 = False
				        b.remove(balls)

                



				else:
					#if there are no collisions, 
					#then check for how the ball was hit.

					#balls.update bowls the bal towards the bat
					#starts at random x point so player doesnt always
					#know where the ball is going to come from
					#so player won't know hwo to swing it before hand
					#also random velocity to make it 
					#better experience for player

					if swings.swing == False and balls.isCaught == False:
						balls.update()

                    
                    #if i am swinging right and the
                    #ball is not intercepted by fielder
                    #it does the balls.hitright fucntion 
                    #which essentially gives ball an x
                    #and y direction velocities

					if swings.swing == True and swings.right == True\
					and swings.left == False and balls.isCaught == False:
						initV = False
						balls.hitRight()
                        
                 		#if ball is hit past the boundary
                 		#go back to original screen and remove the ball
						if balls.x >= 800 or balls.y <= 0:
						    initV = True
						    #logic to determine how much score 
						    #increases by based on X direction velocity
						    if balls.velXR > 28:
						    	score += random.choice([4, 6])
						    else:
						    	score += random.choice([2, 3])
						    b.remove(balls)

					elif swings.swing == True and swings.right == False\
					and swings.left == True and balls.isCaught == False:
						initV = False
						balls.hitLeft()


						if balls.x <= 0 or balls.y <= 0:
						    initV = True
						    #logic to determine how much score 
						    #increases by based on X 
						    #direction velocity
						    if balls.velXL < -28:
						    	score += random.choice([4, 6])
						    else:
						    	score += random.choice([2, 3])
						    b.remove(balls)

					#if i have not swung the bat and the ball has 
					#reached the wickets make me loose a wicket
					elif swings.swing == False and balls.y >= 340:
					    wickets += 1
					    b.remove(balls)



        

       
		clock.tick(27)
		pygame.display.update()


		drawGameWindow()  

intro()
pygame.quit()




'''
Citations:

. The idea for the start screen and buttons derived from: https://pythonprogramming.net/pygame-button-function-events/
. The structure of events and the way the events are in a list 
  (e.g space bar) came from Tech with Tim - 
  Youtube. https://www.youtube.com/watch?v=PyblLBlpf0s&index=10&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5
. the way I make the players run by storing all in a list and making
 a global variable runCount came from https://www.youtube.com/watch?v=UdsNBIzsmlI (Tech with Tim (Youtube))
. 'clock.tick(64)', i learned from 
https://www.youtube.com/watch?v=PyblLBlpf0s&index=10&list=PLzMcBGfZo4-lp3jAExUCewBfMx3UZFkh5. but used different timing.
** All images are not mine. All from google images**
buttons code and idea intro/pause screen https://www.youtube.com/watch?v=P-UuVITG7Vg&index=15&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO
in general got the idea from this channel as well. Also got the code from that channel
''' 




