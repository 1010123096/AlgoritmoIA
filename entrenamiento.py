import numpy as np
from pesosYUmbrales import matrizUmbrales,matrizPesos

numeroDeIteraciones =int( input("Numero de iteraciones: \n"))
errorMaximoPermitido =float(  input("Error maximo permitido: \n"))
rataDeAprendizaje =float( input("Rata de aprendizaje: \n"))
errorActual = .0
patrones=1
entradas=3
salidas = 2
w=matrizPesos()

u=matrizUmbrales()

print(w)
print(u)
matrizSumatoria = np.empty((entradas+1,salidas))


# while (errorMaximoPermitido<=errorActual):
for iteracion in range(1,numeroDeIteraciones+1):
    print("iteracion: ",iteracion)
    for patron in range(1,patrones+1):
        print("patron: ",patron)
        for salida in range(1,salidas+1):    
            print("Salida: ",salida)
            for entrada in range(1,entradas+1):
                print("entrada: ",entrada)
                matrizSumatoria[entrada-1,salida-1]=entrada
                matrizSumatoria[entradas,salida-1]+=entrada
                print(matrizSumatoria)
                
            print("vector--------------")
        print(matrizSumatoria)