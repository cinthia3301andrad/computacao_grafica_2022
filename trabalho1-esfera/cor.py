import math

from calc_vetores import Subtracao_vetores, Produto_escalar, Ponto, Vetor, Vetor_escalar, Produto_arroba, Calcula_vetor_refletido
from intersecoes import IntersecaoEsfera, IntersecaoPlano

def Cor(r, g, b):
    return {'r': r, 'g': g, 'b': b}


def Calcula_ponto_intersecao(posicaoOlhoObservador, t, D): #D = centro do pixel atual
    return Ponto(
        posicaoOlhoObservador['x']+t*D['x'], 
        posicaoOlhoObservador['y']+t*D['y'], 
        posicaoOlhoObservador['z']+t*D['z'], 
    )

def Calcula_iluminacao( N, L, r_refletido,v_vetor, objeto_encontrado, temSombra = False):
    intensidade_d = 0.0 #difusa
    intensidade_e = 0.0 #escalar
    intensidade_a = 0.0 #ambiente
    m = 10
    fd = max(0, Produto_escalar(L, N))
    fe = pow(max(0, Produto_escalar(r_refletido, v_vetor)), m)
    I_F = Vetor(0.7, 0.7, 0.7)  # Intensidade da fonte 
    I_A = Vetor(0.5, 0.5, 0.5) # Intensidade da luz ambiente
    K = objeto_encontrado['K']  # Constante de opacidade do objeto. (quanto de vermelho o objt vai refletir, quanto de verde o objt vai refletir, quanto de azul o objt vai refletir)

    
    
    intensidade_d = Vetor_escalar(Produto_arroba(I_F, K) , fd)   #luz difusa
    intensidade_e = Vetor_escalar(Produto_arroba(I_F, K), fe) #luz especular
    intensidade_a = Produto_arroba(I_A, K) #luz ambiente
    if(temSombra):

        return Vetor(intensidade_a['x'], 
                intensidade_a['y'], 
                intensidade_a['z']) 
    return Vetor(intensidade_d['x']+intensidade_e['x']+intensidade_a['x'], 
                intensidade_d['y']+intensidade_e['y']+intensidade_a['y'], 
                intensidade_d['z']+intensidade_e['z']+intensidade_a['z']) 


def Intersecao_objeto_proximo(posicaoOlhoObservador, D, cena):
    t_proximo = math.inf
    objeto_encontrado = None
    
    for objeto in cena['objetos']:
        if(objeto['tipo'] == 'esfera'):
            [t1, t2] = IntersecaoEsfera(objeto, posicaoOlhoObservador, D)
            if( t1 < t_proximo):
                t_proximo = t1
                objeto_encontrado = objeto

            if( t2 < t_proximo):
                t_proximo = t2
                objeto_encontrado = objeto
        if(objeto['tipo'] == 'plano'):
            t_p =  IntersecaoPlano(objeto, posicaoOlhoObservador, D)
            if( t_p != None and t_p < t_proximo  ):
                t_proximo = t_p
                objeto_encontrado = objeto

    return [t_proximo, objeto_encontrado]

    
# cena recebe  o raio e retorna a cor do objeto mais próximo
def DecideCor(posicaoOlhoObservador, cena, canvas, D, P_F): #D = centro do pixel atual
    t_proximo = math.inf
    objeto_encontrado = None
    intensidade = 0.0

    [t_proximo, objeto_encontrado] =  Intersecao_objeto_proximo(posicaoOlhoObservador, D, cena)
    
    if(objeto_encontrado != None and objeto_encontrado['tipo'] == 'esfera'):
        P = Calcula_ponto_intersecao(posicaoOlhoObservador,t_proximo , D) #ponto que o raio atual incidiu

        N = Subtracao_vetores(P, objeto_encontrado['centro'])
        N = Vetor(N['x']/objeto_encontrado['r'], N['y']/objeto_encontrado['r'], N['z']/objeto_encontrado['r']) #normalizando o vetor N
        #calculo do L
        L = Calc_L(P_F, P)
        
        v_vetor = Subtracao_vetores(posicaoOlhoObservador, P)
        comprimentoV = math.sqrt(Produto_escalar(v_vetor, v_vetor)) 
        v_vetor = Vetor(v_vetor['x']/comprimentoV, v_vetor['y']/comprimentoV, v_vetor['z']/comprimentoV)
        r_vetor_refletido = Calcula_vetor_refletido(L, N)
        intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado)

    if(objeto_encontrado != None and objeto_encontrado['tipo'] == 'plano'):
        P = Calcula_ponto_intersecao(posicaoOlhoObservador,t_proximo , D) #ponto que o raio atual incidiu
        L = Calc_L(P_F, P)
        N = objeto_encontrado['n_bar']
        pf_pi = Subtracao_vetores(P_F, P)
        comprimentoPf_pi = math.sqrt(Produto_escalar(pf_pi, pf_pi))
        comprimentoV = math.sqrt(Produto_escalar(D, D)) 
        v_vetor = Vetor(-D['x']/comprimentoV, -D['y']/comprimentoV, -D['z']/comprimentoV)
        r_vetor_refletido = Calcula_vetor_refletido(L, N)
        [s, _] = Intersecao_objeto_proximo(P, P_F, cena)
        if(s < comprimentoPf_pi):
        
            intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado, True)
        intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado)

      
    if(objeto_encontrado == None):
        return canvas['cor_fundo']
    
    return Cor(round(intensidade['x']*255),
               round(intensidade['y']*255),
              round(intensidade['z']*255))


def Calc_L(P_F, P):
    L = Subtracao_vetores(P_F, P)
    comprimentoL = math.sqrt(Produto_escalar(L, L))
    L = Vetor(L['x']/comprimentoL, L['y']/comprimentoL, L['z']/comprimentoL)
    return L
    