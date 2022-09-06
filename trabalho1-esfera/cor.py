import math

from calc_vetores import Subtracao_vetores, Produto_escalar, Ponto, Vetor, Vetor_escalar, Produto_arroba, Calcula_vetor_refletido

def Cor(r, g, b):
    return {'r': r, 'g': g, 'b': b}

def Intersecao(esfera, posicaoOlhoObservador, D): #D = centro do pixel atual
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

def Calcula_ponto_intersecao(posicaoOlhoObservador, t, D): #D = centro do pixel atual
    return Ponto(
        posicaoOlhoObservador['x']+t*D['x'], 
        posicaoOlhoObservador['y']+t*D['y'], 
        posicaoOlhoObservador['z']+t*D['z'], 
    )

def Calcula_iluminacao( N, L, r_refletido,v_vetor):
    intensidade_d = 0.0 #difusa
    intensidade_e = 0.0 #escalar
    intensidade_a = 0.0 #ambiente
    m = 10
    fd = max(0, Produto_escalar(L, N))
    fe = pow(max(0, Produto_escalar(r_refletido, v_vetor)), m)
    I_F = Vetor(0.7, 0.7, 0.7)  # Intensidade da fonte 
    I_A = Vetor(0.5, 0.5, 0.5) # Intensidade da luz ambiente
    K = Vetor(0, 0.7, 0.7)  # Constante de opacidade do objeto. (quanto de vermelho o objt vai refletir, quanto de verde o objt vai refletir, quanto de azul o objt vai refletir)
 
    intensidade_d = Vetor_escalar(Produto_arroba(I_F, K) , fd)   #luz difusa
    intensidade_e = Vetor_escalar(Produto_arroba(I_F, K), fe) #luz especular
    intensidade_a = Produto_arroba(I_A, K) #luz ambiente
   
    return Vetor(intensidade_d['x']+intensidade_e['x']+intensidade_a['x'], 
                intensidade_d['y']+intensidade_e['y']+intensidade_a['y'], 
                intensidade_d['z']+intensidade_e['z']+intensidade_a['z']) 

# cena recebe  o raio e retorna a cor do objeto mais próximo
def DecideCor(posicaoOlhoObservador, cena, canvas, D, P_F): #D = centro do pixel atual
    t_proximo = math.inf
    objeto_encontrado = None
    intensidade = 0.0
    for objeto in cena['objetos']:
        [t1, t2] = Intersecao(objeto, posicaoOlhoObservador, D)
        if( t1 < t_proximo):
            t_proximo = t1
            objeto_encontrado = objeto

        if( t2 < t_proximo):
            t_proximo = t2
            objeto_encontrado = objeto
    if(objeto_encontrado != None):
        P = Calcula_ponto_intersecao(posicaoOlhoObservador,t_proximo , D) #ponto que o raio atual incidiu

        N = Subtracao_vetores(P, objeto_encontrado['centro'])
        N = Vetor(N['x']/objeto_encontrado['r'], N['y']/objeto_encontrado['r'], N['z']/objeto_encontrado['r']) #normalizando o vetor N
        #calculo do L
        L = Subtracao_vetores(P_F, P)
        comprimentoL = math.sqrt(Produto_escalar(L, L))
        L = Vetor(L['x']/comprimentoL, L['y']/comprimentoL, L['z']/comprimentoL)
        #calculo do I
        # I = Subtracao_vetores(P, P_F)
        # comprimentoI = math.sqrt(Produto_escalar(I, I))
        # I = Vetor(I['x']/comprimentoI, I['y']/comprimentoI, I['z']/comprimentoI)
        
        v_vetor = Subtracao_vetores(posicaoOlhoObservador, P)
        comprimentoV = math.sqrt(Produto_escalar(v_vetor, v_vetor)) 
        v_vetor = Vetor(v_vetor['x']/comprimentoV, v_vetor['y']/comprimentoV, v_vetor['z']/comprimentoV)
        r_vetor_refletido = Calcula_vetor_refletido(L, N)
        intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor)

    if(objeto_encontrado == None):
        return canvas['cor_fundo']
    
    return Cor(round(intensidade['x']*255),
               round(intensidade['y']*255),
              round(intensidade['z']*255))