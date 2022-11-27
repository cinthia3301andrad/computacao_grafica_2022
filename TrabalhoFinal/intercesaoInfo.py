# from raio import Raio
import numpy as np
class IntercesaoInfo:
    def __init__(self, raio):
        self.t_mais_proximo = 100000.0
        self.valido = False
        self.hitObjeto = None
        self.raio = raio

        # self.rayTrace(Raio(np.array([0., 0., 0.]), np.array([1., 0., 0.])))

    def atualizaIntersecao(self, novo_t):
         if (novo_t < self.t_mais_proximo) :
                self.t_mais_proximo = novo_t
                self.valido = True

    def atualizaObjeto(self, novo_objeto):
        self.hitObjeto = novo_objeto
   


