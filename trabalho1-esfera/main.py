from PIL import Image

from calc_vetores import Ponto, CanvasParaJanela
from janela import *
from canvas import *
from cena import *
from esfera import Esfera
from cor import Cor, DecideCor

posicaoOlhoObservador = Ponto(0,0,0)
P_F = Ponto(0, 5, 0) #Posição da fonte pontual situada a 5 centimetros acima do olho do observador.

image = Image.new(mode="RGB", size=(wc, 500))
pixels = image.load()

dJanela = 100 #distância entre a janela e a esfera

canvas = Canvas(Cor(100, 100, 100))
janela = Janela(dJanela, canvas['wc'], canvas['hc'])  

rEsfera = 25 
objeto_esfera1 = Esfera(Ponto(0, 0, -(janela['d'] + rEsfera)), rEsfera, Cor(255, 0, 0))
#objeto_esfera2 = Esfera(Ponto(10, 0, -(janela['d'] +rEsfera +20)), rEsfera, Cor(0, 255, 0))

objetos = [objeto_esfera1]

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