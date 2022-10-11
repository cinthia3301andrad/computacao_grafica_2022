import math
from PIL import Image

def Vetor( x, y, z):
    return {'x': x, 'y': y, 'z': z}
def Cor(r, g, b):
    return {'r': r, 'g': g, 'b': b}

def Janela(wj, hj, d):
    return {'wj': wj, 'hj': hj, 'd': d}

def Esfera(centro, r, cor):
    return {'centro': centro, 'r': r, 'cor': cor}

def Canvas(wc, hc, janela, cor_fundo):
    return {
        'wc': wc,
        'hc': hc,
        'janela': janela,
        'cor_fundo': cor_fundo,
        'dx': janela['wj']/wc,
        'dy': janela['hj']/hc}
     
def CanvasParaJanela(c, l, janela, canvas): #retorna o vetor (Vx, Vy, Vz) que representa o r lançado, ou seja, que parte do meio do pixel atual
    return Vetor(-janela['wj']/2+canvas['dx']/2+canvas['dx']*c, janela['hj']/2-canvas['dy']*l, -janela['d'])

def Multiplica_vetor(v_1, v_2):
        return v_1['x'] * v_2['x'] + v_1['y'] * v_2['y'] + v_1['z'] * v_2['z']

def Sub(v_1, v):
        return Vetor(v_1['x'] - v['x'], v_1['y'] - v['y'], v_1['z'] - v['z'])
def Intersecao(esfera, observador, dr):
    w = Sub(observador, esfera['centro'])

    a = Multiplica_vetor(dr, dr)
    b = 2 * Multiplica_vetor(w, dr)
    c = Multiplica_vetor(w, w) - esfera['r'] * esfera['r'] 

    delta = b * b - 4 * a * c
    if(delta < 0):
        return math.inf, math.inf

    t1 = (-b + math.sqrt(delta)) /(2 * a)
    t2 = (-b - math.sqrt(delta)) /(2 * a)
        
    return (t1, t2)

def Cena(objeto, v_partida_cameraa, canvas):
    return {'objeto': objeto, 'v_partida_cameraa': v_partida_cameraa, 'canvas': canvas}

def DecideCor(cena, canvas, esfera, dr):
    limite_t = math.inf
    esfera_encontrada = None

    [t1, t2] = Intersecao(esfera, cena['v_partida_cameraa'], dr)
    if( t1 < limite_t):
        esfera_encontrada = esfera

    if( t2 < limite_t):
        esfera_encontrada = esfera
            
    if(esfera_encontrada == None):
        return canvas['cor_fundo']
    return esfera['cor']


wJanela = 500 #matriz de pixel do CANVAS
hJanela = 500 #matriz de pixel do CANVAS
image = Image.new(mode="RGB", size=(500, 500))
pixels = image.load()

janela = Janela( 10, 10, 3) 
canvas = Canvas(500, 500, janela, Cor(100, 100, 100))
rEsfera = 1
objeto_esfera = Esfera(Vetor(0, 0, -(janela['d'] + 8*rEsfera)), rEsfera, Cor(255, 0, 0))

cena = Cena(objeto_esfera, Vetor(0, 0, 0), canvas)

image = Image.new(mode="RGB", size=(canvas['wc'], canvas['hc']))
pixels = image.load()
''' cena = Cena(objeto_esfera, Vetor(0, 0, 0), canvas)
 '''
for x in range(canvas['wc']):
    for y in range(canvas['hc']):
        dr = CanvasParaJanela(x, y, janela, canvas)
        color = DecideCor(cena, canvas, objeto_esfera, dr)
        pixels[y, x] = (color['r'], color['g'], color['b'])
      
image.save("esfera.png", format="png")
image.show()
