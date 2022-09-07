import math

from calc_vetores import Subtracao_vetores, Produto_escalar

def IntersecaoEsfera(esfera, posicaoOlhoObservador, D): #D = centro do pixel atual
    w = Subtracao_vetores(posicaoOlhoObservador, esfera['centro'])
   
    a = Produto_escalar(D, D)
    b = 2 * Produto_escalar(w, D)
    c = Produto_escalar(w, w) - esfera['r'] * esfera['r'] 

    delta = b * b - 4 * a * c
    if(delta < 0):
        return math.inf, math.inf

    t1 = (-b + math.sqrt(delta)) / (2 * a)
    t2 = (-b - math.sqrt(delta)) / (2 * a)
        
    return (t1, t2)
