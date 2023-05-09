import numpy as np
import openpyxl

def guardarPesos(matriz,nombre):
  matriz= matriz.tolist()
  workbook = openpyxl.Workbook()
  sheet = workbook.active
  for row in matriz:
    sheet.append(row)
  workbook.save("archivosExcelGuardados/"+nombre+'.xlsx')
  
def guardarUmbrales(matriz,nombre):
  matriz=matriz.tolist()
  workbook = openpyxl.Workbook()
  sheet = workbook.active 
  sheet.append(matriz)
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
matrizp=matrizPesos(entradas, salidas)
print(matrizp)
print("Matriz De umbrales")
matrizu =matrizUmbrales(salidas)
print(matrizu)
guardarPesos(matrizp,"pesos")
guardarUmbrales(matrizu,"Umbrales")

