import pygame


from Main import *
from auxi import *

class Bola():
    def __init__(self,x,y,img):
        self.img = img
        self.x  = x
        self.y = y
        self.V = 0
        self.Vx = 0
        self.Vy = 0
        self.ay = 0
        self.ax = 0
        self.m = 10
        self.w = 100
        self.h = 100
        self.cr = 0 #coeficiente de restituição
        #atributos booleanos
        self.excedeu = False
        self.lost = False
        self.iniciou = False
        self.parou = False
        self.colidiu = False
        self.elastico = False
        self.inelastico = False
        self.colidiu_Score = False
        self.retornou = False

    def draw(self):
        gameDisplay.blit(self.img, (self.x, self.y))

    #metodos
    def throw(self,Vi):
        self.Vx=Vi
        self.ay=g
        self.iniciou = True
    
    def Impulso(self):
        self.Vy = (((30000 * 0.5) + (self.m * self.Vy))/self.m)
   
   #reconhece quando chega no chão
    def check_kick(self, chao, tramp):
        if (self.x + self.w/2 >= tramp.x) and (self.x <= tramp.x + tramp.w):
            if (self.y + self.h) >= tramp.y:
                self.y = tramp.y - self.h
                self.elastico = True 
                if self.Vy > 0:
                    self.colidiu = True    
                    self.colidiu_Score = True
                    #print("colidiu")

        elif self.y + self.h >= chao.y:
            self.y = chao.y - self.h
            self.inelastico = True
        
        #tocar o teto
        if self.y <= limSup and self.Vy < 0:
            self.excedeu = True
        
        elif self.Vy > 0 and self.y > limSup:
           self.excedeu = False
        
        #barrar a passagem
        #if self.excedeu:
        #    self.y = limSup
             
        #tocar o eixo X
        if self.x + self.w >= DISPLAY_WIDTH - limLat:
            self.x = DISPLAY_WIDTH - self.w -limLat
            tramp.x = tramp.x - (self.Vx*(freq))
    
        #Lose
        if self.Vy < 0 and self.Vy < 0:
            #self.Vy = 0
            self.parou = True
            if self.parou and self.iniciou:
               self.lost = True
            
    #Pulo
    def Pulo(self):
        if self.colidiu:
           self.Vy = -self.Vy*0.8

    #metodos para incrementar coisas
    def incremento_Velocidade(self):
        self.Vy = self.Vy + self.ay*(freq)
        self.Vx = self.Vx + self.ax*(freq)
    
    def incremento_Posicao(self):
         self.x = self.x + self.Vx*(freq)
         self.y = self.y + self.Vy*(freq)

    
    
    def update(self):
        self.incremento_Velocidade()
        self.incremento_Posicao()
        


        

     
