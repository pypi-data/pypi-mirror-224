import sys
import numpy as np
from scipy import special
import math

def overlap(molecule):
    
    nbasis=len(molecule)
    S=np.zeros([nbasis,nbasis])
    
    for i in range(nbasis):
        for j in range(nbasis):
            
            nprimitives_i= len(molecule[i])
            nprimitives_j= len(molecule[j])
            
            for k in range(nprimitives_i):
                for l in range(nprimitives_j):
                    
                    N= molecule[i][k].A * molecule[j][l].A
                    
                    p= molecule[i][k].alpha + molecule[j][l].alpha
                    
                    q = molecule[i][k].alpha * molecule[j][l].alpha / p
                    
                    Q = molecule[i][k].coordinates - molecule[j][l].coordinates
                    
                    Q2= np.dot(Q,Q)
                    
                    S[i,j] += N* molecule[i][k].coeff * molecule[j][l].coeff * (np.pi/p)**(3/2)* np.exp(-q*Q2) 
    return S 
                    
            
