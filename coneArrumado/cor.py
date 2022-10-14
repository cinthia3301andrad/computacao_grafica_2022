import math
from cubo import *
from   plano import *
from   calc_vetores import Soma_vetores, Subtracao_vetores, Produto_escalar, Ponto, Vetor, Vetor_escalar, Produto_arroba, Calcula_vetor_refletido, calcula_M_cilindro, mult_matriz_vetor, produto_vetorial, normalizaVetor
from intersecoes import IntersecaoCilindro,IntersecaoCubo,  IntersecaoEsfera, IntersecaoPlano, IntersecaoCone

def Cor(r, g, b):
    return {'r': r, 'g': g, 'b': b}

# Calcula o ponto gerado pelo parâmetro t de um raio
def Calcula_ponto_intersecao(Po, t, D): #D = centro do pixel atual
    return Ponto(
        Po['x'] + t*D['x'],
        Po['y'] + t*D['y'],
        Po['z'] + t*D['z'],
    )
    
def Calc_L(P_F, P):
    L = normalizaVetor(Subtracao_vetores(P_F, P))
    return L

# Calcula a energia que vem do ponto observado, após interação do material com as fontes luminosas
def Calcula_iluminacao( N, L, r_refletido,v_vetor, objeto_encontrado, temSombra = False):
    # incicialização das contribuições ambiente, difusa e especular
    intensidade_a = 0.0 #ambiente
    intensidade_d = 0.0 #difusa
    intensidade_e = 0.0 #especular
    
    # Normalização dos vetores recebidos
    N           = normalizaVetor (N)
    L           = normalizaVetor (L)
    r_refletido = normalizaVetor (r_refletido)
    v_vetor     = normalizaVetor (v_vetor)
    
    # Cálculo do fator de atenuação da reflexão difusa
    fd = max(0, Produto_escalar(L, N))
  
    # Cálculo do fator de atenuação da reflexão especular
    m   = objeto_encontrado['m']
    fe  = pow(max(0, Produto_escalar(r_refletido, v_vetor)), m)
    
    # Intensidades das fontes de iluminação
    I_A = Vetor(0.3, 0.3, 0.3) # Ambiente
    I_F = Vetor(0.7, 0.7, 0.7) # Pontual
    
    #Reflectividade do material nos canais r, g e b para reflexões ambiente, difusa e especular
    K_a = objeto_encontrado['K_a']
    K_d = objeto_encontrado['K_d']
    K_e = objeto_encontrado['K_e']
    
    # Cálculo das contribuições de energia resultantes das reflexões Ambiente, Difusa e Especular
    intensidade_a = Produto_arroba(I_A, K_a)                    # Luz ambiente
    intensidade_d = Vetor_escalar(Produto_arroba(I_F, K_d), fd) # Reflexão difusa
    intensidade_e = Vetor_escalar(Produto_arroba(I_F, K_e), fe) # Reflexão especular
    

    if(temSombra): # Retorna apenas a contribuição ambiente
        return Vetor(intensidade_a['x'], intensidade_a['y'], intensidade_a['z'])
    # Caso contrário, o ponto está sendo iluminado pela fonte (retorna todas as contribuições)
    return Vetor(intensidade_a['x'] + intensidade_d['x'] + intensidade_e['x'],
                 intensidade_a['y'] + intensidade_d['y'] + intensidade_e['y'],
                 intensidade_a['z'] + intensidade_d['z'] + intensidade_e['z'])

# Cálculo da interseção com o objeto mais próximo do observador
def Intersecao_objeto_proximo(Po, D, cena, shadowcheck):
    # Po é o ponto de partida do raio
    # D  é o vetor direção do raio
    # cena contém os objetos do cenário
    # shadowcheck é um flag que, se =1, indica o interesse apenas na obstrução do raio com qualquer objeto.
    #
    t_proximo          = math.inf   # indica o valor do parâmetro do raio associado ao ponto de impacto
    objeto_encontrado  = None       # indica o objeto da cena  que foi atingido pelo raio
    hit                = 0          # indica a parte do objeto que foi atingida pelo raio
    
    for objeto in cena['objetos']:
        # Interseção com esfera
        if(objeto['tipo'] == 'esfera'):
            [t1, t2] = IntersecaoEsfera(objeto, Po, D)
            if(t1 > 0. and t1 < t_proximo):
                t_proximo         = t1
                objeto_encontrado = objeto
                if (shadowcheck == 1): return [t_proximo, objeto_encontrado, hit]

            if(t2 > 0. and t2 < t_proximo):
                t_proximo         = t2
                objeto_encontrado = objeto
                if (shadowcheck == 1): return [t_proximo, objeto_encontrado, hit]
        
        # Interseção com plano
        if(objeto['tipo'] == 'plano'):
            t1 =  IntersecaoPlano(objeto, Po, D)
            if( t1 > 0. and t1 < t_proximo  ):
                t_proximo         = t1
                objeto_encontrado = objeto
                if (shadowcheck == 1): return [t_proximo, objeto_encontrado, hit]

        # Interseção com cilindro
        if(objeto['tipo'] == 'cilindro'):
            t_cilindro = math.inf
            t_base     = math.inf
            t_topo     = math.inf
            hit        = 0
            
            # Cálculo da interseção com a superfície cilíndrica
            t1  =  IntersecaoCilindro(objeto, Po, D)
            if( t1 > 0 and t1 < t_cilindro):
                t_cilindro = t1
                P          = Calcula_ponto_intersecao(Po, t_cilindro , D)
                projecao   = Produto_escalar(Subtracao_vetores( P,objeto['centro'] ), objeto['direcao'])
                if(projecao < 0 or projecao > objeto['altura']): # Ponto de interseção inválido
                      t_cilindro = math.inf
        
            # Cálculo da interseção com o plano da base do cilindro
            plano_base = PlanoBase(objeto['centro'], 
                    Vetor(-objeto['direcao']['x'], -objeto['direcao']['y'],-objeto['direcao']['z'])) 
            t1     =  IntersecaoPlano(plano_base, Po, D)
       
            if(t1 > 0 and t1 < t_base):
                t_base = t1
                P_base          = Calcula_ponto_intersecao(Po, t_base , D)
                P_Cb            = Subtracao_vetores(P_base, objeto['centro'])
                comprimentoP_Cb = math.sqrt(Produto_escalar(P_Cb, P_Cb)) 

                if(comprimentoP_Cb > objeto['r'] ): #t base invalido
                    t_base = math.inf
            
            # Cálculo da interseção com o plano do topo do cilindro
            centroTopo = Soma_vetores(objeto['centro'], Vetor_escalar(objeto['direcao'], objeto['altura']))
            plano_topo = PlanoBase(centroTopo, objeto['direcao']) 
            t1         = IntersecaoPlano(plano_topo, Po, D)
               
            if(t1 > 0 and t1 < t_topo):
                t_topo = t1
                P_topo               = Calcula_ponto_intersecao(Po, t_topo , D)
                P_Cb_topo            = Subtracao_vetores(P_topo, centroTopo)
                comprimentoP_Cb_topo = math.sqrt(Produto_escalar(P_Cb_topo, P_Cb_topo)) 

                if(comprimentoP_Cb_topo > objeto['r'] ): #t base invalido
                    t_topo = math.inf
                
            #validações na base e do topo
            t_min_cilindro = min(t_cilindro, t_base, t_topo)
            if(t_min_cilindro > 0 and t_min_cilindro < math.inf):
                if(t_min_cilindro == t_cilindro): hit = 0
                if(t_min_cilindro == t_base):     hit = 1
                if(t_min_cilindro == t_topo):     hit = 2
            
            if (t_min_cilindro > 0 and t_min_cilindro < t_proximo):
                t_proximo         = t_min_cilindro
                objeto_encontrado = objeto
                if (shadowcheck == 1): return [t_proximo, objeto_encontrado, hit]

        # Interseção com cone
        if(objeto['tipo'] == 'cone'):
            com_base = objeto['com_base']
            t_cone   = math.inf
            t_base   = math.inf
            hit      = 0
            
            # Cálculo da interseção com a superfície cônica
            t_p      = IntersecaoCone(objeto, Po, D)
            
            if( t_p != None and t_p < t_cone ):
                t_cone   = t_p
                P        = Calcula_ponto_intersecao(Po, t_cone , D)
                projecao = Produto_escalar(Subtracao_vetores( objeto['v'] ,P), objeto['direcao']) 
                
                if(projecao < 0 or projecao > objeto['altura']): # P é inválido
                    t_cone = math.inf
                
            # Cálculo da interseção com o plano da base do cone
            plano_base = PlanoBase(objeto['centro'], 
                    Vetor(-objeto['direcao']['x'], -objeto['direcao']['y'],-objeto['direcao']['z'])) 
            t_base     = IntersecaoPlano(plano_base, Po, D)
            
            if(t_base != None):
                P_base          = Calcula_ponto_intersecao(Po, t_base , D)
                P_Cb            = Subtracao_vetores(P_base, objeto['centro'])
                comprimentoP_Cb = math.sqrt(Produto_escalar(P_Cb, P_Cb)) 

                if(comprimentoP_Cb > objeto['r']): #t base invalido
                    t_base = math.inf
                
            #validações na base 
            t_min_cone = max (0, min(t_cone, t_base))
            if(t_min_cone> 0 and t_min_cone < math.inf): # Interseção válida com corpo ou base do cone.
                if(t_min_cone == t_cone): # A interseção foi com a superfície cônica
                    hit=0
                    if (shadowcheck == 1): return [t_min_cone, objeto, hit]
                if(t_min_cone == t_base and com_base == 1): # A interseção foi com a base existente
                    hit=1
                    if (shadowcheck == 1): return [t_min_cone, objeto, hit]
                if(t_min_cone == t_base and com_base == 0): # A interseção com a base inexistente
                   if (t_cone > 0 and t_cone < math.inf):
                      # Interseção pode ser transferida para a interseção válida com a superfície do cone
                      t_min_cone = t_cone
                      hit        = 3
                      if (shadowcheck == 1): return [t_min_cone, objeto, hit]
                   # Não houve interseção válida com o cone sem base
                   if (shadowcheck == 1): return [math.inf, objeto, hit]
                   
            if (t_min_cone > 0 and t_min_cone < t_proximo):
                t_proximo         = t_min_cone
                objeto_encontrado = objeto
            
        if(objeto['tipo'] == 'cubo'):
            t1 = IntersecaoCubo(objeto, Po, D)
            if( t1 > 0. and t1 < t_proximo  ):
                t_proximo         = t1
                objeto_encontrado = objeto
                if (shadowcheck == 1): return [t_proximo, objeto_encontrado, hit]
    return [t_proximo, objeto_encontrado, hit]       
                
    
# cena recebe  o raio e retorna a cor do objeto mais próximo
def DecideCor(Po, cena, canvas, D, P_F):
    # Po é o ponto de partida do raio
    # D  é o vetor direção do raio
    # cena contém os objetos do cenário
    # canvas define as dimensões em pixels da área de exposição da imagem

    t_proximo         = math.inf
    objeto_encontrado = None
    hit               = 0
    intensidade       = 0.0
    shadowcheck       = 0        # se = 1, indica o interesse na obstrução do raio de luz com qualquer objeto.
    

    [t_proximo, objeto_encontrado, hit] =  Intersecao_objeto_proximo(Po, D, cena, shadowcheck)
    
    shadowcheck = 1
  
    if(objeto_encontrado != None and objeto_encontrado['tipo'] == 'esfera'):
        t_corrigido = t_proximo - 0.1
        P = Calcula_ponto_intersecao(Po,t_corrigido , D) #ponto que o raio atual incidiu

        L                 = Calc_L(P_F, P)
        v_vetor           = normalizaVetor(Subtracao_vetores(Po, P))
        N                 = normalizaVetor(Subtracao_vetores(P, objeto_encontrado['centro']))
        r_vetor_refletido = normalizaVetor(Calcula_vetor_refletido(L, N))
        
        # Cálculo da distância entre o ponto de interseção e a fonte luminosa
        pf_pi     = Subtracao_vetores(P_F, P)
        tam_pf_pi = math.sqrt(Produto_escalar(pf_pi, pf_pi))

        # Verifica se o raio que ilumina o ponto de interseção está obstruído
        if (shadowcheck == 1):
            [s, _, _]   = Intersecao_objeto_proximo(P, L, cena, shadowcheck)
        else:
            s = tam_pf_pi
        
        if(s > 0 and s < tam_pf_pi):   
            intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado, True)
        else:
            intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado)

    if(objeto_encontrado != None and objeto_encontrado['tipo'] == 'plano'):
        t_corrigido = t_proximo - 0.1
        P = Calcula_ponto_intersecao(Po,t_corrigido , D) # Ponto atingido pelo raio
        
        L                 = Calc_L(P_F, P)
        v_vetor           = normalizaVetor(Subtracao_vetores(Po, P))
        N                 = normalizaVetor(objeto_encontrado['n_bar'])
        r_vetor_refletido = normalizaVetor(Calcula_vetor_refletido(L, N))

        # Cálculo da distância entre o ponto de interseção e a fonte luminosa
        pf_pi     = Subtracao_vetores(P_F, P)
        tam_pf_pi = math.sqrt(Produto_escalar(pf_pi, pf_pi))
        
        # Verifica se o raio que ilumina o ponto de interseção está obstruído
        if (shadowcheck == 1):
            [s, _, _]   = Intersecao_objeto_proximo(P, L, cena, shadowcheck)
        else:
            s = tam_pf_pi
       
        if(s > 0 and s < tam_pf_pi):
            intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado, True)
        else:
            intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado)

    if(objeto_encontrado != None and objeto_encontrado['tipo'] == 'cilindro'):
        #return objeto_encontrado['cor']
        t_corrigido = t_proximo - 0.1
        P = Calcula_ponto_intersecao(Po,t_corrigido , D) # Ponto atingido pelo raio
        
        L                 = Calc_L(P_F, P)
        v_vetor           = normalizaVetor(Subtracao_vetores(Po, P))
        
        if(hit == 0): # Raio atinge superfície do cilindro
            M    = calcula_M_cilindro(objeto_encontrado['direcao'])
            P_Cb = Subtracao_vetores(P, objeto_encontrado['centro'])
            N    = normalizaVetor(mult_matriz_vetor(M, P_Cb))
            
        else:
            if(hit == 1): # Raio atinge a base do cilindro
                N = normalizaVetor(Vetor_escalar(objeto_encontrado['direcao'],-1.0))
            else: # Raio atinge o topo do cilindro
                N =  normalizaVetor(objeto_encontrado['direcao'])
                
        r_vetor_refletido = normalizaVetor(Calcula_vetor_refletido(L, N))
        
        # Cálculo da distância entre o ponto de interseção e a fonte luminosa
        pf_pi     = Subtracao_vetores(P_F, P)
        tam_pf_pi = math.sqrt(Produto_escalar(pf_pi, pf_pi))
        
        # Verifica se o raio que ilumina o ponto de interseção está obstruído
        if (shadowcheck == 1):
            [s, _, _]   = Intersecao_objeto_proximo(P, L, cena, shadowcheck)
        else:
            s = tam_pf_pi
        
        if(s > 0 and s < tam_pf_pi):
            intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado, True)
        else:
            intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado)
        
    if(objeto_encontrado != None and objeto_encontrado['tipo'] == 'cone'):
     
        t_corrigido = t_proximo - 0.1
        P           = Calcula_ponto_intersecao(Po,t_corrigido , D)
        
        L           = Calc_L(P_F, P)
        v_vetor     = normalizaVetor(Subtracao_vetores(Po, P))
        PV          = Subtracao_vetores(objeto_encontrado['v'], P)

        if(hit == 0): # Raio atinge o corpo do cone
            N_barra = produto_vetorial(PV, objeto_encontrado['direcao'])
            N       = normalizaVetor(produto_vetorial(N_barra, PV))
            
        elif(hit == 3): # Raio passa pela base aberta e atinge o corpo do cone
            
            N_barra = produto_vetorial(PV, objeto_encontrado['direcao'])
            N       = normalizaVetor(produto_vetorial(PV, N_barra)) # N aponta para o interior
        
        else: # Raio atinge a base do cone
            N       = normalizaVetor(Vetor_escalar(objeto_encontrado['direcao'],-1.0))
          
        r_vetor_refletido = normalizaVetor(Calcula_vetor_refletido(L, N))

        # Cálculo da distância entre o ponto de interseção e a fonte luminosa
        pf_pi     = Subtracao_vetores(P_F, P)
        tam_pf_pi = math.sqrt(Produto_escalar(pf_pi, pf_pi))

        # Verifica se o raio que ilumina o ponto de interseção está obstruído
        if (shadowcheck == 1):
            [s, _, _]   = Intersecao_objeto_proximo(P, L, cena, shadowcheck)
        else:
            s = tam_pf_pi
     
        if(s > 0 and s < tam_pf_pi):
            intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado, True)
        else:
            intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado)

    if(objeto_encontrado != None and objeto_encontrado['tipo'] == 'cubo'):
        t_corrigido = t_proximo - 0.1
        P = Calcula_ponto_intersecao(Po, t_corrigido , D) #ponto que o raio atual incidiu
        L                 = Calc_L(P_F, P)
        v_vetor           = normalizaVetor(Subtracao_vetores(Po, P))
        N                 = objeto_encontrado['normal']
        r_vetor_refletido = normalizaVetor(Calcula_vetor_refletido(L, N))
        
        # Cálculo da distância entre o ponto de interseção e a fonte luminosa
        pf_pi     = Subtracao_vetores(P_F, P)
        tam_pf_pi = math.sqrt(Produto_escalar(pf_pi, pf_pi))

        # Verifica se o raio que ilumina o ponto de interseção está obstruído
        if (shadowcheck == 1):
            [s, _, _]   = Intersecao_objeto_proximo(P, L, cena, shadowcheck)
        else:
            s = tam_pf_pi
        
        if(s > 0 and s < tam_pf_pi):   
            intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado, True)
        else:
            intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor, objeto_encontrado)
    if(objeto_encontrado == None):
        return canvas['cor_fundo']
    
    return Cor(round(intensidade['x']*255),
               round(intensidade['y']*255),
               round(intensidade['z']*255))


    
