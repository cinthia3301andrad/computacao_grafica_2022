import math
from calc_vetores import *


from PIL import Image
from cone import *


from cilindro import *
import math  
from calc_vetores import *
from janela import *
from canvas import *
from cena import *
from esfera import *
from cor import *
from plano import *

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

    print('t1', t1, 't2', t2)

  

   
    
 

def main():

    posicaoOlhoObservador = Ponto(0, 20, 40)
    P_F = Ponto(0, 60 , -30) #Posição da fonte pontual situada a 5 centimetros acima do olho do observador.


    D = Vetor(0, 0, -1)


    centro_cone = Ponto(0, 0, 0)
    rCone = 40
    hCone = 40
    #d_cone = Vetor(-1/math.sqrt(3), 1/math.sqrt(3), -1/math.sqrt(3))
    d_cone = Vetor(0, 1, 0)

    K_d_chao = Vetor (0.8, 0.3, 0.2)
    #K_a_chao = Vetor(0.8, 0.3, 0.2)
    #K_e_chao = Vetor(0.8, 0.3, 0.2)

    K_a_chao = Vetor(0, 0, 0)
    K_e_chao = Vetor(0, 0, 0)

    m_cone = 100

    objeto_cone = Cone(centro_cone, 
                        rCone, hCone, d_cone,
                        Cor(255, 0, 0), K_e_chao, K_d_chao, K_a_chao, m_cone, 0)

    objeto_cone['intersecao'](objeto_cone, posicaoOlhoObservador, D)

   
main()