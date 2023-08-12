import sys
import numpy as np
from scipy import special
import math

class primitive_gaussian():
    def __init__(self,alpha,coeff,coordinates,l1,l2,l3):
        self.alpha=alpha
        self.coeff=coeff
        self.coordinates= np.array(coordinates)
        self.A= (2*alpha/np.pi)**0.75
