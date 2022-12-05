from cena import Cena

from janela import Janela

from esfera import Esfera
from plano import Plano

from cilindro import Cilindro

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
    K_d_esfera = Vetor(1, 0.3, 0.1)
    K_a_esfera = Vetor(1, 0.3, 0.1)
    K_e_esfera = Vetor(1, 0.3, 0.1)
    m_esfera = 100
 
    materialEsfera = Material(Cor(255, 0, 0), K_d_esfera, K_a_esfera, K_e_esfera, m_esfera)

    centro_esfera2 =  Ponto(-50, 0, 0)
    esfera = Esfera(centro_esfera, 20, materialEsfera)
    esfera2 = Esfera(centro_esfera2, 20, materialEsfera)
    esfera3 = Esfera(Ponto(0, 0, 50), 20, materialEsfera)
    esfera4 = Esfera(Ponto(0, 0, -50), 20, materialEsfera)
    esfera5 = Esfera(Ponto(0, 0, 0), 20, materialEsfera)


    K_d_plano = Vetor(0.7, 1, 0)
    K_a_plano = Vetor(0.7, 1, 0)
    K_e_plano = Vetor(0.7, 1, 0)
    m_plano = 100
      # Definição do plano do chão
    P_pi         = Ponto(0, -150, 0) #ponto conhecido
    n_bar        = Vetor(0, 1, 0) #vetor normal
    materialPlano = Material(Cor(0, 255, 255), K_d_plano, K_a_plano, K_e_plano, m_plano)
    plano_chao   = Plano(P_pi, n_bar, materialPlano) #, px_img_madeira_chao)

        # Definição do plano de fundo
    P_pi         = Ponto(200, -150, -400) #ponto conhecido
    n_bar        = Vetor(0, 0, 1) #vetor normal
    plano_fundo   = Plano(P_pi, n_bar , materialPlano) #,px_img_madeira_parede_lateral)

    # Definição do plano de lateral_esq
    P_pi         = Ponto(-200, -150, 0) #ponto conhecido
    n_bar        = Vetor(1, 0, 0) #vetor normal
    plano_lateral_esq   = Plano(P_pi, n_bar , materialPlano)

    # Definição do plano de lateral_dir
    P_pi         = Ponto(200, -150, 0) #ponto conhecido
    n_bar        = Vetor(-1, 0, 0) #vetor normal
    plano_lateral_dir   = Plano(P_pi, n_bar ,materialPlano)

    P_F = Ponto(0, 60, -30)
    intensidade_pf = Vetor(0.7, 0.7, 0.7)
    intensidade_ambiente = Vetor(0.3, 0.3, 0.3)   # Ambiente

    luz_ambiente = LuzAmbiente(intensidade_ambiente)
    luz_pontual = LuzPontual(
        P_F, intensidade_pf)

    direcao_luz_direcional = Ponto(0, 1, 0) 

    intensidade_direcional = Vetor(0.7, 0.7, 0.7)
    luz_direcional = LuzDirecional(
      direcao_luz_direcional, intensidade_direcional)


    # Definição do cilindro
    rCilindro  = 40
    m_cilindro = 10
    h_cilindro = 50
    centro_cilindro = Ponto(100, -30, -200)
    #d_cil = Vetor(-1/math.sqrt(3), 1/math.sqrt(3), -1/math.sqrt(3))
    d_cil = Vetor(0, 1, 0)
    K_d_cilindro= Vetor(0.824, 0.706, 0.549)
    K_a_cilindro= Vetor(0.824, 0.706, 0.549)
    K_e_cilindro= Vetor(0.824, 0.706, 0.549)
    cilindro = Cilindro(centro_cilindro, 
                          rCilindro, d_cil, h_cilindro, materialEsfera)



    objetos = [ cilindro]

    #print(objetos[0].material.K_e.x, objetos[0].material.K_e.y)
    luzes = [luz_ambiente]


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

    #for objeto in objetos:
   #   objeto.mundoParaCamera(matriz)
   # for luz in luzes:
    #  luz.mundoParaCamera(matriz) 
    

    cena = Cena(largura, altura, objetos, luzes)
    janela = Janela(dJanela, largura, altura, cena)

    janela.abrir()
    janela.loopEventos()


main()
