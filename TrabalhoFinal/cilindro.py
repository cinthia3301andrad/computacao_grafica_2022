import numpy as np
from raio import Raio
import math
from objetos.objeto import Objeto
from funcoes import Calcula_ponto_intersecao, Vetor_escalar, Subtracao_vetores, Produto_escalar, normalizaVetor, mult_matriz_ponto


class Cilindro(Objeto):
    def __init__(self, posicaoCentro, raioCilindro: float, direcao, altura, material):
        super().__init__(posicaoCentro, material)
        self.raioCilindro = raioCilindro
        self.posicaoCentro = posicaoCentro
        self.direcaoCilindro = direcao
        self.alturaCilindro = altura
        self.material = material

    def intersecao(self, raio: Raio, infoIntersecao, obj):
        return intersecao(raio, infoIntersecao, self.posicaoCentro, self.raioCilindro, self.direcaoCilindro, self.alturaCilindro, obj)

    def getNormal(self, ponto):  # calcula e retorna a normal do ponto da superficie Cilindro
        # return Subtracao_vetores(ponto , self.posicaoCentro) / self.raioCilindro

        return normalizaVetor(Subtracao_vetores(ponto, self.posicaoCentro))

    def getColor(self):
        return self.material.cor

    def mundoParaCamera(self, matriz):
        self.posicaoCentro = mult_matriz_ponto(matriz, self.posicaoCentro)


def intersecao(raio, infoIntersecao, posicaoCentro, raioCilindro, direcaoCilindro,  alturaCilindro, obj):
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
    dp1 = Produto_escalar(Subtracao_vetores(
        posicaoCentro, p1), direcaoCilindro)
    dp2 = Produto_escalar(Subtracao_vetores(
        posicaoCentro, p2), direcaoCilindro)

    if t1 > 0 and 0 <= dp1 <= alturaCilindro:
        pointAux1 = Calcula_ponto_intersecao(raio.origem, t1, raio.direcao)
        points.append((t1, pointAux1))
    if t2 > 0 and 0 <= dp2 <= alturaCilindro:
        pointAux2 = Calcula_ponto_intersecao(raio.origem, t2, raio.direcao)
        points.append((t2, pointAux2))
    if len(points) == 0:
        return None

    minPoint = points[0]
    for point in points:
        if point[0] < minPoint[0]:
            minPoint = point
    if raio.t  < minPoint[0]:
        return None

    raio.t = minPoint[0]
    print("minPoint[0]", minPoint[0], minPoint[1])

    infoIntersecao.atualizaIntersecao(minPoint[0], obj)
    # return Calcula_ponto_intersecao(raio.origem, t, raio.direcao)
