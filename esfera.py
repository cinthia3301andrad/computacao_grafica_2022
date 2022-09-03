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
        'cor_fundo': cor_fundo,
        'janela': janela,
        'dx': janela['wj']/wc,
        'dy': janela['hj']/hc, 
    }
     
def CanvasParaJanela(c, l, janela, canvas): #retorna o vetor (Vx, Vy, Vz) que representa o r lançado, ou seja, que parte do meio do pixel atual
    return Vetor(-janela['wj']/2+canvas['dx']/2+canvas['dx']*c , janela['hj']/2-canvas['dy']*l, -janela['d'])

def Produto_escalar(v_1, v_2):
        return v_1['x'] * v_2['x'] + v_1['y'] * v_2['y'] + v_1['z'] * v_2['z']

def Subtracao_vetores(v_1, v):
        return Vetor(v_1['x'] - v['x'], v_1['y'] - v['y'], v_1['z'] - v['z'])
        
def Intersecao(esfera, observador, centro_px):
    w = Subtracao_vetores(observador, esfera['centro'])

    a = Produto_escalar(centro_px, centro_px)
    b = 2 * Produto_escalar(w, centro_px)
    c = Produto_escalar(w, w) - esfera['r'] * esfera['r'] 

    delta = b * b - 4 * a * c
    if(delta < 0):
        return math.inf, math.inf

    t1 = (-b + math.sqrt(delta)) / (2 * a)
    t2 = (-b - math.sqrt(delta)) / (2 * a)
        
    return (t1, t2)

def Cena(objeto, v_partida_cameraa):
    return {'objeto': objeto, 'v_partida_cameraa': v_partida_cameraa}

#cena recebe o raio e retorna a interseção
def DecideCor(cena, canvas, esfera, centro_px):
    limite_t = math.inf
    esfera_encontrada = None

    [t1, t2] = Intersecao(esfera, cena['v_partida_cameraa'], centro_px)
    if( t1 < limite_t):
        esfera_encontrada = esfera

    if( t2 < limite_t):
        esfera_encontrada = esfera
            
    if(esfera_encontrada == None):
        return canvas['cor_fundo']
    return esfera['cor']


wJanela = 50 #matriz de pixel do CANVAS
hJanela = 50 #matriz de pixel do CANVAS
dJanela = 100
image = Image.new(mode="RGB", size=(500, 500))
pixels = image.load()

janela = Janela( wJanela, hJanela, dJanela) 
canvas = Canvas(500, 500, janela, Cor(100, 100, 100))
rEsfera = 25 
objeto_esfera = Esfera(Vetor(0, 0, -(janela['d'] + rEsfera*1)), rEsfera, Cor(255, 0, 0))

cena = Cena(objeto_esfera, Vetor(0, 0, 0))

image = Image.new(mode="RGB", size=(canvas['wc'], canvas['hc']))
pixels = image.load()

for x in range(canvas['wc']):
    for y in range(canvas['hc']):
        centro_px = CanvasParaJanela(x, y, janela, canvas)
        color = DecideCor(cena, canvas, objeto_esfera, centro_px)
        pixels[x, y] = (color['r'], color['g'], color['b'])
      
image.save("esfera.png", format="png")
image.show()