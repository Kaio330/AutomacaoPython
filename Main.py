import os
from datetime import datetime
from openpyxl import Workbook
from CriaObjetos import CriaObjetos, extrair_texto

directory = 'Pdfs'
files = os.listdir(directory)
files_quantity = len(files)

wb = Workbook()

for file in files:
    pdf_texto = extrair_texto(directory + '/' + file)
    nota = CriaObjetos(pdf_texto)
    nota.adicionarExcel(wb)
    del nota

full_now = str(datetime.now()).replace(':', '_')
dot_index = full_now.index('.')
now = full_now[:dot_index]

wb.save('Planilha preenchida '+ now +'.xlsx')

