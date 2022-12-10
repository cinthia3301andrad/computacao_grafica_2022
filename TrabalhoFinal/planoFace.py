from raio import Raio
import math
from objetos.objeto import Objeto
from funcoes import Subtracao_vetores, Produto_escalar, normalizaVetor, mult_matriz_ponto, mult_matriz_vetor

class PlanoFace(Objeto):
    def __init__(self, p_pi, n_bar, material):
        self.p_pi = p_pi
        self.n_bar = n_bar
        self.material= material
    def intersecao(self, raio: Raio ,infoIntersecao, obj):
        return intersecao(raio, infoIntersecao, self.p_pi, self.n_bar, obj)

    def getNormal(self, _): #calcula e retorna a normal do ponto da superficie esfera
        #return Subtracao_vetores(ponto , self.posicaoCentro) / self.raioEsfera
        return normalizaVetor(self.n_bar)

    def getColor(self):
        return self.material.cor

    def mundoParaCamera(self, matriz):
        self.p_pi = mult_matriz_ponto(matriz, self.p_pi)
        self.n_bar = mult_matriz_vetor(matriz, self.n_bar)
    
def intersecao(raio, infoIntersecao, p_pi , n_bar, obj):
    w = Subtracao_vetores(raio.origem, p_pi)
   
    numerador   = Produto_escalar(w, n_bar)
    denominador = Produto_escalar(raio.direcao , n_bar)
    
    if(denominador == 0 ):
        return 
    t_i = -numerador/denominador
    if(t_i < 0):
        return 
    
    t = raio.t
    if (0 < t_i < t): 
        t = t_i
    if (t == raio.t): 
        return 
        
    raio.t = t
    infoIntersecao.atualizaIntersecao(t, obj)