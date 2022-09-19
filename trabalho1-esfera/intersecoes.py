import math

from calc_vetores import Subtracao_vetores, Produto_escalar, Vetor_escalar

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

def IntersecaoPlano(plano, posicaoOlhoObservador, D):
    w = Subtracao_vetores(posicaoOlhoObservador, plano['p_pi'] )
   
    numerador = Produto_escalar(w, plano['n_bar'])
    denominador = Produto_escalar(D, plano['n_bar'])
    
    if(denominador == 0 ):
        return None
    t_i = -numerador/denominador
    if(t_i < 0):
        return None
    
    return t_i
    

def IntersecaoCilindro(cilindro, posicaoOlhoObservador, D): #D = centro do pixel atual, coincide com a direção do raio lançado
    prod_escalar = Produto_escalar(D, cilindro['direcao'])
    
    mult = Vetor_escalar(cilindro['direcao'], prod_escalar )
    
    w = Subtracao_vetores(D, mult)

    #nao tenho certeza que esse P é o certo
    v_primeiro = Subtracao_vetores(posicaoOlhoObservador, cilindro['centro'] )
    v_segundo = Vetor_escalar( cilindro['direcao'],
                                Produto_escalar(v_primeiro, cilindro['direcao']) 
                            ) 
    v = Subtracao_vetores(v_primeiro, v_segundo)
    
    a = Produto_escalar(w, w)
    b = 2*Produto_escalar(v, w)
    c = Produto_escalar(v, v) - cilindro['r'] * cilindro['r']

    delta = b * b - a * c
    print("delta",delta)
    if(delta < 0):
        return math.inf, math.inf
    
    t1 = (-b + math.sqrt(delta)) / a
    t2 = (-b - math.sqrt(delta)) / a
    
    return (t1, t2)



