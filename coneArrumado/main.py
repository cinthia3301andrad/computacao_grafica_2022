
import math
from PIL  import Image

from plano    import *
from esfera   import *
from cilindro import *
from cone     import *

from janela import *
from canvas import *
from cena   import *

from calc_vetores import *
from cor import *

posicaoOlhoObservador = Ponto(0,0,0)
P_F                   = Ponto(0, 200 , 0)
dJanela               = 15 #distância entre a janela e o olho observador

canvas  = Canvas(Cor(100, 100, 200))
janela  = Janela(dJanela, canvas['wc'], canvas['hc'])

# Definição da esfera
rEsfera        = 40
m_esfera       = 10
centro_esfera  = Ponto(0, 0, -100)
K_d_esfera     = Vetor(0.7, 0.2, 0.2)
K_a_esfera     = Vetor(0.7, 0.2, 0.2)
K_e_esfera     = Vetor(0.7, 0.2, 0.2)
objeto_esfera1 = Esfera(centro_esfera, rEsfera, Cor(255, 0, 0),K_d_esfera, K_d_esfera, K_d_esfera, m_esfera)
#objeto_esfera2 = Esfera(Ponto(10, 0, -(janela['d'] +rEsfera +20)), rEsfera, Cor(0, 255, 0))

# Definição do cilindro
rCilindro        = rEsfera/3
m_cilindro       = 10
h_cilindro       = 3*rEsfera
centro_cilindro  = centro_esfera
#d_cil           = Vetor(-1/math.sqrt(3), 1/math.sqrt(3), -1/math.sqrt(3))
d_cil            = Vetor(0, 1, 0)
K_d_cilindro     = Vetor(0.2, 0.3, 0.8)
K_a_cilindro     = Vetor(0.2, 0.3, 0.8)
K_e_cilindro     = Vetor(0.2, 0.3, 0.8)
objeto_cilindro1 = Cilindro(centro_cilindro, 
                      rCilindro, h_cilindro, d_cil,
                      Cor(255, 0, 0),K_e_esfera, K_d_esfera, K_a_esfera, m_esfera)

# Definição do plano do chão
P_pi         = Ponto(0, -rEsfera, 0) #ponto conhecido
n_bar        = Vetor(0, 1, 0) #vetor normal
K_d_chao     = Vetor (0.2, 0.7, 0.2)
K_a_chao     = Vetor(0.2, 0.7, 0.2)
K_e_chao     = Vetor(0.0, 0.0, 0.0)
m_plano_chao = 1
plano_chao   = Plano(P_pi, n_bar, Cor(0, 255, 255),K_e_chao, K_d_chao, K_a_chao, m_plano_chao)

# Definição do plano de fundo
P_pi         = Ponto(0, -rEsfera, -200) #ponto conhecido
n_bar        = Vetor(0, 0, 1) #vetor normal
K_d_fundo     = Vetor(0.3, 0.3, 0.7)
K_a_fundo     = Vetor(0.8, 0.8, 0.8)
K_e_fundo     = Vetor(0.0, 0.0, 0.0)
m_plano_fundo = 1
plano_fundo   = Plano(P_pi, n_bar , Cor(0, 0, 255), K_e_fundo, K_d_fundo, K_a_fundo, m_plano_fundo)

# Definição do cone
centro_cone   = Calcula_ponto_raio(centro_esfera, h_cilindro, d_cil)
rCone         = 1.5*rEsfera
hCone         = rCone
#d_cone        = Vetor(-1/math.sqrt(3), 1/math.sqrt(3), -1/math.sqrt(3))
d_cone        = d_cil

K_a_cone      = Vetor(0.8, 0.3, 0.2) #Vetor(0.0, 0.0, 0.0)
K_d_cone      = Vetor(0.8, 0.3, 0.2)
K_e_cone      = Vetor(0.8, 0.3, 0.2) #Vetor(0.0, 0.0, 0.0)
m_cone        = 100
objeto_cone   = Cone(centro_cone,
                    rCone, hCone, d_cone,
                    Cor(255, 0, 0), K_e_cone, K_d_cone, K_a_cone, m_cone, 1)

#objetos  = [plano_fundo, plano_chao, objeto_esfera1, objeto_cilindro1, objeto_cone  ]
objetos   = [plano_chao, plano_fundo, objeto_cone, objeto_esfera1, objeto_cilindro1]
#objetos  = [ objeto_esfera1]

cena      = Cena(objetos)

image     = Image.new(mode="RGB", size=(canvas['wc'], canvas['hc']))
pixels    = image.load()

for x in range(canvas['wc']):
    for y in range(canvas['hc']):
        # Direção do raio saindo da origem e passando pelo centro de um quadrado
        # da tela da Janela
        D     = CanvasParaJanela(x, y, janela) #centro do pixel atual
         
        # Projeção perspectiva: Raios convergem para o olho do observador que está a uma distância
        # finita do plano de projeção ("Plano da janela" ou "Plano da tela de mosquito")
        # Obs.: Para ver o cenário todo, ele precisa estar no campo de visão
        #       (dentro do "frustum", i.e., dentro do tronco de pirâmide de visualização)
        #color = DecideCor(posicaoOlhoObservador, cena, canvas, D, P_F)
        
        # Projeção orthográfica: Raios paraleleos saindo de cada centro de retângulo da "tela de mosquito"
        # com vetor direção perpendicular ao plano de projeção, isto é, com d_r = -k = (0, 0, -1)
        # Obs.: Para ver o cenário todo, a Janela tem de ser bem grande
        color = DecideCor(D, cena, canvas, Vetor(0, 0, -1), P_F)

        pixels[x, y] = (color['r'], color['g'], color['b'])
      
image.save("esfera.png", format="png")
image.show()
