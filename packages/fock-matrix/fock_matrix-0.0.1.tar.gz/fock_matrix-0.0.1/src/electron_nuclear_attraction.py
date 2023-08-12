import sys
import numpy as np
from scipy import special
import math
def boys(x,n):
    if x==0:
        return(1/2*n+1)
    else:
        return special.gammainc(n+0.5,x) * special.gamma(n+0.5)* (1.0/(2*x**(n+0.5)))


def electron_nuclear_attraction(molecule,atom_coordinates,z):
    
    natom= len(z)
    nbasis=len(molecule)
    V_ne=np.zeros([nbasis,nbasis])

    for atom in range(natom):
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
                        PG = Pp - atom_coordinates[atom]
                        PG2 = np.dot(PG,PG)
                        V_ne[i][j] += -z[atom] * N * c1c2* np.exp(-q*Q2) * (2*np.pi/p) * boys(p*PG2,0)  

    return V_ne        

