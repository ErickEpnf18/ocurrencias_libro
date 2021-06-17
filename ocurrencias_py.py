# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 20:25:07 2021

@author: aguil
#projec ocurremcias de un archivo by Guillermo Erick Andrade
"""

palabras ={}
def iniciarContador():
  archivo= open('dataset/libro.txt', encoding='utf8')
  linea = archivo.readline()
  lineas = linea.split()
  while linea!="":
     for palabraa in lineas:
      if palabraa in palabras:
        x=int(palabras[palabraa])
        palabras[palabraa] = x+1
      else:
        palabras[palabraa]=1
     linea = archivo.readline()
     lineas = linea.split()
  archivo.close()

def imprimir():
  for a in palabras:
      print("( ", end="")
      num = str(palabras[a])
            # print(a+"= "+num)
      texto1 = a.find(",")
      texto_correg = a[0:texto1]
      print(texto_correg, " , {}".format(num), end=" )\n")

iniciarContador()
imprimir()






