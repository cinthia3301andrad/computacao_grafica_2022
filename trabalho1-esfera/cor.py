import math

from calc_vetores import Soma_vetores, Subtracao_vetores, Produto_escalar, Ponto, Vetor, Vetor_escalar, Produto_arroba, Calcula_vetor_refletido, calcula_M_cilindro, mult_matriz_vetor
from intersecoes import IntersecaoCilindro, IntersecaoEsfera, IntersecaoPlano

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
    m = objeto_encontrado['m']
    fd = max(0, Produto_escalar(L, N))
    fe = pow(max(0, Produto_escalar(r_refletido, v_vetor)), m)
    I_F = Vetor(0.7, 0.7, 0.7)  # Intensidade da fonte 
    I_A = Vetor(0.3, 0.3, 0.3) # Intensidade da luz ambiente
    
    K_e = objeto_encontrado['K_e'] #Opacidade do objeto. (quanto de vermelho o objt vai refletir, quanto de verde o objt vai refletir, quanto de azul o objt vai refletir)
    K_d = objeto_encontrado['K_d']
    K_a = objeto_encontrado['K_a']
    
    
    intensidade_d = Vetor_escalar(Produto_arroba(I_F,  K_d) , fd)   #luz difusa
    intensidade_e = Vetor_escalar(Produto_arroba(I_F, K_e), fe) #luz especular
    intensidade_a = Produto_arroba(I_A, K_a) #luz ambiente

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
    t_proximo_cilindro = math.inf
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
        if(objeto['tipo'] == 'cilindro'):
            
            [t1, t2]  =  IntersecaoCilindro(objeto, posicaoOlhoObservador, D)
            print('entrou para encontrar o cilindro', t1, t2)
            if( t1 < t_proximo):
                t_proximo_cilindro = t1
               

            if( t2 < t_proximo):
                t_proximo_cilindro = t2
                
            P = Calcula_ponto_intersecao(posicaoOlhoObservador, t_proximo_cilindro , D)
            comprimentoP_Cb = math.sqrt(Produto_escalar(P, objeto['centro'])) 
            print(comprimentoP_Cb, "COMPRIMENTO DO VETOR ATE O PONTO P")
            #raio/plano da base
            if(comprimentoP_Cb <= objeto['r']):
                t_proximo = t_proximo_cilindro
                objeto_encontrado = objeto
                print('AQUI O PONTO NO CILINDRO',t_proximo)
    t_proximo = t_proximo 
    return [t_proximo, objeto_encontrado]
    
# cena recebe  o raio e retorna a cor do objeto mais próximo
def DecideCor(posicaoOlhoObservador, cena, canvas, D, P_F): #D = centro do pixel atual
    t_proximo = math.inf
    objeto_encontrado = None
    intensidade = 0.0

    [t_proximo, objeto_encontrado] =  Intersecao_objeto_proximo(posicaoOlhoObservador, D, cena)

    if(objeto_encontrado != None and objeto_encontrado['tipo'] == 'esfera'):
        t_corrigido = t_proximo - 0.1
        P = Calcula_ponto_intersecao(posicaoOlhoObservador,t_corrigido , D) #ponto que o raio atual incidiu

        N = Subtracao_vetores(P, objeto_encontrado['centro'])
        N = Vetor(N['x']/objeto_encontrado['r'], N['y']/objeto_encontrado['r'], N['z']/objeto_encontrado['r']) #normalizando o vetor N
        #calculo do L
        L = Calc_L(P_F, P)
        
        v_vetor = Subtracao_vetores(posicaoOlhoObservador, P)
        comprimentoV = math.sqrt(Produto_escalar(v_vetor, v_vetor)) 
        v_vetor = Vetor(v_vetor['x']/comprimentoV, v_vetor['y']/comprimentoV, v_vetor['z']/comprimentoV)
        r_vetor_refletido = Calcula_vetor_refletido(L, N)
        #intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado)

        pf_pi = Subtracao_vetores(P_F, P)
        #comprimentoPf_pi = math.sqrt(Produto_escalar(pf_pi, pf_pi))
        tam_pf_pi = math.sqrt(Produto_escalar(pf_pi, pf_pi))
        pf_pi = Vetor(pf_pi['x']/tam_pf_pi, pf_pi['y']/tam_pf_pi, pf_pi['z']/tam_pf_pi) #normalizando o vetor 

        [s, _] = Intersecao_objeto_proximo(P, L, cena)  
        
        if(s > 0 and s < tam_pf_pi):   
            intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado, True)
        else:
            intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado)


    if(objeto_encontrado != None and objeto_encontrado['tipo'] == 'plano'):
        t_corrigido = t_proximo - 0.1
        P = Calcula_ponto_intersecao(posicaoOlhoObservador,t_corrigido , D) #ponto que o raio atual incidiu
        L = Calc_L(P_F, P)
        N = objeto_encontrado['n_bar']
        pf_pi = Subtracao_vetores(P_F, P)
        comprimentoPf_pi = math.sqrt(Produto_escalar(pf_pi, pf_pi))
        comprimentoV = math.sqrt(Produto_escalar(D, D)) 
        v_vetor = Vetor(-D['x']/comprimentoV, -D['y']/comprimentoV, -D['z']/comprimentoV)
        r_vetor_refletido = Calcula_vetor_refletido(L, N)

        tam_pf_pi = math.sqrt(Produto_escalar(pf_pi, pf_pi))
        pf_pi = Vetor(pf_pi['x']/tam_pf_pi, pf_pi['y']/tam_pf_pi, pf_pi['z']/tam_pf_pi) #normalizando o vetor 

        [s, _] = Intersecao_objeto_proximo(P, pf_pi, cena)  
       
        if(s > 0 and s < comprimentoPf_pi):   
            intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado, True)
        else:
            intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado)

    if(objeto_encontrado != None and objeto_encontrado['tipo'] == 'cilindro'):
     
        P = Calcula_ponto_intersecao(posicaoOlhoObservador,t_corrigido , D) #ponto que o raio atual incidiu
        M = calcula_M_cilindro(objeto_encontrado['direcao'])
        P_Cb = Subtracao_vetores(P - objeto_encontrado['centro'])
        L = Calc_L(P_F, P)
        N = mult_matriz_vetor(M, P_Cb)  
        r_vetor_refletido = Calcula_vetor_refletido(L, N)
        comprimentoV = math.sqrt(Produto_escalar(D, D)) 
        v_vetor = Vetor(-D['x']/comprimentoV, -D['y']/comprimentoV, -D['z']/comprimentoV)
        intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado)



        print("estou indo para a sombra?")
    
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
    