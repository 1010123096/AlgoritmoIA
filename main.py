from readXlsx.readData import readData
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw() # Oculta la ventana principal

# Abre una ventana de diálogo para buscar el archivo
file_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Excel files", "*.xlsx")])

# Verifica si se seleccionó un archivo
if file_path:
    # Realiza las operaciones necesarias con el archivo
    print("Se seleccionó el archivo:", file_path)
else:
    print("No se seleccionó ningún archivo")


ruta = file_path

print(readData(ruta))



