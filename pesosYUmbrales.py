import numpy as np




def matrizPesos(entradas,salidas):
    matrizPesos = np.random.uniform(low=-1, high=1, size=(entradas,salidas))
    matrizPesos = np.round(matrizPesos,decimals=2)
    return matrizPesos

def matrizUmbrales(salidas):
    matrizUmbrales = np.random.uniform(low=-1, high=1, size=(salidas))
    matrizUmbrales = np.round(matrizUmbrales,decimals=2)
    return matrizUmbrales



print("Matriz De peso")

entradas= int(input("Entradas: \n"))
salidas= int(input("Salidas: \n"))

print(matrizPesos(entradas,salidas))
print("Matriz De umbrales")

print(matrizUmbrales(salidas))


