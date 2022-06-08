# First Importing pygame
import pygame
# Importing Random
import random
#Importing Math
import math
#Importing Music Mixer
from pygame import mixer

#Initzliaise pygame
pygame.init()
clock = pygame.time.Clock()

#set screen
width=800
height=600
screen_size=(width,height)
screen=pygame.display.set_mode(screen_size)

#Icon
icon = pygame.image.load('icon.png')

#Title & Icon
pygame.display.set_caption("Galaxy War")
pygame.display.set_icon(icon)


#Background Color
color = (0,0,0)


#Background
backgroundImg = pygame.image.load('background.jpg')

#Background Music
mixer.music.load('background.wav')
mixer.music.play(-1)


#player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change=0

def player(x,y):
    screen.blit(playerImg,(playerX,playerY))

#enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(10,150)
enemyX_change=1.2
enemyY_change= 50


def enemy(x,y):
    screen.blit(enemyImg,(enemyX,enemyY))

#Bullet Img
#Ready = You can't see the bullet on the screen
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 3
bullet_state ="ready"

#Score
score_value = 0
font = pygame.font.Font("scorefont.ttf",32)

textX = 10
textY = 10

def show_score(x,y):
    score = font.render("SCORE : "+ str(score_value),True , (255,255,255))
    screen.blit(score, (x,y))

#Game Over
over_font = pygame.font.SysFont("freesansbold.ttf",94)

def game_over_text():
    over_text = font.render("Just Over",True , (255,255,255))
    screen.blit(over_text, (300,250))



#(x+16)& (y+10) is spaceship current center

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16 ,y +10))

#Collision
#Adding Distance Eqution
def isCollision(enemyX,enemyY,bulletX,bulletY):   
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

#set game Loop
keep_alive= True
while keep_alive:

    screen.fill((color))
    screen.blit(backgroundImg,(0,0))
#Bullet Movement
#Bullet Boundary 
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
            fire_bullet(bulletX,bulletY)
            bulletY -= bulletY_change

    
    player(playerX, playerY)
    show_score(textX,textY)
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        explosion_sound = mixer.Sound('explosion.wav')
        explosion_sound.play()
        bulletY = 480
        bullet_state = "ready"
        score_value += 1
        enemyX = random.randint(0, 800)
        enemyY = random.randint(20,150)
    enemy(enemyX,enemyY)
 

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_alive = False
            
     # Keystroke playerX
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
               playerX_change = 1
            if event.key == pygame.K_LEFT:
               playerX_change = -1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                   bullet_sound = mixer.Sound('laser.wav')
                   bullet_sound.play()
                   bulletX = playerX
                   fire_bullet(playerX,bulletY)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               playerX_change = 0
            
   # Player Boundary                     
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

# enemy movement
     #Game Over

    if enemyY > 250:
        enemyY =2000
        game_over_text()
        
        
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change= 0.8
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change= -0.8
        enemyY += enemyY_change 
    


 
    pygame.display.update()


