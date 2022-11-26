import numpy as np
from raio import Raio

from material import Material


t_correction = 0.000001

class Objeto:
    def __init__(self, posicao: np.ndarray, material: Material):
        self.posicao = posicao
        self.material = material

    def intersecao(self, raio: Raio):
        return None

    def getNormal(self, point: np.ndarray):
        return None

    def getCor(self, point: np.ndarray):
        return self.material.cor


