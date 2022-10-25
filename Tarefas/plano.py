from calc_vetores import Vetor

tipo= 'plano'

def Plano(p_pi, n_bar, cor, K_e,K_d,K_a, m, imagem=None):
    return {
        'tipo': tipo ,
        'p_pi': p_pi,
        'n_bar': n_bar, 
        'cor': cor, 
        'K_e': K_e, 
        'K_d': K_d, 
        'K_a': K_a,
        'm': m,
        'imagem': imagem,
    }

def PlanoBase(p_pi, n_bar):
    return {
    
        'p_pi': p_pi,
        'n_bar': n_bar, 
    
    }