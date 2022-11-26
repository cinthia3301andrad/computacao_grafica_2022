
class Plano:
    def __init__(self, tipo: "Plano", p_pi, n_bar, cor, K_e,K_d,K_a, m, imagem=None):
        self.tipo = tipo 
        self.p_pi = p_pi
        self.n_bar = n_bar
        self.cor = cor 
        self.K_e = K_e
        self.K_d = K_d
        self.K_a = K_a
        self.m = m
        self.imagem = imagem
    
class PlanoBase:
    def __init__(self, p_pi, n_bar):
        self.p_pi = p_pi
        self.n_bar = n_bar