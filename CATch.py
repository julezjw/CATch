#CATch is a simple game made with pygame 
#
import sys
import pygame
import math

pygame.init()

#Colors 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0) 

# game parameters
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('CATch')

gameExit = False

#for now the cat is represented by a square block 
cat_size = 40 
#coordinates of the cat 
cat_x = SCREEN_WIDTH/2 - cat_size/2 
cat_y = SCREEN_HEIGHT - cat_size
cat_x_change = 0
#characteristics of food for now
food_size = 20
food_x = SCREEN_WIDTH/2 - food_size*2 
food_y = 0
food_y_change = 0 
#characteristics of trash for now
trash_size = 20
trash_x = SCREEN_WIDTH/2 + trash_size
trash_y = 0
trash_y_change = 0  


# main game loop
while not gameExit:
    for event in pygame.event.get():
        #for debugging only 
        #print(event)
        
        if event.type == pygame.QUIT:
            gameExit = True

        #moving the cat     
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if cat_x >= 0: 
                    cat_x_change = -10
            if event.key == pygame.K_RIGHT:
                if cat_x <= SCREEN_WIDTH - cat_size: 
                    cat_x_change = 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and cat_x_change < 0: 
                cat_x_change = 0
            if event.key == pygame.K_RIGHT and cat_x_change > 0:
                cat_x_change = 0              
    if cat_x_change < 0 and cat_x == 0:
        cat_x = 0
    elif cat_x_change > 0 and cat_x == SCREEN_WIDTH - cat_size:
        cat_x = SCREEN_WIDTH - cat_size
    else:
        cat_x += cat_x_change

    #moving the food/trash 
    if food_y < SCREEN_HEIGHT:
        food_y += 5
    if trash_y < SCREEN_HEIGHT:
        trash_y += 5
    

    
    screen.fill(white)
    pygame.draw.rect(screen, black, [cat_x, cat_y, cat_size, cat_size])
    pygame.draw.rect(screen, green, [food_x, food_y, food_size, food_size])
    pygame.draw.rect(screen, red, [trash_x, trash_y, trash_size, trash_size])

    pygame.display.update()

    clock.tick(10)

pygame.quit()
quit()
 
