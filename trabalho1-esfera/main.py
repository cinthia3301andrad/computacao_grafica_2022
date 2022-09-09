
from PIL import Image

from calc_vetores import *
from janela import *
from canvas import *
from cena import *
from esfera import *
from cor import *
from plano import *

posicaoOlhoObservador = Ponto(0,0,0)
P_F = Ponto(0, 60 , -30) #Posição da fonte pontual situada a 5 centimetros acima do olho do observador.

dJanela = 30 #distância entre a janela e o olho observador

canvas = Canvas(Cor(100, 100, 100))
janela = Janela(dJanela, canvas['wc'], canvas['hc'])  

rEsfera = 40 
m_esfera = 10
K_d_esfera = Vetor(0.7, 0.2, 0.2)
K_a_esfera = Vetor(0.7, 0.2, 0.2)
K_e_esfera = Vetor(0.7, 0.2, 0.2)
objeto_esfera1 = Esfera(Ponto(0, 0, -100), rEsfera, Cor(255, 0, 0),K_d_esfera, K_d_esfera, K_d_esfera, m_esfera)
#objeto_esfera2 = Esfera(Ponto(10, 0, -(janela['d'] +rEsfera +20)), rEsfera, Cor(0, 255, 0))

P_pi = Ponto(0, -rEsfera, 0) #ponto conhecido
n_bar = Vetor(0, 1, 0) #vetor normal
K_d_chao = Vetor (0.2, 0.7, 0.2)
K_a_chao = Vetor(0.2, 0.7, 0.2)
K_e_chao = Vetor(0.0, 0.0, 0.0)
m_plano_chao = 1
plano_chao = Plano(P_pi, n_bar, Cor(0, 255, 255),K_e_chao, K_d_chao, K_a_chao, m_plano_chao)

K_d_fundo = Vetor(0.3, 0.3, 0.7)
K_a_fundo = Vetor(0.3, 0.3, 0.7)
K_e_fundo = Vetor(0.0, 0.0, 0.0)
m_plano_fundo = 1
plano_fundo = Plano(Ponto(0, 0, -200), Vetor(0, 0, 1) , Cor(0, 0, 255), K_e_fundo, K_d_fundo, K_a_fundo, m_plano_fundo)


objetos = [objeto_esfera1,plano_chao, plano_fundo]

cena = Cena(objetos)

image = Image.new(mode="RGB", size=(canvas['wc'], canvas['hc']))
pixels = image.load()

for x in range(canvas['wc']):
    for y in range(canvas['hc']):
        D = CanvasParaJanela(x, y, janela) #centro do pixel atual
        color = DecideCor(posicaoOlhoObservador, cena, canvas, D, P_F)

        pixels[x, y] = (color['r'], color['g'], color['b'])
      
image.save("esfera.png", format="png")
image.show()