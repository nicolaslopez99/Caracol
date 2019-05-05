# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

def ordenar (m): 
    if m == [['10']]:
        return '10'
    else:       
        return  leer(m)+" "+ordenar(hacer(m))
def voltear (m):
    return [[m[i][j] for i in range(0, len(m), 1)] for j in range(len(m[0])-1,-1 , -1)]
def hacer (m):
    m.remove(m[0])
    return  voltear(m)
def leer(m):
    return ' '.join(m[0])
print(ordenar([x.split()for x in open ("C:\\Users\\Antonio\\matriz.txt").readlines()]))
