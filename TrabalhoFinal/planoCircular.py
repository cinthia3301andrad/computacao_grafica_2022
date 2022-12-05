from raio import Raio
import math
from objetos.objeto import Objeto
from funcoes import Calcula_ponto_intersecao, Subtracao_vetores, Produto_escalar, normalizaVetor, mult_matriz_ponto, mult_matriz_vetor

class PlanoCircular(Objeto):
    def __init__(self, centroPlano, n_bar,raioCilindro, material):
        self.centroPlano = centroPlano
        self.n_bar = n_bar
        self.raioCilindro = raioCilindro

        self.material= material
    def intersecao(self, raio: Raio ,infoIntersecao, obj):
        return intersecao(raio, infoIntersecao,
                     self.centroPlano, self.n_bar, self.raioCilindro,obj)

    def getNormal(self, _): #calcula e retorna a normal do ponto da superficie esfera
        #return Subtracao_vetores(ponto , self.posicaoCentro) / self.raioEsfera
        return normalizaVetor(self.n_bar)

    def getColor(self):
        return self.material.cor

    def mundoParaCamera(self, matriz):
        self.centroPlano = mult_matriz_ponto(matriz, self.centroPlano)
        self.n_bar = mult_matriz_vetor(matriz, self.n_bar)
    
def intersecao(raio, infoIntersecao, centroPlano , n_bar, raioCilindro, obj):
    h1 = Produto_escalar(Subtracao_vetores(centroPlano, raio.origem), n_bar)
    h2 = Produto_escalar(raio.direcao, n_bar)
    if (h2 == 0 or (h1 / h2) <= 1) :
        return
            
    t = h1 / h2

    P_base = Calcula_ponto_intersecao(raio.origem, t, raio.direcao)
    P_Cb            = Subtracao_vetores(P_base, centroPlano)
    comprimentoP_Cb = math.sqrt(Produto_escalar(P_Cb, P_Cb)) 
    if(comprimentoP_Cb > raioCilindro):
        return
    centroPonto = Subtracao_vetores(P_base, centroPlano)
    infoIntersecao.atualizaIntersecao(t, obj)