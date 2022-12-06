
from malha import Malha
from raio import Raio
from objetos.objeto import Objeto
from funcoes import normalizaVetor, Vetor, Face

class Cubo(Objeto):
    def __init__(self, posicaoCentro, tam_aresta, normal, material ):
        self.posicaoCentro = posicaoCentro
        self.tam_aresta = tam_aresta
        self.material = material
        self.normal = normal

    def MontandoCubo(self):
        return MontandoCubo(self.posicaoCentro, self.tam_aresta)
         
    def getNormal(self, _): #calcula e retorna a normal do ponto da superficie esfera
    #return Subtracao_vetores(ponto , self.posicaoCentro) / self.raioEsfera
        return normalizaVetor(self.normal)

    def getColor(self):
        return self.material.cor

def MontandoCubo(centro, tam_aresta):

    vertices = [
        Vetor(centro['x']- tam_aresta/2, centro['y']- tam_aresta/2, centro['z'] + tam_aresta/2),
        Vetor(centro['x']+ tam_aresta/2, centro['y']- tam_aresta/2, centro['z'] + tam_aresta/2),
        Vetor(centro['x']+ tam_aresta/2, centro['y']+ tam_aresta/2, centro['z'] + tam_aresta/2),
        Vetor(centro['x']- tam_aresta/2, centro['y']+ tam_aresta/2, centro['z'] + tam_aresta/2),
        Vetor(centro['x']- tam_aresta/2, centro['y']+ tam_aresta/2, centro['z'] - tam_aresta/2),
        Vetor(centro['x']- tam_aresta/2, centro['y']- tam_aresta/2, centro['z'] - tam_aresta/2),
        Vetor(centro['x']+ tam_aresta/2, centro['y']- tam_aresta/2, centro['z'] - tam_aresta/2),
        Vetor(centro['x']+ tam_aresta/2, centro['y']+ tam_aresta/2, centro['z'] - tam_aresta/2),
    ]

    faces = [
        Face(vertices[0], vertices[1], vertices[3]),
        Face(vertices[1], vertices[2], vertices[3]),
        Face(vertices[1], vertices[6], vertices[2]),
        Face(vertices[2], vertices[6], vertices[7]),
        Face(vertices[5], vertices[7], vertices[6]),
        Face(vertices[5], vertices[4], vertices[7]),
        Face(vertices[0], vertices[4], vertices[5]),
        Face(vertices[3], vertices[4], vertices[0]),
        Face(vertices[4], vertices[2], vertices[7]),
        Face(vertices[4], vertices[3], vertices[2]),
        Face(vertices[0], vertices[5], vertices[1]),
        Face(vertices[1], vertices[5], vertices[6]),
        
    ]

    # return {
    #     'tipo': tipo ,
    #     'centro': centro, 
    #     'K_e': K_e,
    #     'K_d': K_d,
    #     'K_a': K_a,
    #     'm': m,
    #     'normal': Vetor(0, 0, 0),
    #     'malha': Malha( K_e,K_d,K_a, m, faces),