# 1 - import library
import pygame
import math
import random
from pygame.locals import *

# 2 - initialize the game
pygame.init()
pygame.display.set_caption('ZOMBIE SIEGE by Michal Grzeszczak')
width, height = 800, 600
pi = 3.14159
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False]
playerPos = [width/2,height/2]
acc = [0,0]
arrows = []
badTimer = 100
badTimer0 = 0
badGuys = [[800,100]]
survivors = 25

# 3 - load images
player = pygame.image.load("hunter.png")
grass = pygame.image.load("grass.png")
hut = pygame.image.load("hut.png")
arrow = pygame.image.load("arrow.png")
badguyimg1 = pygame.image.load("zombie.png")
badguyimg=badguyimg1
gameover = pygame.image.load("lose.png")
youwin = pygame.image.load("win.png")

# 4 - keep looping through
running = 1
exitCode = 0
while running:
    badTimer-=1

    # 5 - clear the screen before drawing it again
    screen.fill(0)

    # 6 - draw the screen elements
    screen.blit(grass,(0,0))
    screen.blit(hut,(0,50))
    screen.blit(hut,(0,200))
    screen.blit(hut,(0,350))
    screen.blit(hut,(0,500))

    # 6.1 - draw player position and rotation
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerPos[1]+50),position[0]-(playerPos[0]+50))
    playerRot = pygame.transform.rotate(player, 360-angle*360/(2*pi))
    playerPosRot = (playerPos[0]-playerRot.get_rect().width/2, playerPos[1]-playerRot.get_rect().height/2)
    screen.blit(playerRot, playerPosRot)

    # 6.2 - draw arrows
    for bullet in arrows:
        index = 0
        velx = math.cos(bullet[0])*10
        vely = math.sin(bullet[0])*10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1]>800 or bullet[2] < -64 or bullet[2] > 600:
            arrows.pop(index)
        index += 1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))

    # 6.3 - Draw zombies
    if badTimer == 0:
        badGuys.append([800, random.randint(50,500)])
        badTimer = 100-(badTimer0*2)
        if badTimer0 >= 35:
            badTimer0 = 35
        else:
            badTimer0+=5
    index = 0
    for badGuy in badGuys:
        if badGuy[0] <- 64:
            badGuys.pop(index)
        badGuy[0] -= 2.5

        # 6.3.1 - Attack village
        badRect = pygame.Rect(badguyimg.get_rect())
        badRect.top = badGuy[1]
        badRect.left = badGuy[0]
        if badRect.left < 50:
            survivors -= 1
            badGuys.pop(index)

        #6.3.2 - Check for collisions
        index1=0
        for arr in arrows:
            arrowRect = pygame.Rect(arrow.get_rect())
            arrowRect.left = arr[1]
            arrowRect.top = arr[2]
            if badRect.colliderect(arrowRect):
                acc[0] += 1
                badGuys.pop(index)
                arrows.pop(index1)
            index1 += 1

        # 6.3.3 - Next bad guy
        index += 1
    for badGuy in badGuys:
        screen.blit(badguyimg, badGuy)

    # 6.4 - Draw clock
    font = pygame.font.Font(None, 48)
    timeText = font.render(str((90000-pygame.time.get_ticks())/60000)+":"+str((90000-pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
    textRect = timeText.get_rect()
    textRect.topright = [795,5]
    screen.blit(timeText, textRect)

    # 6.5 - Draw survivors counter
    surviveText = font.render("Survivors left: " + str(survivors), True, (0,0,0))
    textRect = surviveText.get_rect()
    textRect.topleft = [5,5]
    screen.blit(surviveText, textRect)

    # 7 - update the screen
    pygame.display.flip()

    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_s:
                keys[1] = True
            elif event.key == K_a:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
            elif event.key == K_c:
                pygame.quit()
                exit(0)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_s:
                keys[1] = False
            elif event.key == pygame.K_a:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            acc[1] += 1
            arrows.append([math.atan2(position[1]-(playerPosRot[1]+50),position[0]-(playerPosRot[0]+50)),playerPosRot[0]+50,playerPosRot[1]+50])

    # 9 - Move player
    if keys[0]:
        playerPos[1] -= 5
    elif keys[1]:
        playerPos[1] += 5
    if keys[2]:
        playerPos[0] -= 5
    elif keys[3]:
        playerPos[0] += 5

    #check if player is not "out of screen"
    if playerPos[0] < 0: playerPos[0] = 0
    if playerPos[0] > width-100: playerPos[0] = width-100
    if playerPos[1] < 0: playerPos[1] = 0
    if playerPos[1] > height-100: playerPos[1] = height-100

    #10 - Win/Lose check
    if pygame.time.get_ticks()>=90000:
        running=0
        exitCode=1
    if survivors<=0:
        running=0
        exitCode=0
    if acc[1]!=0:
        accuracy=acc[0]*1.0/acc[1]*100
    else:
        accuracy=0

# 11 - Win/lose display        
if exitCode==0:
    pygame.font.init()
    font = pygame.font.Font(None, 48)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+150
    screen.blit(gameover, (width/2-160,height/2-100))
    screen.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 48)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+150
    screen.blit(youwin, (width/2-160,height/2-100))
    screen.blit(text, textRect)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
