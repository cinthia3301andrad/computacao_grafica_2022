
import pygame
import pygame
import pygame.gfxdraw
import random
import math

from definicoes import Cor, Vetor, Ponto
from funcoes import Subtracao_vetores, Produto_escalar, normalizaVetor, mult_matriz_ponto

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
        eye = Ponto(0,200, 0)
        
        for x in range(self.cena.largura):
            for y in range(self.cena.altura):
                #Projeção perspectiva
                D = self.canvasParaJanela(x, y)
            
                raio = Raio(eye, D)
                #Projeção orthográfica
               # raio = Raio(D, Vetor(0, 0, -1))
                infoIntersecao = IntercesaoInfo(raio)
                
                self.calculaIntersecao(raio, infoIntersecao)

                color = self.calculaCor(raio, infoIntersecao)
        
           
                pygame.gfxdraw.pixel(superfice, (self.cena.largura -x) ,(self.cena.altura -y), (color.r, color.g, color.b)) #(self.cena.largura -x) ,(self.cena.altura -y)#para cada posicao x,y da superficie, colore com o (r, g, b)
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
            if objeto_atual.material.imagem:

                C = Ponto(-3750, -150, -2500)
                D = Ponto(3750, -150, -2500)
                S = Ponto(-3750, 4000, -2500)

                M, LI, LJ = objeto_atual.matriz(C,D,S)
                #print('LI ', LI, 'LJ', LJ)

                Pm = mult_matriz_ponto(M, P)

                fx = Pm.x/LI  # p chao e teto P.x e P.z
                fy = 1-(Pm.y/LJ)
                #print(fx, " FX", fy, " FY")
                if fx > 0 and fx < 1:
                    if fy > 0 and fy < 1:
                #coordenada de textura

                        y_textura = math.trunc(fy * (objeto_atual.material.TexturaAltura - 1.) + 0.5)
                        x_textura = math.trunc(fx * (objeto_atual.material.TexturaLargura - 1.)  + 0.5)

                        cor_atual =  objeto_atual.material.imagem[x_textura, y_textura]
                        cor_atual = Vetor(cor_atual[0]/255, cor_atual[1]/255, cor_atual[2]/255)
                        objeto_atual.material.k_difusa = cor_atual
                        objeto_atual.material.k_especular = cor_atual
                        objeto_atual.material.k_ambiente = cor_atual
            nCalcS = False
            if(objeto_atual.tipo == "ceu"):
                nCalcS = True
            
            cor = self.cena.computaLuzes(normal, P, objeto_atual, raio, nCalcS)
            if cor != None: 
            # return objeto_atual.getColor(color)
                return Cor(cor.r, cor.g, cor.b)
            #return Cor(0, 255, 255)
        else:
            cor = Cor(26, 155, 65)
            return cor
  
    def loopEventos(self):
        self.desenha()
        try:
            while 1:
             
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                     

                    
                    if event.type == pygame.KEYDOWN:
                        print(event.key)
                        if event.key == pygame.K_z or event.key == 122:
                            print("ENTROU NA Translação")
                            vetor_translacao = Vetor(40, 0,0)

                            self.cena.objetos[0][0].translacao(vetor_translacao) 
                            self.desenha() 
                            print("recalculando a cena...")
                        if event.key == pygame.K_s:  #115
                            print("ENTROU NA luz")
                            i = 0
                            luzes = []
                            
                            while(len(self.cena.luzes)>i):
                                print(len(self.cena.luzes))
                                print(self.cena.luzes[i].tipo)
                        
                                if self.cena.luzes[i].tipo != "spot":
                                    luzes.append(self.cena.luzes[i])
                        
                                i = i +1
                            self.cena.luzes = luzes
                            print("Tirando a luz spot....")
                            self.desenha()
                            print("Luz retirada!")
                        if event.key == pygame.K_a: #97
                            i = 0
                            luzes = []
                            
                            while(len(self.cena.luzes)>i):
                                if self.cena.luzes[i].tipo != "ambiente":
                                    luzes.append(self.cena.luzes[i])
                                i = i +1
                            self.cena.luzes = luzes
                            print("Tirando a luz ambiente....")
                            self.desenha()
                            print("Luz retirada!")
                        if event.key == pygame.K_d:  
                            i = 0
                            luzes = []
                            
                            while(len(self.cena.luzes)>i):
                                if self.cena.luzes[i].tipo != "direcional":
                                    luzes.append(self.cena.luzes[i])
                                i = i +1
                            print(luzes)
                            self.cena.luzes = luzes
                            print("Tirando a luz direcional....")
                            self.desenha()
                            print("Luz retirada!")
                pygame.display.flip()
                
                
                #print("FOI------------------------------")
        finally:
                pygame.quit() 

     





  