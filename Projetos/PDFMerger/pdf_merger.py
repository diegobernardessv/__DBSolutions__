import PyPDF2
import os

mesclador = PyPDF2.PdfMerger()

lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        mesclador.append(f"arquivos/{arquivo}")

mesclador.write("mesclado.pdf")