import math
from calc_vetores import *

tipo = 'cone'

def Cone(centro, r, altura, direcao, cor, K_e,K_d,K_a, m):
    h_dc = Vetor_escalar(direcao,altura )
    v = Soma_vetores(centro, h_dc)
    return {
        'tipo': tipo ,
        'centro': centro, 
        'r': r, 
        'altura': altura,
        'direcao': direcao,
        'cor': cor, 
        'K_e': K_e,
        'K_d': K_d,
        'K_a': K_a,
        'm': m,
        'intersecao': IntersecaoCone,
        'v' : v
    }

def IntersecaoCone(cone, posicaoOlhoObservador, D):

    w = Subtracao_vetores(cone['v'], posicaoOlhoObservador)

    cos2teta = (cone['altura']*cone['altura'])/(cone['r']*cone['r']+cone['altura']*cone['altura'])

    dr_dc = Produto_escalar(D, cone['direcao'])
    dr_dr = Produto_escalar(D,D)
    w_dc = Produto_escalar(w, cone['direcao'])
    
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
    
    if(t1 < t2):
        return t1
    return  t2
