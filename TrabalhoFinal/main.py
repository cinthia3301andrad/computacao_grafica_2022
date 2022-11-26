from cena import Cena

from janela import Janela

from esfera import Esfera

from material import Material

from definicoes import Cor, Vetor, Ponto

# K_d_esfera     = Vetor(0.854, 0.647, 0.125)
# K_a_esfera     = Vetor(0.854, 0.647, 0.125)
# K_e_esfera     = Vetor(0.854, 0.647, 0.125)
# objeto_esfera1 = Esfera(centro_esfera, rEsfera, Cor(255, 0, 0),K_d_esfera, K_d_esfera, K_d_esfera, m_esfera)

def main():
    largura, altura = 500, 500

    centro_esfera  = Ponto(0, 95, -200)
# rEsfera        = 5
# m_esfera       = 10
# centro_esfera  = Ponto(0, 95, -200), -200)
    rEsfera        = 5
    K_d_esfera     = Vetor(0.854, 0.647, 0.125)
    K_a_esfera     = Vetor(0.854, 0.647, 0.125)
    K_e_esfera     = Vetor(0.854, 0.647, 0.125)
    m_esfera       = 10
    materialEsfera       = Material( Cor(255, 0, 0), K_e_esfera, K_d_esfera, K_a_esfera, m_esfera)
    esfera         = Esfera(centro_esfera, rEsfera, materialEsfera)

    objetos = [esfera]
   
    #print(objetos[0].material.K_e.x, objetos[0].material.K_e.y)
    luzes   = []

    dJanela               = 30 #distância entre a janela e o olho observador

    cena = Cena(largura, altura, objetos, luzes)
    janela = Janela(dJanela, largura, altura, cena)

    janela.abrir()
    janela.loopEventos()


main()