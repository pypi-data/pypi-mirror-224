from fock_matrix import overlap 
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

H1_pg1a= primitive_gaussian(0.3425250914E+01, 0.1543289673E+00,[0,0,0],0,0,0)
H1_pg1b= primitive_gaussian(0.6239137298E+00 ,0.5353281423E+00,[0,0,0],0,0,0)
H1_pg1c= primitive_gaussian( 0.1688554040E+00,0.4446345422E+00,[0,0,0],0,0,0)

H2_pg1a= primitive_gaussian(0.3425250914E+01, 0.1543289673E+00,[1.4,0,0],0,0,0)
H2_pg1b= primitive_gaussian(0.6239137298E+00 ,0.5353281423E+00,[1.4,0,0],0,0,0)
H2_pg1c= primitive_gaussian( 0.1688554040E+00,0.4446345422E+00,[1.4,0,0],0,0,0)

H1_1s=[H1_pg1a,H1_pg1b,H1_pg1c]
H2_1s=[H2_pg1a,H2_pg1b,H2_pg1c]

z=[1.0,1.0]
atom_coordinates= [np.array([0,0,0]),np.array([1.4,0,0])]
molecule=[H1_1s,H2_1s]
def test_overlap():
	assert np.round(overlap(molecule)[0][0],1) == 1

