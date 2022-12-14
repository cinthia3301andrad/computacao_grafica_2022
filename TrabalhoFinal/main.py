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
    dJanela = 12  # distância entre a janela e o olho observador


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
    img_madeira_chao = Image.open("ceu.jpg")
    px_img_madeira_chao = img_madeira_chao.load() 
    K_d_chao     = Vetor (0.2, 0.7, 0.2)
    K_a_chao     = Vetor(0.2, 0.7, 0.2)
    K_e_chao     = Vetor(0.0, 0.0, 0.0)
    m_plano = 1
    P_pi         = Ponto(0, -150, 0) #ponto conhecido
    n_bar        = Vetor(0, 1, 0) #vetor normal
    materialChao = Material(Cor(0, 255, 255), K_d_chao, K_e_chao, K_a_chao, m_plano)
    tipo = "plano"
    plano_chao   = Plano(P_pi, n_bar, materialChao, tipo) #, px_img_madeira_chao)

        # Definição do plano de fundo
    K_d_fundo     = Vetor(0.686, 0.933, 0.933)
    K_a_fundo     =  Vetor(0.686, 0.933, 0.933)
    K_e_fundo     = Vetor(0.686, 0.933, 0.933)
    m_plano_fundo = 1
    materialPlanoFundo = Material(Cor(0, 255, 255), K_d_fundo, K_e_fundo, K_a_fundo, m_plano_fundo, px_img_madeira_chao , 612, 408 ) #noite = 960, 686
    P_pi         = Ponto(200, -150, -1500) #ponto conhecido
    n_bar        = Vetor(0, 0, 1) #vetor normal
    tipo = "ceu"
    plano_fundo   = Plano(P_pi, n_bar , materialPlanoFundo,tipo ) #,px_img_madeira_parede_lateral)

    # Definição do plano de lateral_esq
    # P_pi         = Ponto(-200, -150, 0) #ponto conhecido
    # n_bar        = Vetor(1, 0, 0) #vetor normal
    # K_d_lateral_esq     = Vetor(0.686, 0.933, 0.933)
    # K_a_lateral_esq     =  Vetor(0.686, 0.933, 0.933)
    # K_e_lateral_esq     = Vetor(0.686, 0.933, 0.933)
    # m_plano_lateral_esq = 1
    # materialPlanoEsq = Material(Cor(0, 255, 255), K_d_lateral_esq, K_e_lateral_esq, K_a_lateral_esq, m_plano_lateral_esq)
    # plano_lateral_esq   = Plano(P_pi, n_bar , materialPlanoEsq)

    # # Definição do plano de lateral_dir
    # P_pi         = Ponto(200, -150, 0) #ponto conhecido
    # n_bar        = Vetor(-1, 0, 0) #vetor normal
    # K_d_lateral_dir     = Vetor(0.686, 0.933, 0.933)
    # K_a_lateral_dir     =  Vetor(0.686, 0.933, 0.933)
    # K_e_lateral_dir     = Vetor(0.686, 0.933, 0.933)
    # m_plano_lateral_dir = 1
    # materialPlanoDir = Material(Cor(0, 255, 255), K_d_lateral_dir, K_e_lateral_dir, K_a_lateral_dir, m_plano_lateral_dir)
    # plano_lateral_dir   = Plano(P_pi, n_bar ,materialPlanoDir)

    # # Definição do plano de teto
    # P_pi         = Ponto(0, 150, 0) #ponto conhecido
    # n_bar        = Vetor(0, -1, 0) #vetor normal.
    # K_d_teto     = Vetor(0.933, 0.933, 0.933)
    # K_a_teto  = Vetor(0.933, 0.933, 0.933)
    # m_plano_teto = 1     
    # K_e_teto=  Vetor(0.933, 0.933, 0.933)
    # materialPlanoTeto = Material(Cor(0, 255, 255), K_d_teto, K_e_teto, K_a_teto, m_plano_teto)
    # plano_teto   = Plano(P_pi, n_bar ,materialPlanoTeto)

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

    


    #CERCADO
    rCilindro  = 8
    m_cilindro = 10
    h_cilindro = 400 
    centro_cilindro = Ponto(-500, -110, -200) #Ponto(0, -60, -200) -150
    d_cil = Vetor(1, 0, 0)
    K_d_cilindro= Vetor(0.58, 0.29, 0)
    K_a_cilindro= Vetor(0.58,  0.29, 0)
    K_e_cilindro= Vetor(0.58,0.29, 0)
    material_cilindro = Material(Cor(255, 0, 0),K_e_cilindro, K_d_cilindro, K_a_cilindro, m_cilindro)

    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    cilindro_cercado = Cilindro(centro_cilindro,rCilindro, d_cil, h_cilindro,material_cilindro,baseC, topoPlano )
    
    centro_cilindro = Ponto(-500, -60, -200)
    d_cil = Vetor(1, 0, 0)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_cercado3 = Cilindro(centro_cilindro, 
                        rCilindro,d_cil, h_cilindro, material_cilindro , topoPlano, baseC)
    
    centro_cilindro = Ponto(100, -60, -200)
    d_cil = Vetor(1, 0, 0)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_cercado13 = Cilindro(centro_cilindro, 
                        rCilindro,d_cil, h_cilindro, material_cilindro , topoPlano, baseC)
    
    centro_cilindro = Ponto(100, -110, -200)
    d_cil = Vetor(1, 0, 0)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_cercado14 = Cilindro(centro_cilindro, 
                        rCilindro,d_cil, h_cilindro, material_cilindro , topoPlano, baseC)
    
    h_cilindro = 100 
    centro_cilindro = Ponto(100, -150, -200)
    d_cil = Vetor(0, 1, 0)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_cercado15 = Cilindro(centro_cilindro, 
                        rCilindro,d_cil, h_cilindro, material_cilindro , topoPlano, baseC)
    
    h_cilindro = 100
    centro_cilindro = Ponto(-100, -150, -200)
    d_cil = Vetor(0, 1, 0)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_cercado16 = Cilindro(centro_cilindro, rCilindro,d_cil, h_cilindro, material_cilindro , topoPlano, baseC)


    h_cilindro = 100 
    centro_cilindro = Ponto(-500, -150, -200) #Ponto(0, -60, -200) -150
    d_cil = Vetor(0, 1, 0)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_cercado2 = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    h_cilindro = 100 
    centro_cilindro = Ponto(500, -150, -200) #Ponto(0, -60, -200) -150
    d_cil = Vetor(0, 1, 0)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_cercado4 = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    h_cilindro = 100 
    centro_cilindro = Ponto(500, -150, -700) #Ponto(0, -60, -200) -150
    d_cil = Vetor(0, 1, 0)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_cercado5 = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    h_cilindro = 100 
    centro_cilindro = Ponto(-500, -150, -700) #Ponto(0, -60, -200) -150
    d_cil = Vetor(0, 1, 0)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_cercado6 = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)
    
    h_cilindro = 1000 
    centro_cilindro = Ponto(-500, -60, -700) #Ponto(0, -60, -200) -150
    d_cil = Vetor(1, 0, 0)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_cercado7 = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    h_cilindro = 1000 
    centro_cilindro = Ponto(-500, -110, -700) #Ponto(0, -60, -200) -150
    d_cil = Vetor(1, 0, 0)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_cercado8 = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    h_cilindro = 500 
    centro_cilindro = Ponto(-500, -60, -700) #Ponto(0, -60, -200) -150
    d_cil = Vetor(0, 0, 1)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_cercado9 = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    centro_cilindro = Ponto(-500, -110, -700) #Ponto(0, -60, -200) -150
    d_cil = Vetor(0, 0, 1)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_cercado10 = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    centro_cilindro = Ponto(500, -60, -700) #Ponto(0, -60, -200) -150
    d_cil = Vetor(0, 0, 1)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_cercado11 = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    centro_cilindro = Ponto(500, -110, -700) #Ponto(0, -60, -200) -150
    d_cil = Vetor(0, 0, 1)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_cercado12 = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    centro_cone   = Ponto(-350, 150, -600)
    rCone         = 100
    hCone         = 100
    d_cone        = Vetor(0, 1 , 0)
    K_a_cone      = Vetor(0.89, 0.89, 0.89) #Vetor(0.0, 0.0, 0.0)
    K_d_cone      = Vetor(0.89, 0.89, 0.89)
    K_e_cone      = Vetor(0.89, 0.89, 0.89) #Vetor(0.0, 0.0, 0.0)
    m_cone        = 10
    material_silo = Material(Cor(255, 0, 0), K_e_cone, K_d_cone, K_a_cone, m_cone)
    h_dc = Vetor_escalar(d_cone ,hCone )
    v_cone = Soma_vetores(centro_cone, h_dc)

    n_Base = d_cone
    basePlano_cone = PlanoCircular(centro_cone, n_Base,rCone, materialCone)
    cone_silo   = Cone(centro_cone,rCone, hCone, d_cone, v_cone,material_silo, basePlano_cone)

    rCilindro  = 100
    m_cilindro = 10
    h_cilindro = 300 
    centro_cilindro = Ponto(-350, -150, -600) #Ponto(0, -60, -200) -150
    d_cil = Vetor(0, 1, 0)
    K_d_cilindro= Vetor(0.824, 0.706, 0.549)
    K_a_cilindro= Vetor(0.824, 0.706, 0.549)
    K_e_cilindro= Vetor(0.824, 0.706, 0.549)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_silo)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_silo)
    cilindro_celeiro = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_silo, topoPlano, baseC)

    centro_cone   = Ponto(-350, 200, -300)
    rCone         = 70
    hCone         = 30
    d_cone        = Vetor(0, 1 , 0)
    K_a_cone      = Vetor(0.117, 0.564, 1) #Vetor(0.0, 0.0, 0.0)
    K_d_cone      = Vetor(0.117, 0.564, 1)
    K_e_cone      = Vetor(0.117, 0.564, 1) #Vetor(0.0, 0.0, 0.0)
    m_cone        = 10
    material_cone = Material(Cor(255, 0, 0), K_e_cone, K_d_cone, K_a_cone, m_cone)
    h_dc = Vetor_escalar(d_cone ,hCone )
    v_cone = Soma_vetores(centro_cone, h_dc)
    n_Base = d_cone
    basePlano_cone = PlanoCircular(centro_cone, n_Base,rCone, materialCone)
    cone_caixadagua   = Cone(centro_cone,rCone, hCone, d_cone, v_cone,material_cone, basePlano_cone)

    rCilindro  = 70
    m_cilindro = 10
    h_cilindro = 200 
    centro_cilindro = Ponto(-350, 0, -300) #Ponto(0, -60, -200) -150
    d_cil = Vetor(0, 1, 0)
    K_d_cilindro= Vetor(0.117, 0.564, 1)
    K_a_cilindro= Vetor(0.117, 0.564, 1)
    K_e_cilindro= Vetor(0.117, 0.564, 1)
    material_cilindro = Material(Cor(255, 0, 0),K_e_cilindro, K_d_cilindro, K_a_cilindro, m_cilindro)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_caixadagua = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    rCilindro  = 10
    m_cilindro = 10
    h_cilindro = 150 
    centro_cilindro = Ponto(-350, -150, -350) #Ponto(0, -60, -200) -150
    d_cil = Vetor(0, 1, 0)
    K_d_cilindro= Vetor(1, 0.980, 0.980)
    K_a_cilindro= Vetor(1, 0.980,0.980)
    K_e_cilindro= Vetor(1, 0.980,0.980)
    material_cilindro = Material(Cor(255, 0, 0),K_e_cilindro, K_d_cilindro, K_a_cilindro, m_cilindro)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_apoio1 = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    centro_cilindro = Ponto(-350, -150, -250) #Ponto(0, -60, -200) -150
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_apoio2 = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    centro_cilindro = Ponto(-400, -150, -300) #Ponto(0, -60, -200) -150
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_apoio3 = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    centro_cilindro = Ponto(-300, -150, -300) #Ponto(0, -60, -200) -150
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_apoio4 = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    #ARVORE
    centro_cone   = Ponto(350, -60, -300) # 350, 150, 
    rCone         = 90
    hCone         = 150
    d_cone        = Vetor(0, 1 , 0)
    K_a_cone      = Vetor(0, 1, 0.498) #Vetor(0.0, 0.0, 0.0)
    K_d_cone      = Vetor(0, 1, 0.498)
    K_e_cone      = Vetor(0, 1, 0.498) #Vetor(0.0, 0.0, 0.0)
    m_cone        = 100
    material_cone = Material(Cor(255, 0, 0), K_e_cone, K_d_cone, K_a_cone, m_cone)
    h_dc = Vetor_escalar(d_cone ,hCone )
    v_cone = Soma_vetores(centro_cone, h_dc)
    n_Base = d_cone
    basePlano_cone = PlanoCircular(centro_cone, n_Base,rCone, materialCone)
    cone_arvore  = Cone(centro_cone,rCone, hCone, d_cone, v_cone,material_cone, basePlano_cone)

    rCilindro  = 10
    h_cilindro = 90
    centro_cilindro = Ponto(350, -150, -300)
    d_cil = Vetor(0, 1, 0)
    K_d_cilindro= Vetor(0.58, 0.29, 0)
    K_a_cilindro= Vetor(0.58,  0.29, 0)
    K_e_cilindro= Vetor(0.58,0.29, 0)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    material_cilindro = Material(Cor(255, 0, 0),K_e_cilindro, K_d_cilindro, K_a_cilindro, m_cilindro)
    cilindro_arvore = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    #POSTE
    rCilindro  = 8
    m_cilindro = 10
    h_cilindro = 250 
    centro_cilindro = Ponto(100, -150, -220) #Ponto(0, -60, -200) -150
    d_cil = Vetor(0, 1, 0)
    K_d_cilindro= Vetor(0.6627, 0.6627, 0.6627)
    K_a_cilindro= Vetor(0.6627, 0.6627, 0.6627)
    K_e_cilindro= Vetor(0.6627, 0.6627, 0.6627)
    material_cilindro = Material(Cor(255, 0, 0),K_e_cilindro, K_d_cilindro, K_a_cilindro, m_cilindro)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_poste = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    h_cilindro = 30 
    centro_cilindro = Ponto(70, 95, -220) #Ponto(0, -60, -200) -150
    d_cil = Vetor(1, 0, 0)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_poste2 = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    h_cilindro = 20 
    centro_cilindro = Ponto(70, 80, -220) #Ponto(0, -60, -200) -150
    d_cil = Vetor(0, 1, 0)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_poste3 = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    rCilindro  = 12
    h_cilindro = 10 
    centro_cilindro = Ponto(70, 70, -220) #Ponto(0, -60, -200) -150
    d_cil = Vetor(0, 1, 0)
    centroTopo = Soma_vetores(centro_cilindro, Vetor_escalar(d_cil, h_cilindro))
    topoPlano = PlanoCircular(centroTopo, d_cil, rCilindro, material_cilindro)
    n_Base = d_cil
    baseC= PlanoCircular(centro_cilindro, n_Base,rCilindro, material_cilindro)
    cilindro_poste4 = Cilindro(centro_cilindro,rCilindro, d_cil,  h_cilindro, material_cilindro, topoPlano, baseC)

    rEsfera        = 8
    m_esfera       = 10
    centro_esfera  = Ponto(70, 70, -220)
    K_d_esfera     = Vetor(1,1,1)
    K_a_esfera     = Vetor(1,1,1)
    K_e_esfera     = Vetor(1,1,1)
    materialEsfera = Material(Cor(255, 0, 0), K_d_esfera, K_a_esfera, K_e_esfera, m_esfera)
    esfera_poste = Esfera(centro_esfera, rEsfera, materialEsfera)



    tam_aresta = 60
    posicaoCentro = Ponto(200, -110, -500)
    #posicaoCentro = Ponto(50, -110, -250)
    normal_cubo = Vetor(1, 1, 1)
    materialCuboBase= Material(Cor(255, 0, 0), Vetor(1, 0.75, 0.05), Vetor(1, 0.75, 0.05), Vetor(1, 0.75, 0.05), m_esfera)
    materialCuboPorta= Material(Cor(255, 0, 0), Vetor(0.94, 0.48, 0.36), Vetor(0.94, 0.48, 0.36), Vetor(0.94, 0.48, 0.36), m_esfera)
    materialCuboTelha= Material(Cor(255, 0, 0), Vetor(0.51, 0.17,0.090), Vetor(0.51, 0.17,0.090), Vetor(0.51, 0.17,0.090), m_esfera)
    objeto_cubo_telha_esq = Cubo(posicaoCentro, tam_aresta, normal_cubo, materialCuboTelha )
    objeto_cubo_telha_dir = Cubo(posicaoCentro, tam_aresta, normal_cubo, materialCuboTelha )
    objeto_cubo_telha_base = Cubo(posicaoCentro, tam_aresta, normal_cubo, materialCuboTelha )
    objeto_cubo_base = Cubo(posicaoCentro, tam_aresta, normal_cubo, materialCuboBase )
    objeto_cubo_porta = Cubo(posicaoCentro, tam_aresta, normal_cubo, materialCuboPorta )
    objeto_cubo_janela = Cubo(posicaoCentro, tam_aresta, normal_cubo, materialCuboPorta )
    vetor_translacao = Vetor(4, 4, -5)

    axis_z_cone = Vetor(0, 0, 1)

   # objeto_cubo_telha_esq.rotacao(axis_z_cone, 0.45) #45 graus em
   # objeto_cubo_telha_esq.translacao(vetor_translacao)
    #objeto_cone.rotacao(axis_z_cone, 2)
    objeto_cubo_porta.escala(Vetor(1.5, 3, 0.1))
    objeto_cubo_porta.translacao(Vetor(tam_aresta, 0, 1))

    objeto_cubo_janela.escala(Vetor(1.5, 1.5, 0.1))
    objeto_cubo_janela.translacao(Vetor((tam_aresta*3), (tam_aresta*1.5), 1))

    objeto_cubo_telha_base.escala(Vetor(5, 0.1, 3))
    objeto_cubo_telha_base.translacao(Vetor(0, (tam_aresta*4+5), 0))

    objeto_cubo_telha_esq.escala(Vetor(4, 0.3, 3))
    objeto_cubo_telha_esq.translacao(Vetor(-100, (tam_aresta*2) , 0))
    objeto_cubo_telha_dir.escala(Vetor(4, 0.3, 3))
    objeto_cubo_base.escala(Vetor(5, 4, 3))
    
    objeto_cubo_telha_esq.cisalhamento(Vetor(0, 0, 1), Vetor(0, 1, 0), 0.78)
    objeto_cubo_telha_dir.cisalhamento(Vetor(0, 0, 1), Vetor(0, 1, 0),  -0.78)
    objeto_cubo_telha_dir.translacao(Vetor(140, (tam_aresta*8.5)  , 10))
    P_F = Ponto(0, 0, 0)
    intensidade_pf = Vetor(0.7, 0.7, 0.7)
    intensidade_ambiente = Vetor(0.5, 0.5, 0.5)   # Ambiente

    luz_ambiente = LuzAmbiente(intensidade_ambiente)
    luz_pontual = LuzPontual(
        P_F, intensidade_pf)

    direcao_luz_direcional = Ponto(0, 1, 0) 

    intensidade_direcional = Vetor(0.7, 0.7, 0.7)
    luz_direcional = LuzDirecional(
      direcao_luz_direcional, intensidade_direcional)

    spot_posicao =  Ponto(70,-100, -220) #Ponto(-100, -150, -220)
    spot_intensidade = Vetor(0.7, 0.7, 0.7)
    spot_direcao = Ponto(0, -1, 0)
    spot_teta = 3.14/6
    luz_spot = LuzSpot(spot_posicao, spot_intensidade, spot_direcao,spot_teta )

    cercado = [cilindro_cercado15, cilindro_cercado16, cilindro_cercado13, cilindro_cercado14, cilindro_cercado12, cilindro_cercado11, cilindro_cercado10,cilindro_cercado9,cilindro_cercado8, cilindro_cercado7,cilindro_cercado6, cilindro_cercado5, cilindro_cercado, cilindro_cercado3,cilindro_cercado2, cilindro_cercado4] 
    silo = [cone_silo, cilindro_celeiro]
    caixa_dagua = [cone_caixadagua, cilindro_caixadagua, cilindro_apoio1, cilindro_apoio2, cilindro_apoio3, cilindro_apoio4] 
    Arvore = [cone_arvore, cilindro_arvore]
    poste = [cilindro_poste, cilindro_poste2, cilindro_poste3, cilindro_poste4, esfera_poste]
    ceu = [ plano_chao]
 
    casa = [objeto_cubo_telha_esq, objeto_cubo_base, objeto_cubo_telha_dir, objeto_cubo_telha_base, objeto_cubo_janela, objeto_cubo_porta]
    #print(objetos[0].material.K_e.x, objetos[0].material.K_e.y)
    luzes = [luz_ambiente,luz_pontual, luz_spot ] #
    cercado = [cilindro_cercado15, cilindro_cercado16, cilindro_cercado13, cilindro_cercado14, cilindro_cercado12, cilindro_cercado11, cilindro_cercado10,cilindro_cercado9,cilindro_cercado8, cilindro_cercado7,cilindro_cercado6, cilindro_cercado5, cilindro_cercado, cilindro_cercado3,cilindro_cercado2, cilindro_cercado4] 
    objetos = [ceu, cercado, caixa_dagua, silo, casa,poste,Arvore] # ,cercado,caixa_dagua,silo,Arvore, poste
    #objetos = [ceu] 
    #print(objetos[0].material.K_e.x, objetos[0].material.K_e.y)
    #luzes = [luz_ambiente, luz_spot]


    #posicao_c = Vetor(0, 4, 1) #Vetor(0, -5, 1)
   # at = Vetor(0, 0, -100)
   # up = Vetor(0, 10, -100)

    # posicao_c = Vetor(0, 10, 0) #Vetor(0, -5, 1)
    # at = Vetor(0, 20, -160)
    # up = Vetor(0, 40, -160)

    posicao_c = Vetor(70, 500, -220) 
    at = Vetor(70, -100, -220)
    up = Vetor(70, 500, -300)
    camera1 = Camera(posicao_c, at, up)
    matriz = camera1.matriz()

 
 
   

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
