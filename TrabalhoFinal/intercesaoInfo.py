# from raio import Raio
import numpy as np
from funcoes import Subtracao_vetores, Produto_escalar, Calcula_ponto_intersecao

class IntercesaoInfo:
    def __init__(self, raio):
        self.t_mais_proximo = 100000.0
        self.valido = False
        self.hitObjeto = None
        self.raio = raio

        # self.rayTrace(Raio(np.array([0., 0., 0.]), np.array([1., 0., 0.])))

    def atualizaIntersecao(self, novo_t, obj):
         if (novo_t < self.t_mais_proximo) :
                self.t_mais_proximo = novo_t
                self.valido = True
                self.hitObjeto = obj

    def atualizaObjeto(self, novo_objeto):
        if self.valido is True:
            self.hitObjeto = novo_objeto

    def getPontoAtual(self):
        return Calcula_ponto_intersecao(self.raio.origem, self.t_mais_proximo, self.raio.direcao)
   


