wJanela = 50 #dimenções da janela, por onde o observador ver o mundo
hJanela = 50 

def Janela(dJanela, colunasCanvas, linhasCanvas): #d = distância entre a janela e a esfera
    return {'wj': wJanela, 'hj': hJanela, 'd': dJanela, 'dx': wJanela/colunasCanvas, 'dy': hJanela/linhasCanvas}