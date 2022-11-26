import numpy as np
from numba import jit
from raio import Raio

from objetos.objeto import Objeto


class Esfera(Objeto):
    def __init__(self, posicaoCentro, raioEsfera: float, material ):
        super().__init__(posicaoCentro, material)
        self.raioEsfera = raioEsfera
        self.posicaoCentro = posicaoCentro
        self.material = material


    def intersecao(self, raio: Raio) :
        return intersecao(raio, self.posicaoCentro, self.raioEsfera)

    def getNormal(self, ponto): #calcula e retorna a normal do ponto da superficie esfera
        return (ponto - self.posicaoCentro) / self.raioEsfera

@jit
def intersecao(raio, posicaoCentro, raioEsfera):
    co = raio.origem - posicaoCentro #subtração de vetores que da um vetor

    b = co @ raio.direcao
    c = co @ co - raioEsfera ** 2
    delta = b ** 2 - c
    if (delta < 0): 
        return None

 
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
    return raio.origem + raio.direcao*t