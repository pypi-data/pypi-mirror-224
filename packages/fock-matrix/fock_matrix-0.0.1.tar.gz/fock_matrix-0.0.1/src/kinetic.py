import sys
import numpy as np
from scipy import special
import math

def kinetic(molecule):
    
    nbasis=len(molecule)
    T=np.zeros([nbasis,nbasis])
    
    for i in range(nbasis):
        for j in range(nbasis):
            
            nprimitives_i= len(molecule[i])
            nprimitives_j= len(molecule[j])
            
            for k in range(nprimitives_i):
                for l in range(nprimitives_j):
                    
                    N= molecule[i][k].A * molecule[j][l].A
                    c1c2= molecule[i][k].coeff * molecule[j][l].coeff 
                    p= molecule[i][k].alpha + molecule[j][l].alpha
                    
                    q = molecule[i][k].alpha * molecule[j][l].alpha / p
                    
                    Q = molecule[i][k].coordinates - molecule[j][l].coordinates
                    
                    Q2= np.dot(Q,Q)
                    
                    P= molecule[i][k].alpha * molecule[i][k].coordinates + molecule[j][l].alpha * molecule[j][l].coordinates 
                    
                    Pp= P/p
                    PG = Pp - molecule[j][l].coordinates
                    PGx2 = PG[0]* PG[0]
                    PGy2 = PG[1]* PG[1]
                    PGz2 = PG[2]* PG[2]
                    
                    
                    s= N* c1c2* (np.pi/p)**(3/2)* np.exp(-q*Q2) 
                    
                    T[i,j] += 3* molecule[j][l].alpha * s
                    T[i,j] -= 2*molecule[j][l].alpha * molecule[j][l].alpha * s* (PGx2+0.5/p)
                    T[i,j] -= 2*molecule[j][l].alpha * molecule[j][l].alpha * s* (PGy2+0.5/p)
                    T[i,j] -= 2*molecule[j][l].alpha * molecule[j][l].alpha * s* (PGz2+0.5/p)
            
    return T        
    

