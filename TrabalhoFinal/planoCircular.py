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
                     self.centroPlano, self.n_bar, self.raioCilindro, self)

    def getNormal(self, _): #calcula e retorna a normal do ponto da superficie esfera
        #return Subtracao_vetores(ponto , self.posicaoCentro) / self.raioEsfera
        return normalizaVetor(self.n_bar)

    def getColor(self):
        return self.material.cor

    def mundoParaCamera(self, matriz):
        self.centroPlano = mult_matriz_ponto(matriz, self.centroPlano)
        self.n_bar = mult_matriz_vetor(matriz, self.n_bar)
    
def intersecao(raio, infoIntersecao, centroPlano , n_bar, raioCilindro, obj):

    w = Subtracao_vetores(raio.origem, centroPlano )
   
    numerador   = Produto_escalar(w, n_bar)
    denominador = Produto_escalar(raio.direcao, n_bar)
    
    if(denominador == 0 ):
        return 
    t_i = -numerador/denominador
    if(t_i < 0):
        return 
    
    
    P_base = Calcula_ponto_intersecao(raio.origem, t_i, raio.direcao)
    P_Cb            = Subtracao_vetores(P_base, centroPlano)
    comprimentoP_Cb = math.sqrt(Produto_escalar(P_Cb, P_Cb)) 
    if(comprimentoP_Cb > raioCilindro):
        return

    infoIntersecao.atualizaIntersecao(t_i, obj)