#Universidad de las Fuerzas Armadas ESPE
#Desarrollado por Memo Casanova, Alan Quimbita y Joyce Castro
#Fecha de Creación 09/11/2018
#Fecha de Modificación 16/11/2018

import matplotlib.pyplot
from time import sleep

class Ploter():
    def __init__(self):
        self.ploter=matplotlib.pyplot
       
    def plot(self, numElements, values, title):
        self.ploter.xlabel("Posición en la lista")
        self.ploter.ylabel("Valor")
        self.ploter.title(title)
        self.ploter.bar(list(range(numElements)), values, 0.1)
        self.ploter.show(block=False)

    def clean(self):
        self.ploter.clf()
        

        



