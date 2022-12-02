from cena import Cena

from janela import Janela

from esfera import Esfera

from material import Material

from definicoes import Cor, Vetor, Ponto

from luzes import LuzPontual, LuzAmbiente, LuzDirecional

from camera import Camera

# K_d_esfera     = Vetor(0.854, 0.647, 0.125)
# K_a_esfera     = Vetor(0.854, 0.647, 0.125)
# K_e_esfera     = Vetor(0.854, 0.647, 0.125)
# objeto_esfera1 = Esfera(centro_esfera, rEsfera, Cor(255, 0, 0),K_d_esfera, K_d_esfera, K_d_esfera, m_esfera)


def main():

    largura, altura = 500, 500
    dJanela = 30  # distância entre a janela e o olho observador


    centro_esfera =  Ponto(50, 0, 0)
    # rEsfera        = 5
    # m_esfera       = 10
    # centro_esfera  = Ponto(0, 95, -200), -200)
    rEsfera = 40
    K_d_esfera = Vetor(1, 0, 0)
    K_a_esfera = Vetor(1, 0, 0)
    K_e_esfera = Vetor(1, 0, 0)
    m_esfera = 100
    materialEsfera = Material(Cor(255, 0, 0))

    centro_esfera2 =  Ponto(-50, 0, 0)
    esfera = Esfera(centro_esfera, 20, materialEsfera)
    esfera2 = Esfera(centro_esfera2, 20, materialEsfera)
    esfera3 = Esfera(Ponto(0, 0, 50), 20, materialEsfera)
    esfera4 = Esfera(Ponto(0, 0, -50), 20, materialEsfera)
    esfera5 = Esfera(Ponto(0, 0, 0), 20, materialEsfera)


    P_F = Ponto(0, 60, -30)
    intensidade_pf = Vetor(0.7, 0.7, 0.7)
    intensidade_ambiente = Vetor(0.3, 0.3, 0.3)   # Ambiente

    luz_ambiente = LuzAmbiente(intensidade_ambiente, K_a_esfera)
    luz_pontual = LuzPontual(
        P_F, intensidade_pf, K_d_esfera, K_e_esfera, m_esfera)

    direcao_luz_direcional = Ponto(0, 1, 0) 

    intensidade_direcional = Vetor(0.7, 0.7, 0.7)
    luz_direcional = LuzDirecional(
      direcao_luz_direcional, intensidade_direcional, K_d_esfera, K_e_esfera, m_esfera)



    objetos = [ esfera4, esfera5, esfera, esfera2, esfera3]

    #print(objetos[0].material.K_e.x, objetos[0].material.K_e.y)
    luzes = [luz_direcional]


    # posicao_c = Vetor(0, 4, 1) #Vetor(0, -5, 1)
    # at = Vetor(0, 0, -100)
    # up = Vetor(0, 10, -100)

    # posicao_c = Vetor(80, 0, 0) #Vetor(0, -5, 1)
    # at = Vetor(10, 0, 0)
    # up = Vetor(10, 40, 0)

    posicao_c = Vetor(0, 100, 0) 
    at = Vetor(0, 0, 0)
    up = Vetor(80, 0, 0)
    camera1 = Camera(posicao_c, at, up)
    matriz = camera1.matriz()

    for objeto in objetos:
      objeto.mundoParaCamera(matriz)
    for luz in luzes:
      luz.mundoParaCamera(matriz) 
    

    cena = Cena(largura, altura, objetos, luzes)
    janela = Janela(dJanela, largura, altura, cena)

    janela.abrir()
    janela.loopEventos()


main()
