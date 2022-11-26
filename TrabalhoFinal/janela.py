
import pygame
import pygame
import pygame.gfxdraw
import random

from definicoes import Vetor


from cena import Cena

class Janela:
    
    def __init__(self, dJanela, colunasCanvas, linhasCanvas, cena: Cena):
        wJanela = 60 #dimenções da janela, por onde o observador ver o mundo
        hJanela = 60

        self.wj = wJanela
        self.hj = hJanela
        self.dJanela = dJanela
        self.dx = wJanela/colunasCanvas
        self.dy = hJanela/linhasCanvas
        self.janela = None
        self.cena = cena
        self.display = (cena.largura, cena.altura)




    def abrir(self):
            pygame.display.init()

            self.janela = pygame.display.set_mode(self.display)
    
    def canvasParaJanela(self, c, l): #retorna o vetor (Vx, Vy, Vz) que define a direção do raio, ou seja, que parte do meio do pixel atual
        return Vetor(
            -self.wj/2+self.dx/2+self.dx*c , 
            self.hj/2-self.dy*l, 
            -self.dJanela)

    def desenha(self):

        superfice = pygame.Surface(self.janela.get_size(), pygame.SRCALPHA, 32)
   
        for x in range(self.cena.largura):
            for y in range(self.cena.altura):
                D = self.canvasParaJanela(x, y)

                color = self.calculaCor()
                r = random.randint(1, 255)
                g = random.randint(1, 255)
                b = random.randint(1, 255)
                
           
                pygame.gfxdraw.pixel(superfice, x, y, (r, g, b)) #para cada posicao x,y da superficie, colore com o (r, g, b)
        self.janela.blit(superfice, (0, 0))
        pygame.display.flip()  

    def calculaCor(self):
        for objeto in self.cena.objetos:

    
    def loopEventos(self):
        self.desenha()

        try:
            while 1:
                event = pygame.event.wait()
                if event.type == pygame.QUIT:
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                        break
                    #if event.key in self.keys:
                           # self.keys[event.key]()
                if event.type == pygame.MOUSEBUTTONUP:
                    #if event.button in self.buttons:
                           # self.buttons[event.button]()
                   print('event.button', event.button, event.pos)
                                    
                pygame.display.flip()
                #self.cena.desenha()
                #print("FOI------------------------------")
        finally:
                pygame.quit() 

     





  