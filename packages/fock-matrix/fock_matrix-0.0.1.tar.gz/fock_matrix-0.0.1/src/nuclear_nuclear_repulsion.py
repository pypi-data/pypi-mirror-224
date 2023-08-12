import sys
import numpy as np
from scipy import special
import math

def nuclear_nuclear_repulsion(molecule,zlist,atom_coordinates):
    natoms=len(zlist)
    E_NN=0
    for i in range(natoms):
        zi =zlist[i]
        for j in range(natoms):
            if j>i:
                zj=zlist[j]
                Rijx= atom_coordinates[i][0]-atom_coordinates[j][0]
                Rijy= atom_coordinates[i][1]-atom_coordinates[j][1]
                Rijz= atom_coordinates[i][2]-atom_coordinates[j][2]

                sq_Rijx=Rijx*Rijx
                sq_Rijy=Rijy*Rijy
                sq_Rijz=Rijz*Rijz
                dij= math.sqrt(sq_Rijx+sq_Rijy+sq_Rijz)
                E_NN += zi*zj/dij

    return E_NN

