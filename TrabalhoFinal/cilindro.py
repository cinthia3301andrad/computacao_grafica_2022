import numpy as np
from raio import Raio
import math
from objetos.objeto import Objeto
from definicoes import Cor, Vetor, Ponto
from funcoes import Calcula_ponto_intersecao, Soma_vetores, Produto_escalar, Calcula_ponto_intersecao, Vetor_escalar, Subtracao_vetores, Produto_escalar, normalizaVetor, mult_matriz_ponto

from planoCircular import PlanoCircular
class Cilindro(Objeto):
    def __init__(self, posicaoCentro, raioCilindro: float, direcao, altura, material):
        super().__init__(posicaoCentro, material)
        self.base = Ponto(0, 0, 0)
        self.raioCilindro = raioCilindro
        self.posicaoCentro = posicaoCentro
        self.direcaoCilindro = direcao
        self.alturaCilindro = altura
        self.material = material

    def intersecao(self, raio: Raio, infoIntersecao, obj):
        return intersecao(raio, infoIntersecao, self.posicaoCentro, self.raioCilindro, self.direcaoCilindro, self.alturaCilindro,self.base, obj)

    def getNormal(self, ponto):  # calcula e retorna a normal do ponto da superficie Cilindro
        # return Subtracao_vetores(ponto , self.posicaoCentro) / self.raioCilindro
        w = Subtracao_vetores(ponto, self.base)

        parte_dois = Vetor_escalar(self.direcaoCilindro, 
        Produto_escalar(w, self.direcaoCilindro)
                                )
        N = Subtracao_vetores(w, parte_dois)
        return normalizaVetor(N)

    def getColor(self):
        return self.material.cor

    def mundoParaCamera(self, matriz):
        self.posicaoCentro = mult_matriz_ponto(matriz, self.posicaoCentro)


def intersecao(raio, infoIntersecao, 
posicaoCentro, raioCilindro, direcaoCilindro,  alturaCilindro, base, obj):
    n_Base = Vetor(-direcaoCilindro.x, -direcaoCilindro.y, -direcaoCilindro.z)
    basePlano = PlanoCircular(base, n_Base,raioCilindro, obj.material)

    basePlano.intersecao(raio, infoIntersecao, obj)

    centroTopo = Soma_vetores(posicaoCentro, Vetor_escalar(direcaoCilindro,alturaCilindro))
    topoPlano = PlanoCircular(centroTopo, direcaoCilindro,raioCilindro, obj.material)

    topoPlano.intersecao(raio, infoIntersecao, obj)

    prod_escalar = Produto_escalar(raio.direcao, direcaoCilindro)

    

    mult = Vetor_escalar(direcaoCilindro, prod_escalar)

    w = Subtracao_vetores(raio.direcao, mult)

    # nao tenho certeza que esse P é o certo
    v_primeiro = Subtracao_vetores(raio.origem, posicaoCentro)
    v_segundo = Vetor_escalar(direcaoCilindro,
                              Produto_escalar(v_primeiro, direcaoCilindro)
                              )
    v = Subtracao_vetores(v_primeiro, v_segundo)

    a = Produto_escalar(w, w)
    if (a == 0):
        return None
    b = 2*Produto_escalar(v, w)
    c = Produto_escalar(v, v) - raioCilindro * raioCilindro

    delta = b * b - 4 * a * c

    if (delta < 0):
        return math.inf
    points = []
    t1 = (-b + math.sqrt(delta)) / (2*a)
    t2 = (-b - math.sqrt(delta)) / (2*a)

    p1 = Calcula_ponto_intersecao(raio.origem, t1, raio.direcao)
    p2 = Calcula_ponto_intersecao(raio.origem, t2, raio.direcao)
  
    h1 = Produto_escalar(Subtracao_vetores(p1, base), direcaoCilindro)
    h2 = Produto_escalar(Subtracao_vetores(p2, base), direcaoCilindro)
    t = raio.t
    if(t1 < t2):
        t = t1
    else:
        t = t2
    raio.t = t
    if(h1 >= 0 and h1 <= alturaCilindro):
        infoIntersecao.atualizaIntersecao(t1, obj)
    if(h2 >= 0 and h2 <= alturaCilindro):
        infoIntersecao.atualizaIntersecao(t2, obj)
    # return Calcula_ponto_intersecao(raio.origem, t, raio.direcao)
