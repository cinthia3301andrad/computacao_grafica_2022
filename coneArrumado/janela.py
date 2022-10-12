wJanela = 400 #dimenções da janela, por onde o observador ver o mundo
hJanela = 400

def Janela(dJanela, colunasCanvas, linhasCanvas): #d = distância entre a janela e o olho observador
    return {'wj': wJanela, 'hj': hJanela, 'd': dJanela, 'dx': wJanela/colunasCanvas, 'dy': hJanela/linhasCanvas}
