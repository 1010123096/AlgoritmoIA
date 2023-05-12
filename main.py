from readXlsx.readData import readData
import tkinter as tk
from tkinter import filedialog
from pesosYUmbrales import matrizUmbrales,matrizPesos,guardarPesos,guardarUmbrales,readDataExcel,readDataExcel2

root = tk.Tk()
root.withdraw()  # Oculta la ventana principal

def AbrirDocumento():
    # Abre una ventana de diálogo para buscar el archivo
    file_path = filedialog.askopenfilename(
        title="Seleccionar archivo", filetypes=[("Excel files", "*.xlsx")])

# Verifica si se seleccionó un archivo
    if file_path:
    # Realiza las operaciones necesarias con el archivo
        print("Se seleccionó el archivo:", file_path)
        return file_path
    else:
        print("No se seleccionó ningún archivo")
    



#**Carga archivo
ruta = AbrirDocumento()
#**Asigna todos los datos leidos del archivo
entrada, salida, patron, matrizEntrada, matrizSalida = readData(ruta)
# print(entrada, salida, patron)
# print("////////////////////////////////////")
# print(matrizEntrada)
# print("////////////////////////////////////")
# print(matrizSalida)

#**Se escoge la red la funcion de activacion y la de entrenamiento
red =0
funcionDeActivacion=""
algoritmoDeEntrenamiento="Regla Delta"
while(red==0):
    red = int(input("Digite 1 para Percetron 2 para Adaline: \n"))
    
if(red == 1):
    red = "PERCETRON"
    funcionDeActivacion="Escalon"
else:
    red = "ADALINE"
    funcionDeActivacion="Lineal"
        
print(red)
print(funcionDeActivacion)

#**Carga los pesos y umbrales funciones de llamado
# w = readDataExcel2(AbrirDocumento())
# print(w)
# u = readDataExcel(AbrirDocumento())
# print(u)



#**Se genera la matriz de peso aleatoriamente
w= matrizPesos(entrada,salida)
guardarPesos(w,"Pesos")
# print(w)
#**Se genera el vector de umbrales aleatoriamente
u= matrizUmbrales(salida)
# print(u)
guardarUmbrales(u,"Umbrales")

