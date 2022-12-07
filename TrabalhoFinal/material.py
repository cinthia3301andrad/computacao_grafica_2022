
class Material:
    def __init__(self, cor,k_difusa,k_especular, k_ambiente, m,  imagem = None):
        self.cor = cor
        
        self.k_difusa = k_difusa
        self.k_especular = k_especular
        self.k_ambiente = k_ambiente
        self.m = m
        self.imagem = imagem

    