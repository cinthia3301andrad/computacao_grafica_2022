def Vetor(x, y, z):
    return {'x': x, 'y': y, 'z': z}

def Ponto(x, y, z):
    return {'x': x, 'y': y, 'z': z}

def Produto_escalar(v_1, v_2):
    return v_1['x'] * v_2['x'] + v_1['y'] * v_2['y'] + v_1['z'] * v_2['z']

def Produto_arroba(i, k):
    return Vetor(i['x']*k['x'], i['y']*k['y'], i['z']*k['z'])

def Subtracao_vetores(v_1, v):
    return Vetor(v_1['x'] - v['x'], v_1['y'] - v['y'], v_1['z'] - v['z'])

#def Soma_vetores(v_1, v):
#    return Vetor(v_1['x'] + v['x'], v_1['y'] + v['y'], v_1['z'] + v['z'])

#def Equacao_raio(Eye, ti, dr):
#    return Vetor(Eye['x']+ti*dr['x'], Eye['y']+ti*dr['y'], Eye['z']+ti*dr['z'])

def Vetor_escalar(vetor, escalar):
    return Vetor(vetor['x']*escalar, vetor['y']*escalar, vetor['z']*escalar)

def CanvasParaJanela(c, l, janela): #retorna o vetor (Vx, Vy, Vz) que define a direção do raio, ou seja, que parte do meio do pixel atual
    return Vetor(-janela['wj']/2+janela['dx']/2+janela['dx']*c , janela['hj']/2-janela['dy']*l, -janela['d'])

def Calcula_vetor_refletido(L, N):
    escalar_l_n = Produto_escalar(L, N) * 2
    vetor_l_n = Vetor(N['x']*escalar_l_n, N['y']*escalar_l_n, N['z']*escalar_l_n)

    return Subtracao_vetores(vetor_l_n, L)