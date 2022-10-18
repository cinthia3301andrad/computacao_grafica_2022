import math

from cubo     import *

from calc_vetores import *
from cor import *

from intersecoes import  IntersecaoPlano


def Malha( K_e,K_d,K_a, m, faces):
    return {
        'K_e': K_e,
        'K_d': K_d,
        'K_a': K_a,
        'm': m,
        'faces':faces,
        'normal': Vetor(0, 0, 0),
    }



