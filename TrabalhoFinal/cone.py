from raio import Raio
import math
from objetos.objeto import Objeto
from funcoes import Vetor, Subtracao_vetores, Produto_escalar, normalizaVetor, mult_matriz_ponto, Vetor_escalar, Soma_vetores, mult_matriz_vetor,produto_vetorial, Calcula_ponto_intersecao
from planoCircular import PlanoCircular
class Cone(Objeto):
    def __init__(self, centro, raio : float, altura, direcao, v, material): # ,com_base = 1
        self.centro = centro
        self.raio = raio
        self.altura = altura
        self.direcao = direcao
        self.material = material
        self.v = v
        #self.com_base = com_base

    def intersecao(self, raio: Raio, infoIntersecao, obj):
        return intersecao( raio, infoIntersecao, self.centro, self.direcao, self.raio, self.altura, self.v, obj)
    
    def getNormal(self, ponto): #calcula e retorna a normal do ponto da superficie esfera
        #return Subtracao_vetores(ponto , self.posicaoCentro) / self.raioEsfera
        PV = Subtracao_vetores(self.v, ponto)
        N_barra = produto_vetorial(PV, self.direcao)

        return normalizaVetor(produto_vetorial(N_barra, PV))

    def getColor(self):
        return self.material.cor

    def mundoParaCamera(self, matriz):
        self.centro = mult_matriz_ponto(matriz, self.centro)
        self.direcao = mult_matriz_vetor(matriz, self.direcao)

def intersecao(raio, infoIntersecao, centro, direcao, r, altura, v, obj):

    n_Base = Vetor(-direcao.x, -direcao.y,-direcao.z)
    basePlano = PlanoCircular(centro, n_Base, r, obj.material)

    basePlano.intersecao(raio, infoIntersecao, obj)
    
    v_cone     = Subtracao_vetores( v , raio.origem)
    drdotdc = Produto_escalar(raio.direcao, direcao)
    drdotdr = Produto_escalar( raio.direcao, raio.direcao)
    vdotdr  = Produto_escalar(v_cone, raio.direcao)
    vdotdc  = Produto_escalar(v_cone, direcao)
    vdotv   = Produto_escalar(v_cone,v_cone)
    h2      = altura * altura
    r2      = r*r
    costet2 = h2/(h2 + r2)

    a = math.pow(drdotdc,2) - drdotdr*costet2
    b = 2*(vdotdr*costet2   - vdotdc*drdotdc)
    c = math.pow(vdotdc,2)  - vdotv* costet2
    
    delta = b * b - 4 * a * c
  
    if(delta < 0):
        return math.inf
        
    if (a == 0):
        return  -c/b
    
    t1 = (-b + math.sqrt(delta)) / (2*a)
    t2 = (-b - math.sqrt(delta)) / (2*a)

    p1 = Calcula_ponto_intersecao(raio.origem, t1, raio.direcao)
    p2 = Calcula_ponto_intersecao(raio.origem, t2, raio.direcao)
  
    projecao1 = Produto_escalar(Subtracao_vetores(p1, centro), direcao)
    projecao2 = Produto_escalar(Subtracao_vetores(p2, centro), direcao)
    t = raio.t
 
    if(projecao1 >= 0 and projecao1 <= altura):
        t = t1
        raio.t = t
        infoIntersecao.atualizaIntersecao(t1, obj)
    if(projecao2 >= 0 and projecao2 <= altura):
        t = t2
        raio.t = t
        infoIntersecao.atualizaIntersecao(t2, obj)
