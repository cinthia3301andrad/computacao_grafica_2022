
from funcoes import normalizaVetor, Subtracao_vetores, produto_vetorial, Produto_escalar

class Camera: 

    def __init__(self, posicao, at, up):
        self.posicao = posicao
        self.at = at
        self.up = up
        self.mundoParaCamera = None

    def matriz(self):
        K = normalizaVetor(Subtracao_vetores(self.posicao, self.at))
        viewUp = normalizaVetor(Subtracao_vetores(self.up, self.posicao))
        I = normalizaVetor(produto_vetorial(viewUp, K))
        J = normalizaVetor(produto_vetorial(K, I))

        coluna4_I= - Produto_escalar(I, self.posicao)
        coluna4_J= - Produto_escalar(J, self.posicao)
        coluna4_K= - Produto_escalar(K, self.posicao)

        M = [[I.x, I.y, I.z, coluna4_I], [J.x, J.y, J.z, coluna4_J], [K.x, K.y, K.z, coluna4_K], [0, 0, 0, 1]]

        return M