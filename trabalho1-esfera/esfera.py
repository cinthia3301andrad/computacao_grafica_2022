import math
from PIL import Image

def Vetor( x, y, z):
    return {'x': x, 'y': y, 'z': z}
    
def Cor(r, g, b):
    return {'r': r, 'g': g, 'b': b}

def Janela(wj, hj, d, colunas, linhas):
    return {'wj': wj, 'hj': hj, 'd': d, 'dx': wj/colunas, 'dy': hj/linhas}

def Esfera(centro, r, cor):
    return {'centro': centro, 'r': r, 'cor': cor}

def Canvas(wc, hc, cor_fundo):
    return {
        'wc': wc,
        'hc': hc,
        'cor_fundo': cor_fundo,
    }
     
def CanvasParaJanela(c, l, janela): #retorna o vetor (Vx, Vy, Vz) que define a direção do raio, ou seja, que parte do meio do pixel atual
    return Vetor(-janela['wj']/2+janela['dx']/2+janela['dx']*c , janela['hj']/2-janela['dy']*l, -janela['d'])

def Produto_escalar(v_1, v_2):
        return v_1['x'] * v_2['x'] + v_1['y'] * v_2['y'] + v_1['z'] * v_2['z']

def Subtracao_vetores(v_1, v):
        return Vetor(v_1['x'] - v['x'], v_1['y'] - v['y'], v_1['z'] - v['z'])
        
def Intersecao(esfera, observador, D):
    w = Subtracao_vetores(observador, esfera['centro'])

    a = Produto_escalar(D, D)
    b = 2 * Produto_escalar(w, D)
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
def DecideCor(cena, canvas, objetos, D):
    limite_t = math.inf
    esfera_encontrada = None

    
    for objeto in objetos:
        [t1, t2] = Intersecao(objeto, cena['v_partida_cameraa'], D)
        if( t1 < limite_t):
            limite_t = t1
            esfera_encontrada = objeto

        if( t2 < limite_t):
            limite_t = t2
            esfera_encontrada = objeto
            
    if(esfera_encontrada == None):
        return canvas['cor_fundo']
    return esfera_encontrada['cor']


wJanela = 50 #dimenções da janela, por onde o observador ver o mundo
hJanela = 50 
dJanela = 100
wc = 500 #matriz de pixel do CANVAS
hc = 500
rEsfera = 25 

image = Image.new(mode="RGB", size=(wc, 500))
pixels = image.load()

janela = Janela( wJanela, hJanela, dJanela, wc, hc) 
canvas = Canvas(wc, hc, Cor(100, 100, 100))

objeto_esfera1 = Esfera(Vetor(0, 0, -(janela['d'] + rEsfera)), rEsfera, Cor(255, 0, 0))
objeto_esfera2 = Esfera(Vetor(10, 0, -(janela['d'] +rEsfera +20)), rEsfera, Cor(0, 255, 0))

objetos = [objeto_esfera1, objeto_esfera2 ]
cena = Cena(objetos, Vetor(0, 0, 0))

image = Image.new(mode="RGB", size=(canvas['wc'], canvas['hc']))
pixels = image.load()

for x in range(canvas['wc']):
    for y in range(canvas['hc']):
        D = CanvasParaJanela(x, y, janela)
        color = DecideCor(cena, canvas, objetos, D)
        pixels[x, y] = (color['r'], color['g'], color['b'])
      
image.save("esfera.png", format="png")
image.show()