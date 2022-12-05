import numpy as np
import math
from definicoes import Cor, Vetor, Ponto
from funcoes import Produto_arroba, Vetor_escalar, Calc_L, Subtracao_vetores, Produto_escalar, normalizaVetor, Calcula_vetor_refletido, mult_matriz_vetor


class Luz:
    def __init__(self, posicao, intensidade):
        self.posicao = posicao
        self.intensidade = intensidade
        

    def computaLuz(self, ponto, normal, raio, shininess: float):
        return 0

    def getDirecao(self, ponto):
        direcao = self.posicao - ponto
        distance = np.linalg.norm(direcao)
        return direcao / distance, distance

    @property
    def ignoreShadow(self):
        return False


class LuzPontual(Luz):
    def __init__(self, posicao, intensidade):
        self.posicao = posicao
        self.intensidade = intensidade
 
    def computaLuz(self, normal, ponto, objeto_atual, raio):
    # incicialização das contribuições ambiente, difusa e especular
        intensidade_d = 0.0 #difusa
        intensidade_e = 0.0 #especular
        L = normalizaVetor(Calc_L(self.posicao, ponto))
        normal = normalizaVetor(normal)

        r_vetor_refletido = normalizaVetor(Calcula_vetor_refletido(L, normal))
        v_vetor = normalizaVetor(Subtracao_vetores(raio.origem, ponto))
     
        # Cálculo do fator de atenuação da reflexão difusa
        fd = max(0, Produto_escalar(L, normal))

        # Cálculo do fator de atenuação da reflexão especular
        m = objeto_atual.material.m
        fe = pow(max(0, Produto_escalar(r_vetor_refletido, v_vetor)), m)
        I_F = self.intensidade  # Pontual
        # Cálculo das contribuições de energia resultantes das reflexões Ambiente, Difusa e Especular
        intensidade_d = Vetor_escalar(Produto_arroba(
            I_F, objeto_atual.material.k_difusa), fd)  # Reflexão difusa
        intensidade_e = Vetor_escalar(Produto_arroba(
            I_F, objeto_atual.material.k_especular), fe)  # Reflexão especular

        intensidade_x = (intensidade_e.x + intensidade_d.x)
        intensidade_y = (intensidade_e.y + intensidade_d.y)
        intensidade_z =   (intensidade_e.z + intensidade_d.z)
    
        return Cor(intensidade_x, intensidade_y, intensidade_z)

class LuzAmbiente(Luz):
    def __init__(self, intensidade):

   
        self.intensidade = intensidade

    def computaLuz(self, normal, ponto, objeto_atual, raio):
        I_A = self.intensidade
        K_a = objeto_atual.material.k_ambiente
        intensidade_a = Produto_arroba(I_A, K_a)
       
        return Cor(intensidade_a.x,
                   intensidade_a.y,
                   intensidade_a.z)

    def ignoreShadow(self):
        return True

class LuzDirecional(Luz):
    def __init__(self,  direcao, intensidade):

        self.intensidade = intensidade
    
        self.direcao = direcao
       

    def computaLuz(self, normal, ponto, objeto_atual, raio):
        intensidade_d = 0.0 #difusa
        intensidade_e = 0.0 #especular
        L = normalizaVetor(self.direcao)
        normal = normalizaVetor(normal)

        r_vetor_refletido = normalizaVetor(Calcula_vetor_refletido(L, normal))
        v_vetor = normalizaVetor(Subtracao_vetores(raio.origem, ponto))
     
        # Cálculo do fator de atenuação da reflexão difusa
        fd = max(0, Produto_escalar(L, normal))

        # Cálculo do fator de atenuação da reflexão especular
        m = objeto_atual.material.m
        fe = pow(max(0, Produto_escalar(r_vetor_refletido, v_vetor)), m)
        I_F = self.intensidade  # Pontual
        # Cálculo das contribuições de energia resultantes das reflexões Ambiente, Difusa e Especular
        intensidade_d = Vetor_escalar(Produto_arroba(
            I_F, objeto_atual.material.k_difusa), fd)  # Reflexão difusa
        intensidade_e = Vetor_escalar(Produto_arroba(
            I_F, objeto_atual.material.k_especular), fe)  # Reflexão especular

        intensidade_x = (intensidade_e.x + intensidade_d.x)
        intensidade_y = (intensidade_e.y + intensidade_d.y)
        intensidade_z =   (intensidade_e.z + intensidade_d.z)
    
        return Cor(intensidade_x, intensidade_y, intensidade_z)
    
    def mundoParaCamera(self, matriz):
        self.direcao = mult_matriz_vetor(matriz, self.direcao)

    def ignoreShadow(self):
        return True
