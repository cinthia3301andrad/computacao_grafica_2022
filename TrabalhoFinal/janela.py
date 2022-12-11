
import pygame
import pygame
import pygame.gfxdraw
import random

from definicoes import Cor, Vetor, Ponto
from funcoes import Subtracao_vetores, Produto_escalar, normalizaVetor

from intercesaoInfo import IntercesaoInfo
from raio import Raio
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

    def desenha(self, novaJanela = True):
   
        superfice = pygame.Surface(self.janela.get_size(), pygame.SRCALPHA, 32)
        eye = Ponto(0, 0, 0)
        
        for x in range(self.cena.largura):
            for y in range(self.cena.altura):
                D = self.canvasParaJanela(x, y)
            
                raio = Raio(eye, D)
                infoIntersecao = IntercesaoInfo(raio)
                
                self.calculaIntersecao(raio, infoIntersecao)
                
                color = self.calculaCor(raio, infoIntersecao)
        
           
                pygame.gfxdraw.pixel(superfice,  (self.cena.largura -x), (self.cena.altura -y), (color.r, color.g, color.b)) #(self.cena.largura -x) ,(self.cena.altura -y)#para cada posicao x,y da superficie, colore com o (r, g, b)
        if(novaJanela):
            self.janela.blit(superfice, (0, 0))
            pygame.display.flip()  

    def calculaIntersecao(self, raio, infoIntersecao):
        for objetoComplexo in self.cena.objetos:
            for objeto in objetoComplexo:
                objeto.intersecao(raio, infoIntersecao, objeto)            

    def calculaCor(self, raio, infoIntersecao):
        
        if(infoIntersecao.valido):
            objeto_atual = infoIntersecao.hitObjeto
         

            normal = normalizaVetor(objeto_atual.getNormal(infoIntersecao.getPontoAtual()))
      
            P = infoIntersecao.getPontoAtual()
            
            cor = self.cena.computaLuzes(normal, P, objeto_atual, raio)
            if cor != None: 
            # return objeto_atual.getColor(color)
                return Cor(cor.r, cor.g, cor.b)
            #return Cor(0, 255, 255)
        else:
            cor = Cor(0, 255, 0)
            return cor
  
    def loopEventos(self):
        self.desenha()
        try:
            while 1:
             
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                      
                        if event.key == pygame.K_z or event.key == 122:
                            print("ENTROU NA Translação")
                            vetor_translacao = Vetor(40, 0,0)

                            self.cena.objetos[0][0].translacao(vetor_translacao) 
                            self.desenha() 
                            print("recalculando a cena...")               
                pygame.display.flip()
                
                
                #print("FOI------------------------------")
        finally:
                pygame.quit() 

     





  