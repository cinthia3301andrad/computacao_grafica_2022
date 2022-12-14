
from raio import Raio
from objetos.objeto import Objeto
from funcoes import Subtracao_vetores, produto_vetorial, normalizaVetor, Vetor, Produto_escalar,Soma_vetores,Vetor_escalar
from raio import Raio
from planoFace import PlanoFace
import math

from transformacoes import rotacaoPonto, escalaPonto, translacaoPonto, cisalhamentoPonto

from intercesaoInfo import IntercesaoInfo

from face import Face
class Cubo(Objeto):
    
    def __init__(self, posicaoCentro, tam_aresta, normal, material, tipo= None ):
        
        self.posicaoCentro = posicaoCentro
        self.tam_aresta = tam_aresta
        self.normal = normal
        self.material = material
        self.tipo =tipo

        self.vertices = [
        Vetor(posicaoCentro.x- tam_aresta/2, posicaoCentro.y- tam_aresta/2, posicaoCentro.z + tam_aresta/2),
        Vetor(posicaoCentro.x+ tam_aresta/2, posicaoCentro.y- tam_aresta/2, posicaoCentro.z + tam_aresta/2),
        Vetor(posicaoCentro.x+ tam_aresta/2, posicaoCentro.y+ tam_aresta/2, posicaoCentro.z + tam_aresta/2),
        Vetor(posicaoCentro.x- tam_aresta/2, posicaoCentro.y+ tam_aresta/2, posicaoCentro.z + tam_aresta/2),
        Vetor(posicaoCentro.x- tam_aresta/2, posicaoCentro.y+ tam_aresta/2, posicaoCentro.z - tam_aresta/2),
        Vetor(posicaoCentro.x- tam_aresta/2, posicaoCentro.y- tam_aresta/2, posicaoCentro.z - tam_aresta/2),
        Vetor(posicaoCentro.x+ tam_aresta/2, posicaoCentro.y- tam_aresta/2, posicaoCentro.z - tam_aresta/2),
        Vetor(posicaoCentro.x+ tam_aresta/2, posicaoCentro.y+ tam_aresta/2, posicaoCentro.z - tam_aresta/2),
    ]
        
        self.faces = [
        Face(self.vertices[0], self.vertices[1], self.vertices[3]),
        Face(self.vertices[1], self.vertices[2], self.vertices[3]),
        Face(self.vertices[1], self.vertices[6], self.vertices[2]),
        Face(self.vertices[2], self.vertices[6], self.vertices[7]),
        Face(self.vertices[5], self.vertices[7], self.vertices[6]),
        Face(self.vertices[5], self.vertices[4], self.vertices[7]),
        Face(self.vertices[0], self.vertices[4], self.vertices[5]),
        Face(self.vertices[3], self.vertices[4], self.vertices[0]),
        Face(self.vertices[4], self.vertices[2], self.vertices[7]),
        Face(self.vertices[4], self.vertices[3], self.vertices[2]),
        Face(self.vertices[0], self.vertices[5], self.vertices[1]),
        Face(self.vertices[1], self.vertices[5], self.vertices[6]),
        
    ]

    def intersecao(self, raio: Raio, infoIntersecao, obj):
        return intersecao(self, raio, infoIntersecao, self.posicaoCentro,
         self.tam_aresta, self.normal,self.faces, obj)
         
    def getNormal(self, _): #calcula e retorna a normal do ponto da superficie esfera
    #return Subtracao_vetores(ponto , self.posicaoCentro) / self.raioEsfera
        return normalizaVetor(self.normal)

    def getColor(self):
        return self.material.cor

    def mundoParaCamera(self, matriz):
        for face in self.faces:
            face.mundoParaCamera(matriz)
    
    def translacao(self, d):
        for face in self.faces:
         #   print("face", face)
            face.p1 = translacaoPonto(d, face.p1)
            face.p2 =  translacaoPonto(d, face.p2)
            face.p3 = translacaoPonto(d, face.p3)

    def rotacao(self, axis, teta):
        for face in self.faces:
         #   print("face", face)
            face.p1 = rotacaoPonto(axis, face.p1, teta)
            face.p2 = rotacaoPonto(axis, face.p2, teta)
            face.p3 = rotacaoPonto(axis, face.p3, teta)
    def escala(self, escala):
        ancor = self.faces[0].p1
        for face in self.faces:
         #   print("face", face)
            face.p1 =  escalaPonto(escala, face.p1, ancor)
            face.p2 =  escalaPonto(escala, face.p2, ancor)
            face.p3 =  escalaPonto(escala, face.p3, ancor)

    def cisalhamento(self, plane, d, t):
        for face in self.faces:
         #   print("face", face)
            face.p1 =  cisalhamentoPonto(plane, d, face.p1, t)
            face.p2 =  cisalhamentoPonto(plane, d, face.p2, t)
            face.p3 =  cisalhamentoPonto(plane, d, face.p3, t)


def intersecao(self, raio, infoIntersecao, posicaoCentro, tam_aresta, normal, faces, obj):

   # [t, nova_normal] = IntersecaoTodasFaces(faces, raio, obj)
    #print("ATUALIZOU?", nova_normal.x, nova_normal.y, nova_normal.z)
   # self.normal = nova_normal

   # infoIntersecao.atualizaIntersecao(t, obj)
   for face in self.faces:
        face.intersecao(raio, infoIntersecao, obj)
        




def verifica_face(p_i, face):
    
    area_total = Produto_escalar(produto_vetorial(Subtracao_vetores(face.p2, face.p1), 
                                Subtracao_vetores(face.p3, face.p1)), face.normal)
   

 
    c1 = Produto_escalar(produto_vetorial(Subtracao_vetores(face.p1, p_i), Subtracao_vetores(face.p2, p_i)), face.normal) / area_total
    c2 = Produto_escalar(produto_vetorial(Subtracao_vetores(face.p3, p_i), Subtracao_vetores(face.p1, p_i)), face.normal) / area_total
   
  #  c3 =  Produto_escalar(produto_vetorial(Subtracao_vetores(face.p2, p_i), Subtracao_vetores(face.p3, p_i)), face.normal) / area_total
    c3 = 1 - c1 - c2

    return c1 > 0.0-0.0000001 and c2 > 0.0-0.0000001 and c3 > 0.0-0.0000001


def IntersecaoFace(face, raio, obj):
    plano = PlanoFace(face.p1, face.normal, obj.material) 
    
   # raiocopy = Raio(raio.origem, raio.direcao)

    t1 =  plano.intersecao(raio)
    p_i = Soma_vetores(raio.origem, Vetor_escalar(raio.direcao, t1))
    
    
    if(verifica_face(p_i, face)):
    
        return t1
    return math.inf

def IntersecaoTodasFaces(faces, raio, obj):
    t = math.inf
    t_aux = 0
    normal_aux = Vetor(0, 0, 0)
    #infoIntersecao = IntercesaoInfo(raio)
  #  raioS = Raio(raio.origem, raio.direcao)
    
    for face in faces:
     
        if(Produto_escalar(face.normal, raio.direcao) < 0.0):
            t_aux = IntersecaoFace(face, raio, obj)
            if(t_aux < t):
                t = t_aux
                normal_aux = face.normal
                
  
    return [t, normal_aux]

