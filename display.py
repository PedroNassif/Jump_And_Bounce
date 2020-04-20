import pygame
import random

from Main import *
from auxi import *
from bola import *

class solo(object):
    def __init__(self, x, y, width, height, color):
        self.x = x 
        self.y = y 
        self.w = width
        self.h = height
        self.color = color

    def desenha_chao(self):
        pygame.draw.rect(gameDisplay, self.color, [self.x, self.y, self.w, self.h])

    def update(self, bola):
        if self.y <= DISPLAY_HEIGHT - self.h:
            self.y = DISPLAY_HEIGHT - self.h

        if bola.y <= limSup and bola.Vy <= 0:
            self.y = self.y + (-bola.Vy*(1/60))
            
        elif bola.excedeu and bola.Vy > 0:
            self.y = self.y + (-bola.Vy*(1/60))

            

class trampolim(object):
    def __init__(self, x, y, width, height, color, id):
        self.x = x 
        self.y = y 
        self.w = width
        self.h = height
        self.color = color
        self.id = id
    
    def desenha_tramp(self):
        pygame.draw.rect(gameDisplay, self.color, [self.x, self.y, self.w, self.h]) 

    def update(self, bola, chao):
        if self.y <= DISPLAY_HEIGHT - self.h - chao.h:
            self.y = DISPLAY_HEIGHT - self.h - chao.h

        if bola.y <= limSup and bola.Vy < 0:
            self.y = self.y + (-bola.Vy*(1/60))

        elif bola.excedeu and bola.Vy > 0:
            self.y = self.y + (-bola.Vy*(1/60))

        if self.x <= 0:
           self.x = DISPLAY_WIDTH

class nuvem(object):
    def __init__(self, x, y, width, height, color):
        self.x = x 
        self.y = y 
        self.w = width
        self.h = height
        self.color = color

    def desenha_nuvem(self):
        pygame.draw.rect(gameDisplay, self.color, [self.x, self.y, self.w, self.h])
  
    def update(self, bola):
        if bola.x + bola.w >= limLat:
            self.x = self.x + (-bola.Vx*(1/60))
        
        if self.x + self.w <= 0:
            self.x = DISPLAY_WIDTH
            self.x = self.x + (-bola.Vx*(1/60))
        
        if bola.y <= limSup and bola.Vy < 0:
            self.y = self.y + (-bola.Vy*(1/60))

        elif bola.excedeu and bola.Vy > 0:
            self.y = self.y + (-bola.Vy*(1/60))
            
        

        
                


        