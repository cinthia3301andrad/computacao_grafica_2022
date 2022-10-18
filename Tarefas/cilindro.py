tipo = 'cilindro'

def Cilindro(centro, r, altura, direcao, cor, K_e,K_d,K_a, m):
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
        'm': m
    }
