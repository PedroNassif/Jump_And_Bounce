import time
import random
import pygame

from bola import *
from auxi import *

###############################################################################
#                                 Pontuacao
###############################################################################
class Score(object):
    
    def __init__(self, score):
        self.score = score
        self.font = pygame.font.SysFont(None, 25)
        self.text = ""

    def draw(self):
        self.text = self.font.render("Score: {}".format(self.score), True, white)
        gameDisplay.blit(self.text, (0,0))
    
    def update(self, Bola):
        if Bola.colidiu_Score:
            self.score += 1
            #reditag oila
            Bola.colidiu_Score = False
    
        return True
