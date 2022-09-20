from calc_vetores import Vetor

tipo= 'plano'

def Plano(p_pi, n_bar, cor, K_e,K_d,K_a, m):
    return {
        'tipo': tipo ,
        'p_pi': p_pi,
        'n_bar': n_bar, 
        'cor': cor, 
        'K_e': K_e, 
        'K_d': K_d, 
        'K_a': K_a,
        'm': m
    }

def PlanoBase(p_pi, n_bar):
    return {
    
        'p_pi': p_pi,
        'n_bar': n_bar, 
    
    }