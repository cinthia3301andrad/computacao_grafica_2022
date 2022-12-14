
import numpy as np
import math
from definicoes import Cor, Vetor, Ponto
from funcoes import Produto_escalar,Subtracao_vetores,Calc_L, normalizaVetor
from raio import Raio
from intercesaoInfo import IntercesaoInfo



class Cena:
    def __init__(self, largura: int, altura: int, objetos, luzes, sombras=True):
        self.largura = largura
        self.altura = altura
        self.objetos = objetos
        self.luzes = luzes
        self.loaded = False
        self.loading = False
        self.sombras = sombras

        # self.rayTrace(Raio(np.array([0., 0., 0.]), np.array([1., 0., 0.])))

    def desenha(self):
        print("desenha°",self.largura, self.altura, self.objetos)


    def computaLuzes(self, normal, P, material, raio, nCalcS):
        contribuicao = None
          # Cálculo da distância entre o ponto de interseção e a fonte luminosa
        temLuzComPonto = False
        temSombra = False
        posicaoPF = .000
        for luz in self.luzes:
            if(luz.tipo == 'pontual'):
                temLuzComPonto = True
                posicaoPF = luz.posicao

        if(temLuzComPonto):

            L                 = Calc_L(posicaoPF, P) #direcao
                    
            pf_pi     = Subtracao_vetores(posicaoPF, P)
            tam_pf_pi = math.sqrt(Produto_escalar(pf_pi, pf_pi))
            raioS = Raio(P, normalizaVetor(L),tam_pf_pi)
    
            infoIntersecaoSombra = IntercesaoInfo(raioS, tam_pf_pi)
            
            for objetoComplexo in self.objetos:
                for objeto in objetoComplexo:
                    objeto.intersecao(raioS, infoIntersecaoSombra, objeto) 
            
                    if( infoIntersecaoSombra.t_mais_proximo > 0 and infoIntersecaoSombra.t_mais_proximo < tam_pf_pi ):
                        temSombra = True
                        break
                if temSombra:
                    break
            if(raioS.t > 0.001 and  raioS.t < tam_pf_pi):
                temSombra = True
        if nCalcS == True:
            temSombra = False
            for luz in self.luzes:
               
                r = luz.computaLuz( normal,P, material, raio).r
                g = luz.computaLuz( normal,P, material, raio).g
                b = luz.computaLuz( normal,P, material, raio).b

                    
                if(contribuicao != None):
                    contribuicao = Cor( contribuicao.r + r, 
                                        contribuicao.g + g,
                                        contribuicao.b + b)
                else:
                    contribuicao = Cor(r, g, b)
            if(contribuicao.r > 1): contribuicao.r = 1
            if(contribuicao.g > 1): contribuicao.g = 1
            if(contribuicao.b > 1): contribuicao.b = 1
            return Cor(round(contribuicao.r*255), round(contribuicao.g*255), round(contribuicao.b*255))

        if (temSombra and temLuzComPonto): 
            for luz in self.luzes:
                if(luz.tipo == 'ambiente'):
                    r = luz.computaLuz( normal,P, material, raio).r
                    g = luz.computaLuz( normal,P, material, raio).g
                    b = luz.computaLuz( normal,P, material, raio).b
                    if(contribuicao != None):
                        return Cor(round(contribuicao.r*255), round(contribuicao.g*255), round(contribuicao.b*255))
                    else:
                        return Cor(round(r*255), round(g*255), round(b*255))
                else:
                    r = 0
                    g = 0
                    b = 0
                    if(contribuicao != None):
                        return Cor(round(contribuicao.r*255), round(contribuicao.g*255), round(contribuicao.b*255))
                    else:
                        return Cor(round(r*255), round(g*255), round(b*255))
        else: 
            temSombra = False
            for luz in self.luzes:
               
                r = luz.computaLuz( normal,P, material, raio).r
                g = luz.computaLuz( normal,P, material, raio).g
                b = luz.computaLuz( normal,P, material, raio).b

                    
                if(contribuicao != None):
                    contribuicao = Cor( contribuicao.r + r, 
                                        contribuicao.g + g,
                                        contribuicao.b + b)
                else:
                    contribuicao = Cor(r, g, b)
            if(contribuicao.r > 1): contribuicao.r = 1
            if(contribuicao.g > 1): contribuicao.g = 1
            if(contribuicao.b > 1): contribuicao.b = 1
            return Cor(round(contribuicao.r*255), round(contribuicao.g*255), round(contribuicao.b*255))
                

   


