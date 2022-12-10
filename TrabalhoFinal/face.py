
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