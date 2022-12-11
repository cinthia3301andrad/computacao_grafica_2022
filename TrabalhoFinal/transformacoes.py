from funcoes import mult_matriz_ponto, mult_matriz_vetor
import math

def matrizIdentidade():
    M = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

    return M

def montaMatrizRotacao(v, t):
    resultado = matrizIdentidade()

    if(v.x==1):
        resultado[1][1] = math.cos(t)
        resultado[2][2] = math.cos(t)
        resultado[1][2] = -math.sin(t)
        resultado[2][1] = math.sin(t)
    if(v.y==1):
        resultado[0][0] = math.cos(t)
        resultado[2][2] = math.cos(t)
        resultado[0][2] = math.sin(t)
        resultado[2][0] = -math.sin(t)

    if(v.z==1):
        resultado[0][0] = math.cos(t)
        resultado[1][1] = math.cos(t)
        resultado[0][1] = -math.sin(t)
        resultado[1][0] = math.sin(t)
      
    return resultado


def translacaoMatriz(v):

    resultado = matrizIdentidade()
    resultado[0][3] = v.x
    resultado[1][3] = v.y
    resultado[2][3] = v.z

    return resultado 

def rotacaoPonto(v, p, teta):
    matriz_rotacao = montaMatrizRotacao(v, teta)

    return mult_matriz_ponto(matriz_rotacao, p)

def rotacaoVetor(v, u, teta):
    matriz_rotacao = montaMatrizRotacao(v, teta)

    return mult_matriz_vetor(matriz_rotacao, u)


def translacaoPonto(v, p):
    matriz_translacao = translacaoMatriz(v)

    return mult_matriz_ponto(matriz_translacao, p)


def escalaMatriz(v, p):
    resultado = matrizIdentidade()
    resultado[0][0] = v.x
    resultado[1][1] = v.y
    resultado[2][2] = v.z
    resultado[3][3] = 1 
    resultado[0][3] = (1-v.x) * p.x
    resultado[1][3] = (1-v.y) * p.y
    resultado[2][3] = (1-v.z) * p.z

    return resultado 
def escalaPonto(escala, posicaoCentro, ancor):
    matriz_escala = escalaMatriz(escala, posicaoCentro)

    return mult_matriz_ponto(matriz_escala, ancor)