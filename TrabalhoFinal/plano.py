from raio import Raio
import math
from objetos.objeto import Objeto
from funcoes import Subtracao_vetores, Produto_escalar, normalizaVetor, mult_matriz_ponto, mult_matriz_vetor, produto_vetorial

class Plano(Objeto):
    def __init__(self, p_pi, n_bar, material, tipo= None):
        self.p_pi = p_pi
        self.n_bar = n_bar
        self.material= material
        self.tipo = tipo
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


    def matriz(self, C, D, S):
        I = Subtracao_vetores(D,C)
        
        J = Subtracao_vetores(S, C)
        
       
        LI  = math.sqrt(Produto_escalar(I, I))
        
        LJ  =  math.sqrt(Produto_escalar(J, J))
        #print('LI ', LI, LJ)
        i = normalizaVetor(I)
        j = normalizaVetor(J)
        k = produto_vetorial(i, j)
        M = [[i.x, i.y, i.z, -Produto_escalar(C, i)], [j.x, j.y, j.z, -Produto_escalar(C, j)], [k.x, k.y, k.z, -Produto_escalar(C, k)], [0, 0, 0, 1]]

        return (M, LI, LJ)
    
def intersecao(raio, infoIntersecao, p_pi , n_bar, obj):
    w = Subtracao_vetores(raio.origem, p_pi)
   
    numerador   = Produto_escalar(w, n_bar)
    denominador = Produto_escalar(raio.direcao , n_bar)
    
    if(denominador == 0 ):
        return math.inf
    t_i = -numerador/denominador
    if(t_i < 0):
        return math.inf
    
    t = raio.t
    if (0 < t_i < t): 
        t = t_i
    if (t == raio.t): 
        return None
        
    raio.t = t
    infoIntersecao.atualizaIntersecao(t, obj)