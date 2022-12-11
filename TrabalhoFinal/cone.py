from raio import Raio
import math
from objetos.objeto import Objeto

from planoCircular import PlanoCircular
from funcoes import Calcula_ponto_intersecao, Vetor, Subtracao_vetores, Produto_escalar, normalizaVetor, mult_matriz_ponto, Vetor_escalar, Soma_vetores, mult_matriz_vetor,produto_vetorial
from planoCircular import PlanoCircular

from transformacoes import translacaoPonto, rotacaoPonto,rotacaoVetor, escalaPonto
class Cone(Objeto):
    def __init__(self, centro, raio : float, altura, direcao, v, material, basePlano): # ,com_base = 1
        self.centro = centro
        self.raio = raio
        self.altura = altura
        self.direcao = direcao
        self.material = material
        self.v = v
        self.basePlano = basePlano
        #self.com_base = com_base

    def intersecao(self, raio: Raio, infoIntersecao, obj):
        return intersecao( raio, infoIntersecao, self.centro, self.direcao, self.raio, self.altura, self.v, obj, self.basePlano)
    
    def getNormal(self, ponto): #calcula e retorna a normal do ponto da superficie esfera
        #return Subtracao_vetores(ponto , self.posicaoCentro) / self.raioEsfera
        PV = Subtracao_vetores(self.v, ponto)
        N_barra = produto_vetorial(PV, self.direcao)

        return normalizaVetor(produto_vetorial(N_barra, PV))

    def getColor(self):
        return self.material.cor

    def reCalculaPlanos(self):
        n_Base = Vetor(-self.direcao.x, -self.direcao.y, -self.direcao.z)
        basePlano_cone = PlanoCircular(self.centro, n_Base,self.raio, self.material)
        self.basePlano = basePlano_cone

    def mundoParaCamera(self, matriz):
        self.v = mult_matriz_ponto(matriz, self.v)
        self.centro = mult_matriz_ponto(matriz, self.centro)
        self.direcao = mult_matriz_vetor(matriz, self.direcao)

        self.reCalculaPlanos()

    def rotacao(self, axis, teta):
        self.v = rotacaoPonto(axis, self.v, teta)
        self.centro = rotacaoPonto(axis, self.centro, teta)
        self.direcao = rotacaoVetor(axis, self.direcao, teta)
        self.reCalculaPlanos()

    def translacao(self, d):
        self.v = translacaoPonto(d, self.v)

        self.centro = translacaoPonto(d, self.centro)
   

        self.reCalculaPlanos()
        
    def escala(self, escala, ancor):
        fator = escala.x
        self.raio = self.raio * fator
        self.altura = self.altura * fator

        self.v = escalaPonto(escala, self.v, ancor)
        self.reCalculaPlanos()

def intersecao(raio, infoIntersecao, centro, direcao, r, altura, v, obj, basePlano):
    
    
    basePlano.intersecao(raio, infoIntersecao, basePlano)
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
    menor_t = raio.t
    if   (t1 >= t2 and t2 > 0):
        menor_t = t2
    elif (t1 < t2 and t1 > 0):
        menor_t = t1
    elif (t1 < 0 and t2 > 0):
        menor_t = t2
    elif (t2 < 0 and t1 > 0):
        menor_t = t1
    else: 
        return
    P        = Calcula_ponto_intersecao(raio.origem, menor_t , raio.direcao)
    projecao = Produto_escalar(Subtracao_vetores( v ,P), direcao) 
                
    if(projecao < 0 or projecao > altura): # P é inválido
        return
        
    raio.t = menor_t
    infoIntersecao.atualizaIntersecao(menor_t, obj)
