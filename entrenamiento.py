import numpy as np
from pesosYUmbrales import matrizUmbrales,matrizPesos

numeroDeIteraciones =int( input("Numero de iteraciones: \n"))
errorMaximoPermitido =float(  input("Error maximo permitido: \n"))
rataDeAprendizaje =float( input("Rata de aprendizaje: \n"))
errorActual = .0
patrones=1
entradas=3
salidas = 2

# # while (errorMaximoPermitido<=errorActual):
# for iteracion in range(1,numeroDeIteraciones+1):
#     print("iteracion: ",iteracion)
#     for patron in range(1,patrones+1):
#         print("patron: ",patron)

#**Patron falso
a = [1,2,3]
#**Salida Falsa
s=[1,2]

#**Comprobar los valores del umbral
u = matrizUmbrales(2)
# print(u)

#**Comprobar los valores de los pesos
w = matrizPesos(3,2)
# print(b)

Yr = np.empty(salidas)
El = np.empty(salidas)
Ep=0

for i in range(0,salidas): 
    aux=0
    print("valor de i:" ,i)
    for j in range(0,entradas):
        print("valor de j:",j)
        print("valor de a[j]:",a[j])
        print("valor de b[i][j]:",w[i][j])
        aux+=(a[j])*(w[i][j])
        print(aux)
    print("umbral : ",i)
    print(u[i])
    print("salida: ",i)
    Yr[i]=aux-u[i]
    print(Yr[i])
    El[i] = s[i]-Yr[i]
    print("error por salida: ",El[i])
    Ep+=El[i]
    print("error: por patron: ",Ep)

Ep/=salidas
print(Yr)
print(El)
print("error: por patron: ",Ep)