import numpy as np
from utils.ray import Ray
from utils import transforms
from utils.material import Material


class Light:
    def __init__(self, position: np.ndarray, intensidade: float, cor: np.ndarray = np.array([255., 255., 255.])):
        self.position = position
        self.intensidade = intensidade
        self.cor = cor/255.

    def computaLuz(self, point: np.ndarray, normal: np.ndarray, ray: Ray, shininess: float):
        return 0

    def getDirection(self, point: np.ndarray):
        direction = self.position - point
        distance = np.linalg.norm(direction)
        return direction / distance, distance

    @property
    def ignoreShadow(self):
        return False

class PointLight(Light):
    def __init__(self, position: np.ndarray, intensidade, cor: np.ndarray = np.array([255., 255., 255.])):
        super().__init__(position, intensidade, cor)

    def computaLuz(self, point: np.ndarray, normal: np.ndarray, ray: Ray, material: Material):
        direction = self.position - point
        distance = np.linalg.norm(direction)
        direction = direction / distance

        dot = direction @ normal
        if dot <= 0: return 0

        sqrtD = (distance ** 0.5)
        lightness = self.intensidade * dot / sqrtD
        if material.shininess == np.inf:
            return lightness

        r = 2*(direction @ normal) * normal - direction
        dot2 = r @ -ray.direction
        if dot2 > 0:
            lightness += self.intensidade * (dot2 ** material.shininess) / sqrtD

        return lightness

class AmbientLight(Light):
    def __init__(self, intensidade, cor):
        super().__init__(np.zeros(3), intensidade, cor)

    def computaLuz(self):
        return self.intensidade

    @property
    def ignoreShadow(self):
        return True


class DirectionalLight(Light):
    def __init__(self, direction: np.ndarray, intensidade: np.ndarray, cor = np.array([255., 255., 255.])):
        super().__init__(np.array([0., 0., 0.]), intensidade, cor)
        self.direction = transforms.normalize(-direction)

    def computaLuz(self, point: np.ndarray, normal: np.ndarray, ray: Ray, material: Material):
        dot = self.direction @ normal
        if dot <= 0: return 0

        lightness = self.intensidade * dot
        if material.shininess == np.inf:
            return lightness

        r = 2*(self.direction @ normal) * normal - self.direction
        dot2 = r @ -ray.direction
        if dot2 > 0:
            lightness += self.intensidade * (dot2 ** material.shininess)

        return lightness

    def getDirection(self, point: np.ndarray):
        return self.direction, np.inf
