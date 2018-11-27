#Universidad de las Fuerzas Armadas ESPE
#Desarrollado por Memo Casanova, Alan Quimbita y Joyce Castro
#Fecha de Creación 09/11/2018
#Fecha de Modificación 16/11/2018

from tkinter import *
from tkinter import messagebox
from Sorter import Sorter
from Ploter import Ploter
from time import clock

class Window():
    def __init__(self, title):
        self.ploter=Ploter()
        self.sorter=Sorter()
        self.window=Tk()    
        self.window.geometry("400x300")
        self.window.config(bg="white")
        self.window.title(title)
        self.window.iconbitmap("icono.ico")
        self.window.resizable(False,False)
        self.mainFrame=Frame(self.window, width=400, height=300, bg="white")
        self.lblNumElements=Label(self.mainFrame, text="Número de elementos", bg="white")
        self.lblNumElements.place(x=10,y=20)
        self.lblNumCicles=Label(self.mainFrame, text="Número de pasadas", bg="white")
        self.lblNumCicles.place(x=10,y=50)
        self.lblDataRange=Label(self.mainFrame, text="Rango de datos", bg="white")
        self.lblDataRange.place(x=10,y=80)
        self.txtNumElements=Entry(self.mainFrame, width=20)
        self.txtNumElements.place(x=150, y=20)
        self.txtNumCicles=Entry(self.mainFrame, width=20)
        self.txtNumCicles.place(x=150, y=50)
        self.txtMinData=Entry(self.mainFrame, width=15)
        self.txtMinData.place(x=150, y=80)
        self.txtMaxData=Entry(self.mainFrame, width=15)
        self.txtMaxData.place(x=250, y=80)
        self.btnRadix=Button(self.mainFrame, command=self.runRadix, text="Radix", height=2, width=52)
        self.btnRadix.place(x=10, y=150)
        self.btnMerge=Button(self.mainFrame, command=self.runMerge, text="Intercalación Directa", height=2, width=52)
        self.btnMerge.place(x=10, y=200)
        self.btnGeneralTest=Button(self.mainFrame, command=self.generalTest, text="Testeo General", height=2, width=52)
        self.btnGeneralTest.place(x=10, y=250)       
        self.mainFrame.pack()
        self.window.mainloop()  
        
    def runRadix(self):
        try:
            if(int(self.txtMinData.get())>=int(self.txtMaxData.get())): messagebox.showerror("Error", "El limite inferior debe ser menor al superior")
            elif int(self.txtNumElements.get())<=0: messagebox.showerror("Error", "El Número de elementos debe ser positivo")
            elif int(self.txtNumCicles.get())<=0: messagebox.showerror("Error", "El Número de pasadas debe ser positivo")
            else:
                arrays=list(self.sorter.generateList(int(self.txtNumElements.get()), int(self.txtMinData.get()), int(self.txtMaxData.get())) for i in range(int(self.txtNumCicles.get())))
                orderedList=list()
                Otime=clock()
                for i in arrays:
                    orderedList=self.sorter.radixSort(i)
                currentTime=(clock()-Otime)*1000
                if currentTime==0: currentTime=0.01
                self.ploter.plot(int(self.txtNumElements.get()), arrays[int(self.txtNumCicles.get())-1], "Lista desordenada")
                messagebox.showinfo("Resultados", "El tiempo de ejecución fue: " + str(currentTime)[:5] + "ms")
                self.ploter.clean()
                self.ploter.plot(int(self.txtNumElements.get()), orderedList, "Lista ordenada")
        except:
           messagebox.showerror("Error", "La entrada no es correcta")

    def runMerge(self):
        try:
            if(int(self.txtMinData.get())>=int(self.txtMaxData.get())): messagebox.showerror("Error", "El limite inferior debe ser menor al superior")
            elif int(self.txtNumElements.get())<=0: messagebox.showerror("Error", "El Número de elementos debe ser positivo")
            elif int(self.txtNumCicles.get())<=0: messagebox.showerror("Error", "El Número de pasadas debe ser positivo")
            else:
                arrays=list(self.sorter.generateList(int(self.txtNumElements.get()), int(self.txtMinData.get()), int(self.txtMaxData.get())) for i in range(int(self.txtNumCicles.get())))
                orderedList=list()
                Otime=clock()
                for i in arrays:
                    orderedList=self.sorter.mergeSort(i)
                currentTime=(clock()-Otime)*1000
                if currentTime==0: currentTime=0.01
                self.ploter.plot(int(self.txtNumElements.get()), arrays[int(self.txtNumCicles.get())-1], "Lista desordenada")
                messagebox.showinfo("Resultados", "El tiempo de ejecución fue: " + str(currentTime)[:5] + "ms")
                self.ploter.clean()
                self.ploter.plot(int(self.txtNumElements.get()), orderedList, "Lista ordenada")
        except:
           messagebox.showerror("Error", "La entrada no es correcta")

    def generalTest(self):
        try:
            if(int(self.txtMinData.get())>=int(self.txtMaxData.get())): messagebox.showerror("Error", "El limite inferior debe ser menor al superior")
            elif int(self.txtNumElements.get())<=0: messagebox.showerror("Error", "El Número de elementos debe ser positivo")
            elif int(self.txtNumCicles.get())<=0: messagebox.showerror("Error", "El Número de pasadas debe ser positivo")
            else:
                arraysA=list(self.sorter.generateList(int(self.txtNumElements.get()), int(self.txtMinData.get()), int(self.txtMaxData.get())) for i in range(int(self.txtNumCicles.get())))
                arraysB=list(self.sorter.generateList(int(self.txtNumElements.get()), int(self.txtMinData.get()), int(self.txtMaxData.get())) for i in range(int(self.txtNumCicles.get())))
                orderedList=list()
                Otime=clock()
                for i in arraysA:
                    orderedList=self.sorter.radixSort(i)
                currentTime=(clock()-Otime)*1000
                if currentTime==0: currentTime=0.01
                messageA="Tiempo Radix: " + str(currentTime)[:5] + "ms"
                Otime=clock()
                for i in arraysB:
                    orderedList=self.sorter.mergeSort(i)
                currentTime=(clock()-Otime)*1000
                if currentTime==0: currentTime=0.01
                messageA+="\nTiempo Intercalación Directa: " + str(currentTime)[:5] + "ms"
                messagebox.showinfo("Resultados", messageA)
        except:
            messagebox.showerror("Error", "La entrada no es correcta")