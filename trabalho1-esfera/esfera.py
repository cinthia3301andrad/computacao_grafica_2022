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

def Soma_vetores(v_1, v):
        return Vetor(v_1['x'] + v['x'], v_1['y'] + v['y'], v_1['z'] + v['z'])

def Equacao_raio(Eye, ti, dr):
    return Vetor(Eye['x']+ti*dr['x'], Eye['y']+ti*dr['y'], Eye['z']+ti*dr['z'])
        
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

def Calcula_iluminacao(L, N):
    Ieyed = 0.0
    fd = Produto_escalar(N, L)
    I_F = 0.7
    #comprimentoN = math.sqrt(Produto_escalar(N, N))
    #comprimentoL = math.sqrt(Produto_escalar(L, L))
    if(fd > 0): 
       Ieyed += I_F * fd
    return Ieyed
  

    

#cena recebe o raio e retorna a interseção
def DecideCor(cena, canvas, objetos, D, P_F):
    t_proximo = math.inf
    esfera_encontrada = None
    cor_final = objetos[0]['cor']

    for objeto in objetos:
        [t1, t2] = Intersecao(objeto, cena['v_partida_cameraa'], D)
        if( t1 < t_proximo):
            t_proximo = t1
            esfera_encontrada = objeto

        if( t2 < t_proximo):
            t_proximo = t2
            esfera_encontrada = objeto
        
    if(esfera_encontrada != None):
        P = Equacao_raio(cena['v_partida_cameraa'], t_proximo, D) #ponto de interseção do raio de direção D com a esfera no ponto t_proximo 
        
        N = Subtracao_vetores(P, esfera_encontrada['centro']) #vetor normal que sai no ponto P
        N = Vetor(N['x']/esfera_encontrada['r'], N['y']/esfera_encontrada['r'], N['z']/esfera_encontrada['r']) #normalizando
        
        L = Subtracao_vetores(P_F , P ) #vetor unitario que sai do ponto P e vai em direção ao ponto de luz P_F
        comprimentoL = math.sqrt(Produto_escalar(L, L))
        L = Vetor(L['x']/comprimentoL, L['y']/comprimentoL, L['z']/comprimentoL) #normalizando
        cor_final = Calcula_iluminacao(L, N)
       
    if(esfera_encontrada == None):
        return canvas['cor_fundo']

    return Cor(round(esfera_encontrada['cor']['r']*cor_final), 
            round(esfera_encontrada['cor']['g']*cor_final), 
            round(esfera_encontrada['cor']['b']*cor_final))


wJanela = 50 #dimenções da janela, por onde o observador ver o mundo
hJanela = 50 
dJanela = 100
wc = 500 #matriz de pixel do CANVAS
hc = 500
rEsfera = 25 

P_F = Vetor(0, 5, 0) #Posição da fonte pontual situada a 5 metros acima do olho do observador.

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
        color = DecideCor(cena, canvas, objetos, D, P_F)
   
        pixels[x, y] = (color['r'], color['g'], color['b'])
      
image.save("esfera.png", format="png")
image.show()