import math

from calc_vetores import Soma_vetores, Subtracao_vetores, Produto_escalar, Vetor, Vetor_escalar, normalizaVetor

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
        return math.inf
    t_i = -numerador/denominador
    if(t_i < 0):
        return math.inf
    
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
    
    delta = b * b - 4* a * c
  
    if(delta < 0):
        return math.inf
    
    t1 = (-b + math.sqrt(delta)) / (2*a)
    t2 = (-b - math.sqrt(delta)) / (2*a)
    
    if(t1 < t2):
        return t1
    return  t2

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

