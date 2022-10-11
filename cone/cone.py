import math
from calc_vetores import *

tipo = 'cone'

def Cone(centro, r, altura, direcao, cor, K_e,K_d,K_a, m, com_base = 1):
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
        'v' : v,
        'com_base': com_base
    }


def IntersecaoCone(cone, Po, D): #D = centro do pixel atual, coincide com a direção do raio lançado
    v       = Subtracao_vetores(cone['v'], Po)
    drdotdc = Produto_escalar(D, cone['direcao'])
    drdotdr = Produto_escalar(D,D)
    vdotdr  = Produto_escalar(v,D)
    vdotdc  = Produto_escalar(v,cone['direcao'])
    vdotv   = Produto_escalar(v,v)
    h2      = cone['altura']*cone['altura']
    r2      = cone['r']*cone['r']
    costet2 = h2/(h2 + r2)

    a = math.pow(drdotdc,2) - drdotdr*costet2
    b = 2*(vdotdr*costet2   - vdotdc*drdotdc)
    c = math.pow(vdotdc,2)  - vdotv* costet2

    delta = b * b - 4 * a * c

    if(delta < 0):
        return math.inf

    t1 = (-b + math.sqrt(delta)) / (2*a)
    t2 = (-b - math.sqrt(delta)) / (2*a)

    if   (t1 >= t2 and t2 > 0):
        return t2
    elif (t1 < t2 and t1 > 0):
        return t1
    elif (t1 < 0 and t2 > 0):
        return t2
    elif (t2 < 0 and t1 > 0):
        return t1
    return  math.inf

