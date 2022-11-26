class Cilindro:
    def __init__(self, tipo: "Cilindro", centro, r, altura, direcao, cor, K_e,K_d,K_a, m):
        self.tipo = tipo 
        self.centro = centro
        self.r = r
        self.altura = altura
        self.direcao = direcao
        self.cor = cor
        self.K_e = K_e
        self.K_d = K_d
        self.K_a = K_a
        self.m = m