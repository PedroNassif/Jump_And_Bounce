import time
import random
import pygame

from bola import *
from auxi import *
from display import *
from Score  import *

# inicia o pygame
pygame.init()

##########################################################################################################################
#                                           Tela Inicial
##########################################################################################################################
def game_start():
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    intro = False
                    gameLoop()

        BackGround = pygame.image.load('Imagens/background.png')
        largeText = pygame.font.Font('freesansbold.ttf',100)
        
        TextSurf, TextRect = text_objects("Press Start", largeText, white)
        TextRect.center = ((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT/4))
        
        gameDisplay.blit(BackGround,(0,0))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(15)

############################################################################################################################
#                                       Tela de Derrota
############################################################################################################################
def game_over():

    GameOver = pygame.image.load("Imagens/fire.png")
    largeText = pygame.font.Font('freesansbold.ttf', 105)
    
    TextSurf, TextRect = text_objects("GAME OVER!", largeText, white)
    TextRect.center = ((DISPLAY_WIDTH/2),(DISPLAY_HEIGHT/4))
    
    #Plano de Fundo
    gameDisplay.blit(GameOver,(0,0))
    gameDisplay.blit(TextSurf, TextRect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:
                game_start()
    
    
    pygame.display.update()
    clock.tick(60)

############################################################################################################################
#                                           Loop Jogo
############################################################################################################################
def gameLoop():
    
    #criar bola e plotar na tela
    bola = Bola(DISPLAY_WIDTH*0.025, DISPLAY_HEIGHT*0.1, ballImg)
   
    #Criando Lista de  trammpolins
    list_t = []
    
    for i in range(5):
        Tramp = trampolim(random.randrange(0, DISPLAY_WIDTH) + (random.randrange(0, 100)*i), 540, 150, 10, orange, (i+1)*10)
        list_t.append(Tramp)

    chao = solo(0, 550, 1200, 50, green)
    cloud = nuvem(DISPLAY_WIDTH/4 + 150,DISPLAY_HEIGHT/4, 300,100, white)

    # cria ponto
    score = Score(score=0)
    
    while True:
        #background
        gameDisplay.fill(blue)

        #desenhar o solo 
        chao.desenha_chao()
        
        #desenhar trampolim
        for t in list_t:
            t.desenha_tramp()
        
        #desenha nuvem
        cloud.desenha_nuvem()
        
        #aparecer a bola
        bola.draw()
        
        #Atualizar posição da bola
        bola.update()
        cloud.update(bola)

        #Update no chao e trampolim
        chao.update(bola)
        for t in list_t:
            t.update(bola, chao)
       
        #Checar se deu Kick
        for t in list_t:
            bola.check_kick(chao, t)

        if bola.colidiu:
            bola.Pulo()
            bola.colidiu = False
            bola.y = Tramp.y - bola.h
                     
        # tratamento dos eventos    
        for event in pygame.event.get():     
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit() 
            
            if event.type == pygame.KEYDOWN:
               
                if event.key == pygame.K_SPACE:
                    bola.throw(410)
                    #print("Bola Lançada")      
               
                if event.key == pygame.K_DOWN:
                    bola.Impulso()
                    #print("Impulso dado")    
                
                if event.key == pygame.K_r:
                    gameLoop()          
               
        #Perder
        if bola.lost:
            game_over()
        
        # atualiza placar
        if score.update(bola):
            score.draw()
        else:    
            game_start()
        
        # atualiza display
        pygame.display.update()
       
        #FPS
        clock.tick(60)  
        
        #print("Vx: {} e Vy: {}".format(bola.Vx, bola.Vy))


#Chama o game star --- toda funçao tem que chamada
if __name__ == "__main__":
    game_start()