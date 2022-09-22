# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:54:43 2022

@author: pablo
"""

import numpy as np 
x,y,z= 1,1,9 #INDICAR EL NÚMERO DE CELDAS EN CADA DIRECCIÓN
dimension=[x,y,z]
vacio=13/0.529177
ejes=np.array([6.8862,6.8862,1.45856*6.8862])
ejes_ang=np.array([6.8862,6.8862,1.45856*6.8862])*0.529177
celldm_3=(1.45856*6.8862*z+vacio)/ejes[0]
pos=np.array([[0.000, 0.000, 0.000],
              [1.822, 1.822, 2.6575],
              [0.000, 1.822, 1.62639],
              [0.000, 1.822, 4.28389],
              [1.822, 0.000, 1.031],
              [1.822, 0.000, 3.826]])

posiciones=[]
for i in range(x):
    for k in range(y):
        for l in range(z):
            for j in range(len(pos)):
                dim=[i,k,l]
                posiciones.append(pos[j]+dim*ejes_ang)
                np.array(posiciones)
n=len(posiciones)
print('El número de átomos es ' + str(n+1))
print('El número de bandas es ' + str((n+1)*8))
print('Nuevos ejes ' + str(dimension*ejes))
print('celldm(1)= ' + str(ejes[0]) + ' y celldm(3)= ' + str(np.round(celldm_3,5)))
print(pos)
np.savetxt("Pos2z.txt", np.round(posiciones,5), fmt="%s")