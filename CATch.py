#CATch is a simple game made with pygame 
#
import sys
import pygame
import math
import random
from Food import Food 

pygame.init()

#Colors 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0) 

cat_left = pygame.image.load('CAT_LEFT.png')
cat_right = pygame.image.load('CAT_RIGHT.png')

# game parameters
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
FPS = 10

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('CATch')
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 25)

def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color):
    textSurf, textRect = text_objects(msg, color)
    textRect.center = (SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)
    screen.blit(textSurf, textRect) 

# main game loop
def gameLoop():
    
    gameExit = False
    gameOver = False

    points = 0
    lives = 3
    #for now the cat is represented by a square block 
    cat_size = SCREEN_WIDTH/10  
    #coordinates of the cat 
    cat_x = SCREEN_WIDTH/2 - cat_size/2 
    cat_y = SCREEN_HEIGHT - cat_size
    cat_x_change = 0
    CAT = cat_right
    #characteristics of food for now
    food_size = cat_size/2
    FOOD_LST = []

    
    #characteristics of trash for now
    trash_size = cat_size/2
    trash_x = random.randrange(1, int(SCREEN_WIDTH - trash_size))
    trash_y = 0
    trash_y_change = 0

    while not gameExit:


            
        if lives == 0:
            gameOver = True 
        
        for event in pygame.event.get():
            #for debugging only 
            #print(event)
            
            if event.type == pygame.QUIT:
                gameOver = True

            #moving the cat     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if cat_x >= 0: 
                        cat_x_change = -cat_size/4
                        CAT = cat_left
                elif event.key == pygame.K_RIGHT:
                    if cat_x <= SCREEN_WIDTH - cat_size: 
                        cat_x_change = cat_size/4
                        CAT = cat_right
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and cat_x_change < 0: 
                    cat_x_change = 0
                elif event.key == pygame.K_RIGHT and cat_x_change > 0:
                    cat_x_change = 0              
        if cat_x_change < 0 and cat_x == 0:
            cat_x = 0
        elif cat_x_change > 0 and cat_x == SCREEN_WIDTH - cat_size:
            cat_x = SCREEN_WIDTH - cat_size
        else:
            cat_x += cat_x_change

        #moving the food/trash
        if len(FOOD_LST) == 0 or FOOD_LST[0].get_y() > SCREEN_HEIGHT*random.randrange(4,9)/9:
            food_x = random.randrange(0, int(SCREEN_WIDTH - food_size))
            food_y = 0
            food = Food(food_x, food_y, food_size) 
            FOOD_LST.insert(0, food)
        if trash_y < SCREEN_HEIGHT:
            trash_y += food_size/2

        for food in FOOD_LST:
            if food.get_x() in range(int(cat_x - food.get_size()), int(cat_x + cat_size))and \
               food.get_y() + food.get_size() in range(int(cat_y), SCREEN_HEIGHT):
                FOOD_LST.remove(food)
                points += food.get_points()
            if food.get_y() >= SCREEN_HEIGHT:
                FOOD_LST.remove(food)
                lives -= 1 

        #drawing everything 
        screen.fill(white)
        for food in FOOD_LST:
            food.update_y(food.get_size()/2)
            food.draw_it(screen)

        screen.blit(CAT, (cat_x, cat_y)) 
        HP = 'Lives:' + str(lives)
        pts = 'Points: ' + str(points)
        HP_text = font.render(HP, True, green)
        pts_text = font.render(pts, True, green)
        screen.blit(HP_text, [SCREEN_WIDTH*.8, 50])
        screen.blit(pts_text, [SCREEN_WIDTH*.8, 69])
        
        pygame.display.update()

        clock.tick(FPS)

        while gameOver == True:
            screen.fill(white)
            message_to_screen("Game Over: Press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False 
                        gameExit = True
                    elif event.key == pygame.K_c:
                        gameLoop() 

    pygame.quit()
    quit()
 
gameLoop()
