import math

from PIL import Image

def Vetor( x, y, z):
    return {'x': x, 'y': y, 'z': z}

def Ponto( x, y, z):
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

def Cena(objetos, posicao_olho_observador):
    return {'objetos': objetos, 'posicao_olho_observador': posicao_olho_observador}

def Calcula_ponto_intersecao(O, t, D):
    return Ponto(
        O['x']+t*D['x'], 
        O['y']+t*D['y'], 
        O['z']+t*D['z'], 
    )

def Calcula_vetor_refletido(L, N):
    escalar_l_n = Produto_escalar(L, N) * 2
    vetor_l_n = Vetor(N['x']*escalar_l_n, N['y']*escalar_l_n, N['z']*escalar_l_n)

    return Subtracao_vetores(vetor_l_n, L)
def Calcula_iluminacao( N, L, r_refletido,v_vetor):
    intensidade_d = 0.0 
    intensidade_e = 0.0
    fd = max(0, Produto_escalar(L, N))
    fe = max(0, Produto_escalar(r_refletido, v_vetor))
    I_F = Vetor(0.7, 0.7, 0.7)  # Intensidade da fonte pontual
    K = Vetor(0.9, 0.5, 0.5)  # Intensidade da fonte pontual

    #luz difusa
    intensidade_d = Produto_escalar(I_F, K) * fd
    intensidade_e = Produto_escalar(I_F, K) * fe
    return intensidade_d + intensidade_e

#cena recebe  o raio e retorna a interseção
def DecideCor(cena, canvas, D, P_F):
    t_proximo = math.inf
    objeto_encontrado = None
    intensidade = 0.0
    for objeto in cena['objetos']:
        [t1, t2] = Intersecao(objeto, cena['posicao_olho_observador'], D)
        if( t1 < t_proximo):
            t_proximo = t1
            objeto_encontrado = objeto

        if( t2 < t_proximo):
            t_proximo = t2
            objeto_encontrado = objeto
    if(objeto_encontrado != None):
        P = Calcula_ponto_intersecao(cena['posicao_olho_observador'],t_proximo , D) #ponto que o raio atual incidiu

    
        N = Subtracao_vetores(P, objeto_encontrado['centro'])
        N = Vetor(N['x']/objeto_encontrado['r'], N['y']/objeto_encontrado['r'], N['z']/objeto_encontrado['r']) #normalizando o vetor N
        #calculo do L
        L = Subtracao_vetores(P_F, P)
        comprimentoL = math.sqrt(Produto_escalar(L, L))
        L = Vetor(L['x']/comprimentoL, L['y']/comprimentoL, L['z']/comprimentoL)
        #calculo do I
        # I = Subtracao_vetores(P, P_F)
        # comprimentoI = math.sqrt(Produto_escalar(I, I))
        # I = Vetor(I['x']/comprimentoI, I['y']/comprimentoI, I['z']/comprimentoI)
        
        v_vetor = Subtracao_vetores(cena['posicao_olho_observador'], P)
        comprimentoV = math.sqrt(Produto_escalar(v_vetor, v_vetor)) 
        v_vetor = Vetor(v_vetor['x']/comprimentoV, v_vetor['y']/comprimentoV, v_vetor['z']/comprimentoV)
        r_vetor_refletido = Calcula_vetor_refletido(L, N)
        intensidade = Calcula_iluminacao( N, L, r_vetor_refletido, v_vetor)
 
    if(objeto_encontrado == None):
        return canvas['cor_fundo']

    return Cor(round(objeto_encontrado['cor']['r']*intensidade),
                round(objeto_encontrado['cor']['g']*intensidade),
               round( objeto_encontrado['cor']['b']*intensidade))


wJanela = 50 #dimenções da janela, por onde o observador ver o mundo
hJanela = 50 
dJanela = 100
wc = 500 #matriz de pixel do CANVAS
hc = 500
rEsfera = 25 
P_F = Ponto(0, 5, 0) #Posição da fonte pontual situada a 5 metros acima do olho do observador.

image = Image.new(mode="RGB", size=(wc, 500))
pixels = image.load()

janela = Janela( wJanela, hJanela, dJanela, wc, hc)  
canvas = Canvas(wc, hc, Cor(100, 100, 100))

objeto_esfera1 = Esfera(Ponto(0, 0, -(janela['d'] + rEsfera+40)), rEsfera, Cor(255, 0, 0))
objeto_esfera2 = Esfera(Ponto(10, 0, -(janela['d'] +rEsfera +20)), rEsfera, Cor(0, 255, 0))

objetos = [objeto_esfera1,objeto_esfera2]

cena = Cena(objetos, Ponto(0, 0, 0))

image = Image.new(mode="RGB", size=(canvas['wc'], canvas['hc']))
pixels = image.load()

for x in range(canvas['wc']):
    for y in range(canvas['hc']):
        D = CanvasParaJanela(x, y, janela) #centro do pixel atual
        color = DecideCor(cena, canvas, D, P_F)

        pixels[x, y] = (color['r'], color['g'], color['b'])
      
image.save("esfera.png", format="png")
image.show()