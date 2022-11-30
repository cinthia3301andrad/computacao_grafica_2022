from cena import Cena

from janela import Janela

from esfera import Esfera

from material import Material

from definicoes import Cor, Vetor, Ponto

from luzes import LuzPontual, LuzAmbiente, LuzDirecional

# K_d_esfera     = Vetor(0.854, 0.647, 0.125)
# K_a_esfera     = Vetor(0.854, 0.647, 0.125)
# K_e_esfera     = Vetor(0.854, 0.647, 0.125)
# objeto_esfera1 = Esfera(centro_esfera, rEsfera, Cor(255, 0, 0),K_d_esfera, K_d_esfera, K_d_esfera, m_esfera)


def main():
    largura, altura = 500, 500

    centro_esfera =  Ponto(0, 0, -100)
    # rEsfera        = 5
    # m_esfera       = 10
    # centro_esfera  = Ponto(0, 95, -200), -200)
    rEsfera = 40
    K_d_esfera = Vetor(1, 0, 0)
    K_a_esfera = Vetor(1, 0, 0)
    K_e_esfera = Vetor(1, 0, 0)
    m_esfera = 100
    materialEsfera = Material(Cor(255, 0, 0))

    P_F = Ponto(0, 60, -30)
    intensidade_pf = Vetor(0.7, 0.7, 0.7)
    intensidade_ambiente = Vetor(0.3, 0.3, 0.3)   # Ambiente

    luz_ambiente = LuzAmbiente(intensidade_ambiente, K_a_esfera)
    luz_pontual = LuzPontual(
        P_F, intensidade_pf, K_d_esfera, K_e_esfera, m_esfera)

    direcao_luz_direcional = Ponto(-1., 0, 0.4) #

    intensidade_direcional = Vetor(0.7, 0.7, 0.7)
    luz_direcional = LuzDirecional(
      direcao_luz_direcional, intensidade_direcional, K_d_esfera, K_e_esfera, m_esfera)
    esfera = Esfera(centro_esfera, rEsfera, materialEsfera)

    objetos = [esfera]

    #print(objetos[0].material.K_e.x, objetos[0].material.K_e.y)
    luzes = [ luz_direcional]

    dJanela = 30  # distância entre a janela e o olho observador

    cena = Cena(largura, altura, objetos, luzes)
    janela = Janela(dJanela, largura, altura, cena)

    janela.abrir()
    janela.loopEventos()


main()
