import numpy as np
from raio import Raio
import math
from objetos.objeto import Objeto
from funcoes import Subtracao_vetores, Produto_escalar, normalizaVetor


class Esfera(Objeto):
    def __init__(self, posicaoCentro, raioEsfera: float, material ):
        super().__init__(posicaoCentro, material)
        self.raioEsfera = raioEsfera
        self.posicaoCentro = posicaoCentro
        self.material = material


    def intersecao(self, raio: Raio, infoIntersecao) :
        return intersecao(raio, infoIntersecao, self.posicaoCentro, self.raioEsfera)

    def getNormal(self, ponto): #calcula e retorna a normal do ponto da superficie esfera
        #return Subtracao_vetores(ponto , self.posicaoCentro) / self.raioEsfera

        return normalizaVetor(Subtracao_vetores(ponto, self.posicaoCentro))

    def getColor(self):
        return self.material.cor



def intersecao(raio, infoIntersecao, posicaoCentro, raioEsfera):
    w = Subtracao_vetores(raio.origem, posicaoCentro)
   
    a = Produto_escalar(raio.direcao, raio.direcao)
    b = 2 * Produto_escalar(w, raio.direcao)
    c = Produto_escalar(w, w) - raioEsfera * raioEsfera 

    delta = b * b - 4 * a * c
    if(delta < 0):
        return math.inf, math.inf

    t1 = (-b + math.sqrt(delta)) / (2 * a)
    t2 = (-b - math.sqrt(delta)) / (2 * a)
    
    t = raio.t
    if (0 < t1 < t): 
        t = t1
    if (0 < t2 < t):
        t = t2
    if (t == raio.t): 
        return None
        
    raio.t = t
    infoIntersecao.atualizaIntersecao(t)

    #return Calcula_ponto_intersecao(raio.origem, t, raio.direcao)
  
   