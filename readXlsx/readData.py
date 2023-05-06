import openpyxl
from tabulate import tabulate

excel_dataframe = openpyxl.load_workbook("pruebasubirArchivos.xlsx")
dataframe = excel_dataframe.active

print(dataframe)
