from overlap import overlap
from primitive_gaussian import primitive_gaussian
from electron_electron_repulsion import electron_electron_repulsion
from electron_nuclear_attraction import electron_nuclear_attraction
from nuclear_nuclear_repulsion import nuclear_nuclear_repulsion
from kinetic import kinetic

# from hf import overlap
# from hf import primitive_gaussian
# from hf import electron_electron_repulsion
# from hf import electron_nuclear_attraction
# from hf import nuclear_nuclear_repulsion
# from hf import kinetic
import sys
import numpy as np
from scipy import special
import math

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

print("\n STO-3G basis for H2:")
print("overlap matrix: \n",np.array(overlap(molecule)))
print("Kinetic Matrix: \n", kinetic(molecule))
print("electron_nuclear_ attraction matrix \n"  , electron_nuclear_attraction(molecule,atom_coordinates,z))
print("electron_electron \n ", electron_electron_repulsion(molecule))
print("nuclear_nuclear replusion \n ",nuclear_nuclear_repulsion(molecule,z,atom_coordinates))
print("\n")
print("FOCK MATRIX:  ")
print(overlap(molecule)+ kinetic(molecule)+  electron_nuclear_attraction(molecule,atom_coordinates,z) + electron_electron_repulsion(molecule) + nuclear_nuclear_repulsion(molecule,z,atom_coordinates))

#create many H2 molecules with various distances for one of the H

# distances= [round(i*0.1,3) for i in range(10,33)] # disntance in Bhor -- au 
# molecule_coordinates=[[[0,0,0],[distance,0,0]] for distance in distances]
# print(molecule_coordinates)
# print(distances)
# for molecule_coordinate in molecule_coordinates:
#     #create a H2 molecule with STO-3G basis set
    
#     H1_pg1a= primitive_gaussian(0.3425250914E+01, 0.1543289673E+00,molecule_coordinate[0],0,0,0)
#     H1_pg1b= primitive_gaussian(0.6239137298E+00 ,0.5353281423E+00,molecule_coordinate[0],0,0,0)
#     H1_pg1c= primitive_gaussian( 0.1688554040E+00,0.4446345422E+00,molecule_coordinate[0],0,0,0)

#     H2_pg1a= primitive_gaussian(0.3425250914E+01, 0.1543289673E+00,molecule_coordinate[1],0,0,0)
#     H2_pg1b= primitive_gaussian(0.6239137298E+00 ,0.5353281423E+00,molecule_coordinate[1],0,0,0)
#     H2_pg1c= primitive_gaussian( 0.1688554040E+00,0.4446345422E+00,molecule_coordinate[1],0,0,0)
    
    
#     H1_1s=[H1_pg1a,H1_pg1b,H1_pg1c]
#     H2_1s=[H2_pg1a,H2_pg1b,H2_pg1c]
#     z=[1.0,1.0]
#     atom_coordinates= [np.array(molecule_coordinate[0]),np.array(molecule_coordinate[1])]
#     molecule=[H1_1s,H2_1s]
#     #print("\n STO-3G basis for H2: with positon coordinates {0}{1}".format(molecule_coordinate[0],molecule_coordinate[1]))

#     #print("overlap matrix: \n",overlap(molecule))
#     #print("Kinetic Matrix: \n", kinetic(molecule))
#     #print("electron_nuclear_ attraction matrix \n"  , eletron_nuclear_attraction(molecule,atom_coordinates,z))

# #     print("electron_electron \n ", electron_electron_repulsion(molecule))


# #     print("nuclear_nuclear replusion \n ",nuclear_nuclear_repulsion(molecule,z,atom_coordinates))
# #     print("\n")
# #     print("\n")

#     S=overlap(molecule)
#     T= kinetic(molecule)
#     Vne= electron_nuclear_attraction(molecule,atom_coordinates,z)
#STO-3G
