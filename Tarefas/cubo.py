
from malha import Malha
from calc_vetores import *
tipo = 'cubo'

def Cubo(centro, K_e,K_d,K_a, m, tam_aresta):

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
    return {
        'tipo': tipo ,
        'centro': centro, 
        'K_e': K_e,
        'K_d': K_d,
        'K_a': K_a,
        'm': m,
        'normal': Vetor(0, 0, 0),
        'malha': Malha( K_e,K_d,K_a, m, faces),
        
    }

