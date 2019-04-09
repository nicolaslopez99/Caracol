# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
lista=[]
def voltear (m):
    filas = len(m)
    col = len(m[0])
    return [[m[i][j] for i in range(0, filas, 1)] for j in range(col-1, -1, -1)]
def ordenar (m,lista): 
    if not m:
        print("la matriz esta vacia")
        return 0
    lista = lista + m[0]
    m.remove(m[0])
    print(lista)
    m=voltear(m)
    return  ordenar(m,lista),lista

m1=[x.split()for x in open ("C:\\Users\\Antonio\\matriz.txt").readlines()]

ordenar(m1,lista)

