import numpy as np
from numba import jit
import math

class Cone:
    def __init__(self, tipo: "Cone", centro, r, altura, direcao, cor, K_e,K_d,K_a, m, com_base = 1):
        self.tipo = tipo 
        self.centro = centro
        self.r = r
        self.altura = altura
        self.direcao = direcao
        self.cor = cor
        self.K_e = K_e
        self.K_d = K_d
        self.K_a = K_a
        self.m = m
        self.v = calc_v
        self.com_base = com_base

    def intersecao(self, posicaoOlhoObservador, D):
        return intersecao(self.direcao, self.r, self.altura, self.v, posicaoOlhoObservador, D)

    def calc_v(self):
        h_dc = Vetor_escalar(self.direcao, self.altura)
        v = Soma_vetores(centro, h_dc)
        return v

@jit
def IntersecaoCone(direcao, r, altura, v, posicaoOlhoObservador, D):
    
    w = Subtracao_vetores(altura,v, posicaoOlhoObservador)

    cos2teta = (altura*altura)/(altura*r+altura*altura)

    dr_dc = Produto_escalar(D, direcao)
    dr_dr = Produto_escalar(D,D)
    w_dc = Produto_escalar(w, direcao)
    
    a = dr_dc * dr_dc - dr_dr*cos2teta
    b_primeira_parte = Produto_escalar(w, D)* cos2teta
    b_segunda_parte = w_dc* dr_dc
    b = 2 * (b_primeira_parte - b_segunda_parte)
    c = w_dc * w_dc - Produto_escalar(w,w) * cos2teta

    delta = b * b - 4* a * c

    if(a==0):
        if(b==0):
            return math.inf
        t1 = -c / 2*b
        return t1
    
    if(delta < 0):
        return math.inf
    
    t1 = (-b + math.sqrt(delta)) / (2*a)
    t2 = (-b - math.sqrt(delta)) / (2*a)

    if(t1 > 0 and t2 > 0):
        if(t1 < t2):
            return t1
        return  t2

    if(t1 < 0 and t2 > 0):
        return  t2
    else:
        return  t1