import numpy as np
from raio import Raio
import math
from objetos.objeto import Objeto
from definicoes import Cor, Vetor, Ponto
from funcoes import mult_matriz_vetor, Calcula_ponto_intersecao, Soma_vetores, Produto_escalar, Calcula_ponto_intersecao, Vetor_escalar, Subtracao_vetores, Produto_escalar, normalizaVetor, mult_matriz_ponto

from planoCircular import PlanoCircular

from transformacoes import rotacaoPonto, translacaoPonto, escalaPonto
class Cilindro(Objeto):
    def __init__(self, posicaoCentro, raioCilindro: float, direcao, altura, material, basePlano, topoPlano):
        super().__init__(posicaoCentro, material)
        self.raioCilindro = raioCilindro
        self.posicaoCentro = posicaoCentro
        self.direcaoCilindro = direcao
        self.alturaCilindro = altura
        self.material = material
        self.basePlano = basePlano
        self.topoPlano = topoPlano

    def intersecao(self, raio: Raio, infoIntersecao, obj):
        return intersecao(raio, infoIntersecao, self.posicaoCentro, self.raioCilindro, self.direcaoCilindro, self.alturaCilindro, obj, self.basePlano, self.topoPlano)

    def getNormal(self, ponto):  # calcula e retorna a normal do ponto da superficie Cilindro
        # return Subtracao_vetores(ponto , self.posicaoCentro) / self.raioCilindro
        w = Subtracao_vetores(ponto, self.posicaoCentro)

        parte_dois = Vetor_escalar(self.direcaoCilindro,
                                   Produto_escalar(w, self.direcaoCilindro)
                                   )
        N = Subtracao_vetores(w, parte_dois)
        return normalizaVetor(N)
    
    def reCalculaPlanos(self):
        n_Base = Vetor(-self.direcaoCilindro.x, -self.direcaoCilindro.y, -self.direcaoCilindro.z)
        nova_basePlano_plano = PlanoCircular(self.posicaoCentro, n_Base,self.raioCilindro, self.material)

        self.basePlano = nova_basePlano_plano

        centroTopo = Soma_vetores(self.posicaoCentro, Vetor_escalar(
        self.direcaoCilindro, self.alturaCilindro))
        novo_topoPlano = PlanoCircular(
        self.posicaoCentro, self.direcaoCilindro, self.raioCilindro, self.material)

        self.topoPlano = novo_topoPlano

    def getColor(self):
        return self.material.cor

    def mundoParaCamera(self, matriz):
        self.posicaoCentro = mult_matriz_ponto(matriz, self.posicaoCentro)
        self.direcaoCilindro = mult_matriz_vetor(matriz, self.direcaoCilindro)

        self.reCalculaPlanos()
    
    def rotacao(self,axis, teta):
        self.posicaoCentro = rotacaoPonto(axis, self.posicaoCentro, teta)
        self.reCalculaPlanos()

    def translacao(self, d):
        self.posicaoCentro = translacaoPonto(d, self.posicaoCentro)

        self.reCalculaPlanos()

    def escala(self, escala, ancor):
        fator = escala.x
        self.raioCilindro = self.raioCilindro * fator
        self.alturaCilindro = self.alturaCilindro * fator

        self.posicaoCentro = escalaPonto(escala, self.posicaoCentro, ancor)
        self.reCalculaPlanos()



   

def intersecao(raio, infoIntersecao,
               posicaoCentro, raioCilindro, direcaoCilindro,  alturaCilindro, obj, basePlano, topoPlano):


    basePlano.intersecao(raio, infoIntersecao, basePlano)

    

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

    projecao1 = Produto_escalar(Subtracao_vetores(
        p1, posicaoCentro), direcaoCilindro)
    projecao2 = Produto_escalar(Subtracao_vetores(
        p2, posicaoCentro), direcaoCilindro)
    t = raio.t

    if (projecao1 >= 0 and projecao1 <= alturaCilindro):
        t = t1
        raio.t = t

        infoIntersecao.atualizaIntersecao(t1, obj)
    if (projecao2 >= 0 and projecao2 <= alturaCilindro):
        t = t2
        raio.t = t

        infoIntersecao.atualizaIntersecao(t2, obj)
    # return Calcula_ponto_intersecao(raio.origem, t, raio.direcao)
