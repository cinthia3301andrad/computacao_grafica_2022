
from raio import Raio
from objetos.objeto import Objeto
from funcoes import Subtracao_vetores, produto_vetorial, normalizaVetor, Vetor, Face, Produto_escalar,Soma_vetores,Vetor_escalar, mult_matriz_ponto
from raio import Raio
from planoFace import PlanoFace
import math

from intercesaoInfo import IntercesaoInfo
class Face(Objeto):
    
    def __init__(self, p1, p2, p3 ):
        
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.normal = normalizaVetor(produto_vetorial(Subtracao_vetores(p2, p1), Subtracao_vetores(p3, p1)))

    def mundoParaCamera(self, matriz):
        self.p1 = mult_matriz_ponto(matriz, self.p1)
        self.p2 = mult_matriz_ponto(matriz, self.p2)
        self.p3 = mult_matriz_ponto(matriz, self.p3)

    def intersecao(self, raio, infoIntersecao, obj):
        EPSILON =  0.0000001
        vertex0 = self.p1
        vertex1 = self.p2
        vertex2 = self.p3
    
        edge1 = Subtracao_vetores(vertex1, vertex0)  
        edge2 = Subtracao_vetores(vertex2, vertex0)  
        h =  produto_vetorial(raio.direcao, edge2)
        a =  Produto_escalar(edge1, h)
        if (a > -EPSILON and a < EPSILON):
            return
        f = 1.0/a
        s = Subtracao_vetores(raio.origem, vertex0)  
        u = f * Produto_escalar(s, h)
        if (u < 0.0 or u > 1.0):
            return
        q = produto_vetorial(s, edge1)
        v = f * Produto_escalar(raio.direcao, q)
        if (v < 0.0 or u + v > 1.0):
            return

        t = f * Produto_escalar(edge2, q)

        if(t > EPSILON):
            infoIntersecao.atualizaIntersecao(t, obj)

        else: 
            return