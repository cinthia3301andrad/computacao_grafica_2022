from cena import Cena

from janela import Janela

from cubo import Cubo
from cone import Cone
from esfera import Esfera
from plano import Plano

from cilindro import Cilindro

from planoCircular import PlanoCircular

import math
from material import Material

from definicoes import Cor, Vetor, Ponto

from luzes import LuzPontual, LuzAmbiente, LuzDirecional, LuzSpot

from camera import Camera

from funcoes import Vetor_escalar, Soma_vetores
from PIL import Image


# K_d_esfera     = Vetor(0.854, 0.647, 0.125)
# K_a_esfera     = Vetor(0.854, 0.647, 0.125)
# K_e_esfera     = Vetor(0.854, 0.647, 0.125)
# objeto_esfera1 = Esfera(centro_esfera, rEsfera, Cor(255, 0, 0),K_d_esfera, K_d_esfera, K_d_esfera, m_esfera)


def main():

    largura, altura = 500, 500
    dJanela = 30  # distância entre a janela e o olho observador


    centro_esfera =  Ponto(0, 100, -200)
    # rEsfera        = 5
    # m_esfera       = 10
    # centro_esfera  = Ponto(0, 95, -200), -200)
    rEsfera = 5
    K_d_esfera = Vetor(0.854, 0.647, 0.125)
    K_a_esfera = Vetor(0.854, 0.647, 0.125)
    K_e_esfera = Vetor(0.854, 0.647, 0.125)
    m_esfera = 1
 
    materialEsfera = Material(Cor(255, 0, 0), K_d_esfera, K_a_esfera, K_e_esfera, m_esfera)

    centro_esfera2 =  Ponto(-50, 0, 0)
    esfera = Esfera(centro_esfera, 5, materialEsfera)
    esfera2 = Esfera(centro_esfera2, 20, materialEsfera)
    esfera3 = Esfera(Ponto(0, 0, 50), 20, materialEsfera)
    esfera4 = Esfera(Ponto(0, 0, -50), 20, materialEsfera)
    esfera5 = Esfera(Ponto(0, 0, 0), 20, materialEsfera)

  # Definição do plano do chão
    img_madeira_chao = Image.open("madeira.jpg")
    px_img_madeira_chao = img_madeira_chao.load() 
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
    materialPlanoFundo = Material(Cor(0, 255, 255), K_d_fundo, K_e_fundo, K_a_fundo, m_plano_fundo, px_img_madeira_chao ,  4256, 2832)
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
    n_bar        = Vetor(0, -1, 0) #vetor normal.
    K_d_teto     = Vetor(0.933, 0.933, 0.933)
    K_a_teto  = Vetor(0.933, 0.933, 0.933)
    m_plano_teto = 1     
    K_e_teto=  Vetor(0.933, 0.933, 0.933)
    materialPlanoTeto = Material(Cor(0, 255, 255), K_d_teto, K_e_teto, K_a_teto, m_plano_teto)
    plano_teto   = Plano(P_pi, n_bar ,materialPlanoTeto)

    folhas = Image.open("folha.jpg")
    folhas_load = folhas.load()
    rCone         = 90
    hCone         = 150
    d_cone        = Vetor(0., 1., 0.)
    centro_cone   = Ponto(0, -60, -200)
    K_a_cone      = Vetor(0, 1, 0.498) #Vetor(0.0, 0.0, 0.0)
    K_d_cone      = Vetor(0, 1, 0.498)
    K_e_cone      = Vetor(0, 1, 0.498) #Vetor(0.0, 0.0, 0.0)
    m_cone        = 1
    materialCone = Material(Cor(0, 255, 255), K_d_cone, K_e_cone, K_a_cone, m_cone )
    h_dc = Vetor_escalar(d_cone ,hCone )
    v_cone = Soma_vetores(centro_cone, h_dc)

    n_Base = Vetor(-d_cone.x, -d_cone.y, -d_cone.z)
    basePlano_cone = PlanoCircular(centro_cone, n_Base,rCone, materialCone)

    objeto_cone   = Cone(centro_cone, rCone, hCone, d_cone, v_cone,materialCone, basePlano_cone)


  

        # Definição do cilindro
    rCilindro  = 5
    m_cilindro = 10
    h_cilindro = 90
    centro_cilindro = Ponto(0, -150, -200)
   # d_cil = Vetor(-1/math.sqrt(3), 1/math.sqrt(3), -1/math.sqrt(3))
    d_cil = Vetor(0., 1., 0.)
    K_d_cilindro= Vetor(0.8, 0.0, 0.0)
    K_a_cilindro= Vetor(0.8, 0.0, 0.0)
    K_e_cilindro= Vetor(0.8, 0.0, 0.0)
    materialCilindro= Material(Cor(255, 0, 0), K_d_cilindro, K_e_cilindro, K_a_cilindro, m_esfera)

    n_Base = Vetor(-d_cil.x, -d_cil.y, -d_cil.z)
    basePlano = PlanoCircular(centro_cilindro, n_Base,
                              rCilindro, materialCilindro)

    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(
        d_cil, h_cilindro))
    topoPlano = PlanoCircular(
        centroTopo, d_cil, rCilindro, materialCilindro)

    cilindro = Cilindro(centro_cilindro, 
                          rCilindro, d_cil, h_cilindro, materialCilindro, basePlano,topoPlano)

    posicaoCentro = Ponto(0, 0, -160)
    tam_aresta = 40
    normal_cubo = Vetor(1, 1, 1)
  
    objeto_cubo = Cubo(posicaoCentro, tam_aresta, normal_cubo, materialCilindro )
 
    P_F = Ponto(-50, 30, -30)
    intensidade_pf = Vetor(0.7, 0.7, 0.7)
    intensidade_ambiente = Vetor(0.3, 0.3, 0.3)   # Ambiente

    luz_ambiente = LuzAmbiente(intensidade_ambiente)
    luz_pontual = LuzPontual(
        P_F, intensidade_pf)

    direcao_luz_direcional = Ponto(0, 1, 0) 

    intensidade_direcional = Vetor(0.7, 0.7, 0.7)
    luz_direcional = LuzDirecional(
      direcao_luz_direcional, intensidade_direcional)

    spot_posicao = Ponto(0, 60, -100)
    spot_intensidade = Vetor(0.7, 0.7, 0.7)
    spot_direcao = Ponto(0, -1, -1)
    spot_teta = 0.00001


    luz_spot = LuzSpot(spot_posicao, spot_intensidade, spot_direcao,spot_teta )

    Arvore = [cilindro,objeto_cone, esfera]

    paredes = [plano_chao,plano_fundo, plano_lateral_esq, plano_lateral_dir, plano_teto]


    objetos = [[objeto_cubo]] #[objeto_cubo]
 
    #print(objetos[0].material.K_e.x, objetos[0].material.K_e.y)
    luzes = [luz_ambiente]


    # posicao_c = Vetor(0, 4, 1) #Vetor(0, -5, 1)
    # at = Vetor(0, 0, -100)
    # up = Vetor(0, 10, -100)

    posicao_c = Vetor(0, 10, 0) #Vetor(0, -5, 1)
    at = Vetor(0, 20, -160)
    up = Vetor(0, 40, -160)

   # posicao_c = Vetor(0, 100, 0) 
    #at = Vetor(0, 0, 0)
   # up = Vetor(80, 0, 0)
    camera1 = Camera(posicao_c, at, up)
    matriz = camera1.matriz()

    vetor_translacao = Vetor(20, 0,0)

    axis_z_cone = Vetor(0, 1, 0)
    
    #objeto_cone.translacao(vetor_translacao)
    objeto_cubo.rotacao(axis_z_cone, 0.45) #45 graus em
    #objeto_cone.rotacao(axis_z_cone, 2)


    vetor_escala = Vetor(10, 0, 0)
    vetor_ancora = Vetor(0, 0, 0)

    #objeto_cone.escala(vetor_escala, vetor_ancora)   
   

    for objetoComplexo in objetos:
        for objeto in objetoComplexo:
            objeto.mundoParaCamera(matriz)
    for luz in luzes:
        if(luz.tipo != 'ambiente'):
            luz.mundoParaCamera(matriz) 
    

    cena = Cena(largura, altura, objetos, luzes)
    janela = Janela(dJanela, largura, altura, cena)

    janela.abrir()
    janela.loopEventos()


main()
