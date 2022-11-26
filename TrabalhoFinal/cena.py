# from raio import Raio
import numpy as np
class Cena:
    def __init__(self, largura: int, altura: int, objetos, luzes, sombras=True):
        self.largura = largura
        self.altura = altura
        self.objetos = objetos
        self.luzes = luzes
        self.loaded = False
        self.loading = False
        self.sombras = sombras

        # self.rayTrace(Raio(np.array([0., 0., 0.]), np.array([1., 0., 0.])))

    def desenha(self):
        print("desenha°",self.largura, self.altura, self.objetos)
   


