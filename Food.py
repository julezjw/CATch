import sys
import pygame
import math


class Food(object):
    def __init__(self, x, y, size, food_type):
        self.x = x
        self.y = y
        self.size = size 
        self.color = (0, 255, 0) #green
        self.points = 10
        self.food_type = food_type
        
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_size(self):
        return self.size

    def get_points(self):
        return self.points

    def get_type(self):
        return self.food_type

    def update_x(self, change_x):
        self.x += change_x

    def update_y(self, change_y):
        self.y += change_y 
                
    def draw_it(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.size, self.size])
