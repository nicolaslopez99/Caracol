# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""


def ordenar (m,lista): 
    if m == [['10']]:
        #print("la matriz esta vacia")
        
        return lista.append('10')
    else:
        lista.append(','.join(m[0]))
        m.remove(m[0])
        return  ordenar(voltear(m),lista),lista 
    

def voltear (m):
    filas = len(m)
    col = len(m[0])-1
    return [[m[i][j] for i in range(0, filas, 1)] for j in range(col,-1 , -1)]

m1=[x.split()for x in open ("C:\\Users\\Antonio\\matriz.txt").readlines()]
lista=[]
#print(ordenar(m1,lista))
a= ','.join(ordenar(m1,lista))
print(a)


#
#def ordenar (m,lista): 
##    if m == [['10']]:
 #       #print("la matriz esta vacia")
 #       lista.append('10')
 #       return 0
 #   else:
 #       lista.append(','.join(m[0]))
 #       m.remove(m[0])
#        return  ordenar(voltear(m),lista),lista 
    

##def voltear (m):
 #   filas = len(m)
 #   col = len(m[0])-1
 #   return [[m[i][j] for i in range(0, filas, 1)] for j in range(col,-1 , -1)]

#m1=[x.split()for x in open ("C:\\Users\\Antonio\\matriz.txt").readlines()]
#lista=[]
#print(ordenar(m1,lista))
