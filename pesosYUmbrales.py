import numpy as np
import openpyxl

def guardarPesos(matriz,nombre):
  workbook = openpyxl.Workbook()
  sheet = workbook.active
  for row in matriz:
    sheet.append(row)
  workbook.save("archivosExcelGuardados/"+nombre+'.xlsx')
  
def guardarUmbrales(x,nombre):
  workbook = openpyxl.Workbook()
  sheet = workbook.active 
  sheet.append(x)
  workbook.save("archivosExcelGuardados/"+nombre+'.xlsx')
  

def matrizPesos(entradas, salidas):
    matrizPesos = np.random.uniform(low=-1, high=1, size=(entradas, salidas))
    matrizPesos = np.round(matrizPesos, decimals=2)
    return matrizPesos


def matrizUmbrales(salidas):
    matrizUmbrales = np.random.uniform(low=-1, high=1, size=(salidas))
    matrizUmbrales = np.round(matrizUmbrales, decimals=2)
    return matrizUmbrales


print("Matriz De peso")

entradas = int(input("Entradas: \n"))
salidas = int(input("Salidas: \n"))
mp=matrizPesos(entradas, salidas)
matrizp=mp.tolist()
print(matrizp)
print("Matriz De umbrales")
mu =matrizUmbrales(salidas)
matrizu=mu.tolist()
print(matrizu)
guardarPesos(matrizp,"pesos")
guardarUmbrales(matrizu,"Umbrales")

