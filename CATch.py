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

#images
background = pygame.image.load('background.jpg')

cat_left = pygame.image.load('CAT_LEFT.png')
cat_right = pygame.image.load('CAT_RIGHT.png')

food_burger = pygame.image.load('food_burger.png')
food_noodles = pygame.image.load('food_noodles.png')
food_pie = pygame.image.load('food_pie.png')
food_rice = pygame.image.load('food_rice.png')
food_shortcake = pygame.image.load('food_shortcake.png')
food_donut = pygame.image.load('food_donut.png')

foodLst = [food_burger, food_noodles, food_pie, food_rice, food_shortcake, food_donut]

# game parameters
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
FPS = 10
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
backgroundRect = background.get_rect()

pygame.display.set_caption('CATch')

smallFont = pygame.font.SysFont("comicsansms", 25)
medFont = pygame.font.SysFont("comicsansms", 50)
largeFont = pygame.font.SysFont("comicsansms", 80)


def text_objects(text, color, size):
    if size == "small": 
        textSurface = smallFont.render(text, True, color)
    elif size == "medium": 
        textSurface = medFont.render(text, True, color)
    elif size == "large": 
        textSurface = largeFont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (SCREEN_WIDTH/2), (SCREEN_HEIGHT/2)+y_displace
    screen.blit(textSurf, textRect)
    
def gameIntro():

    intro = True
    
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                intro = False
                
        screen.fill(white)
        message_to_screen("welcome to", green, -175, "medium")
        message_to_screen("CATch", green, -90, "large")
        message_to_screen("The objective of this game is to",
                          black)
        message_to_screen("eat all the food that you possibly can", black, 30)
        message_to_screen("by catching the food as it falls down the screen", black, 60)
        message_to_screen("Press any key to play!", black, 150)

        pygame.display.update()
        clock.tick(5)


# main game loop
def gameLoop():
    
    gameExit = False
    gameOver = False

    points = 0
    lives = 3
    #for now the cat is represented by a square block 
    cat_size = SCREEN_WIDTH/6  
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
            food_type = foodLst[random.randrange(0, len(foodLst))]
            food = Food(food_x, food_y, food_size, food_type) 
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
        screen.blit(background, backgroundRect)
        for food in FOOD_LST:
            food.update_y(food.get_size()/2)
            screen.blit(food.get_type(), (food.get_x(), food.get_y()))

        screen.blit(CAT, (cat_x, cat_y)) 
        HP = 'Lives: ' + str(lives)
        pts = 'Points: ' + str(points)
        HP_text = smallFont.render(HP, True, green)
        pts_text = smallFont.render(pts, True, green)
        screen.blit(HP_text, [SCREEN_WIDTH*.75, 33])
        screen.blit(pts_text, [SCREEN_WIDTH*.75, 66])
        
        pygame.display.update()

        clock.tick(FPS)

        while gameOver == True:
            screen.fill(white)
            message_to_screen("Game Over", red, -80, "large")
            message_to_screen("Your score: " + str(points), black, 40)
            message_to_screen("Press C to play again or Q to quit", black, 75)
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

gameIntro() 
gameLoop()
