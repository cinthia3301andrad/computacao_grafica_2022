from cena import Cena

from janela import Janela

from cone import Cone
from esfera import Esfera
from plano import Plano

from cilindro import Cilindro

import math
from material import Material

from definicoes import Cor, Vetor, Ponto

from luzes import LuzPontual, LuzAmbiente, LuzDirecional

from camera import Camera

from funcoes import Vetor_escalar, Soma_vetores

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

  # Definição do plano do chão
    K_d_chao     = Vetor (0.2, 0.7, 0.2)
    K_a_chao     = Vetor(0.2, 0.7, 0.2)
    K_e_chao     = Vetor(0.0, 0.0, 0.0)
    m_plano = 1
    P_pi         = Ponto(0, -150, 0) #ponto conhecido
    n_bar        = Vetor(0, 1, 0) #vetor normal
    materialChao = Material(Cor(0, 255, 255), K_d_chao, K_e_chao, K_a_chao, m_plano)
    plano_chao   = Plano(P_pi, n_bar, materialChao) #, px_img_madeira_chao)

        # Definição do plano de fundo
    K_d_fundo     = Vetor(0.686, 0.933, 0.933)
    K_a_fundo     =  Vetor(0.686, 0.933, 0.933)
    K_e_fundo     = Vetor(0.686, 0.933, 0.933)
    m_plano_fundo = 1
    materialPlanoFundo = Material(Cor(0, 255, 255), K_d_fundo, K_e_fundo, K_a_fundo, m_plano_fundo)
    P_pi         = Ponto(200, -150, -400) #ponto conhecido
    n_bar        = Vetor(0, 0, 1) #vetor normal
    plano_fundo   = Plano(P_pi, n_bar , materialPlanoFundo) #,px_img_madeira_parede_lateral)

    # Definição do plano de lateral_esq
    P_pi         = Ponto(-200, -150, 0) #ponto conhecido
    n_bar        = Vetor(1, 0, 0) #vetor normal
    K_d_lateral_esq     = Vetor(0.686, 0.933, 0.933)
    K_a_lateral_esq     =  Vetor(0.686, 0.933, 0.933)
    K_e_lateral_esq     = Vetor(0.686, 0.933, 0.933)
    m_plano_lateral_esq = 1
    materialPlanoEsq = Material(Cor(0, 255, 255), K_d_lateral_esq, K_e_lateral_esq, K_a_lateral_esq, m_plano_lateral_esq)
    plano_lateral_esq   = Plano(P_pi, n_bar , materialPlanoEsq)

    # Definição do plano de lateral_dir
    P_pi         = Ponto(200, -150, 0) #ponto conhecido
    n_bar        = Vetor(-1, 0, 0) #vetor normal
    K_d_lateral_dir     = Vetor(0.686, 0.933, 0.933)
    K_a_lateral_dir     =  Vetor(0.686, 0.933, 0.933)
    K_e_lateral_dir     = Vetor(0.686, 0.933, 0.933)
    m_plano_lateral_dir = 1
    materialPlanoDir = Material(Cor(0, 255, 255), K_d_lateral_dir, K_e_lateral_dir, K_a_lateral_dir, m_plano_lateral_dir)
    plano_lateral_dir   = Plano(P_pi, n_bar ,materialPlanoDir)

        # Definição do plano de teto
    P_pi         = Ponto(0, 150, 0) #ponto conhecido
    n_bar        = Vetor(0, -1, 0) #vetor normal
    K_d_teto     = Vetor(0.933, 0.933, 0.933)
    K_a_teto  = Vetor(0.933, 0.933, 0.933)
    m_plano_teto = 1     
    K_e_teto=  Vetor(0.933, 0.933, 0.933)
    materialPlanoTeto = Material(Cor(0, 255, 255), K_d_teto, K_e_teto, K_a_teto, m_plano_teto)
    plano_teto   = Plano(P_pi, n_bar ,materialPlanoTeto)


   
    rCone         = 90
    hCone         = 150
    d_cone        = Vetor(0, 1 , 0)
    centro_cone   = Ponto(0, -60, -200)
    K_a_cone      = Vetor(0, 1, 0.498) #Vetor(0.0, 0.0, 0.0)
    K_d_cone      = Vetor(0, 1, 0.498)
    K_e_cone      = Vetor(0, 1, 0.498) #Vetor(0.0, 0.0, 0.0)
    m_cone        = 100
    materialCone = Material(Cor(0, 255, 255), K_d_cone, K_e_cone, K_a_cone, m_cone )
    h_dc = Vetor_escalar(d_cone ,hCone )
    v_cone = Soma_vetores(centro_cone, h_dc)
    objeto_cone   = Cone(centro_cone, rCone, hCone, d_cone, v_cone,materialCone)


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
    centro_cilindro = Ponto(-100, 0, -400)
   # d_cil = Vetor(-1/math.sqrt(3), 1/math.sqrt(3), -1/math.sqrt(3))
    d_cil = Vetor(0, 1,  0)
    K_d_cilindro= Vetor(0.824, 0.706, 0.549)
    K_a_cilindro= Vetor(0.824, 0.706, 0.549)
    K_e_cilindro= Vetor(0.824, 0.706, 0.549)
    cilindro = Cilindro(centro_cilindro, 
                          rCilindro, d_cil, h_cilindro, materialEsfera)



    objetos = [cilindro, plano_chao , plano_fundo, plano_lateral_esq, plano_lateral_dir, plano_teto]

    #print(objetos[0].material.K_e.x, objetos[0].material.K_e.y)
    luzes = [luz_ambiente, luz_pontual]


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
