# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

def ordenar (m,lista): 
    if m == [['10']]:
        return lista.append('10')
    else:
        (','.join(m[0]))
        hacer(lista,m)
        return  lista 
def voltear (m):
    return [[m[i][j] for i in range(0, len(m), 1)] for j in range(len(m[0])-1,-1 , -1)]
def hacer (lista,m):
    lista.append(','.join(m[0]))
    m.remove(m[0])
    return  ordenar(voltear(m),lista) 
lista=[]
ordenar([x.split()for x in open ("C:\\Users\\Antonio\\matriz.txt").readlines()],lista)
print(','.join(lista))
