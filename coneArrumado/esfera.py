from calc_vetores import Subtracao_vetores, Vetor

tipo = 'esfera'

def Esfera(centro, r, cor, K_e,K_d,K_a, m):
    return {
        'tipo': tipo ,
        'centro': centro, 
        'r': r, 
        'cor': cor, 
        'K_e': K_e,
        'K_d': K_d,
        'K_a': K_a,
        'm': m
    }
#calculo do N 
def calcN(P, objeto_encontrado):
    N = Subtracao_vetores(P, objeto_encontrado['centro'])
    N = Vetor(N['x']/objeto_encontrado['r'], N['y']/objeto_encontrado['r'], N['z']/objeto_encontrado['r']) #normalizando o vetor N
    return N
