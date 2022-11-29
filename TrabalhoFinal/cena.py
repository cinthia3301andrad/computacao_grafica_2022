
import numpy as np
import math
from definicoes import Cor, Vetor, Ponto



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


    def computaLuzes(self, normal, P, raio, material):
        contribuicao = None
        for luz in self.luzes:
            r = luz.computaLuz(P, normal, raio, material).r
            g = luz.computaLuz(P, normal, raio, material).g
            b = luz.computaLuz(P, normal, raio, material).b
            if(contribuicao != None):
                contribuicao = Cor( contribuicao.r + r, 
                                contribuicao.g + g,
                                contribuicao.b + b)
            else:
                contribuicao = Cor(r, g, b)
        
        print(contribuicao.r * 255,contribuicao.g * 255,contribuicao.b * 255)

        return Cor(round(contribuicao.r * 255),round(contribuicao.g * 255), round(contribuicao.b * 255))
        

   


