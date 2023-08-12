import sys
import numpy as np
from scipy import special
import math


def boys(x,n):
    if x==0:
        return(1/2*n+1)
    else:
        return special.gammainc(n+0.5,x) * special.gamma(n+0.5)* (1.0/(2*x**(n+0.5)))


def electron_electron_repulsion(molecule):
    
    nbasis = len(molecule)   
    
    V_ee = np.zeros([nbasis, nbasis, nbasis, nbasis])
 
    for i in range(nbasis):
        for j in range(nbasis):
            for k in range(nbasis):
                for l in range(nbasis):

                    nprimitives_i = len(molecule[i])
                    nprimitives_j = len(molecule[j])
                    nprimitives_k = len(molecule[k])
                    nprimitives_l = len(molecule[l])
            
                    for ii in range(nprimitives_i):
                        for jj in range(nprimitives_j):
                            for kk in range(nprimitives_k):
                                for ll in range(nprimitives_l):

                                    N = molecule[i][ii].A * molecule[j][jj].A * molecule[k][kk].A * molecule[l][ll].A
                                    cicjckcl = molecule[i][ii].coeff * molecule[j][jj].coeff * \
                                               molecule[k][kk].coeff * molecule[l][ll].coeff
                    
                                    pij = molecule[i][ii].alpha + molecule[j][jj].alpha
                                    pkl = molecule[k][kk].alpha + molecule[l][ll].alpha
                         
                                    Pij = molecule[i][ii].alpha*molecule[i][ii].coordinates +\
                                          molecule[j][jj].alpha*molecule[j][jj].coordinates
                                    Pkl = molecule[k][kk].alpha*molecule[k][kk].coordinates +\
                                          molecule[l][ll].alpha*molecule[l][ll].coordinates
                            
                                    Ppij = Pij/pij
                                    Ppkl = Pkl/pkl
                                    
                                    PpijPpkl  = Ppij - Ppkl
                                    PpijPpkl2 = np.dot(PpijPpkl,PpijPpkl)
                                    denom     = 1.0/pij + 1.0/pkl
                            
                                    qij = molecule[i][ii].alpha * molecule[j][jj].alpha / pij
                                    qkl = molecule[k][kk].alpha * molecule[l][ll].alpha / pkl

                                    Qij = molecule[i][ii].coordinates - molecule[j][jj].coordinates
                                    Qkl = molecule[k][kk].coordinates - molecule[l][ll].coordinates
                                    
                                    Q2ij = np.dot(Qij,Qij)
                                    Q2kl = np.dot(Qkl,Qkl)
                                    
                                    term1 = 2.0*math.pi*math.pi/(pij*pkl)
                                    term2 = math.sqrt(  math.pi/(pij+pkl) )
                                    term3 = math.exp(-qij*Q2ij) 
                                    term4 = math.exp(-qkl*Q2kl)
                                                      
                                    V_ee[i,j,k,l] += N * cicjckcl * term1 * term2 * term3 * term4 * boys(PpijPpkl2/denom,0)  # 3 more                               
                    

    return V_ee           

