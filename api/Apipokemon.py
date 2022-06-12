from tkinter import Tk, Label, Button
import tkinter

class Pokedex:

    def __init__(self,master):
        self.master=master
        master.title("Pokedex")
        self.etiqueta=Label(master,text="Buscar Pokemon")
        self.etiqueta.pack()
        master.geometry("400x500")
        self.dato=tkinter.StringVar()
        self.entrada=tkinter.Entry(master,textvariable=self.dato)
        self.entrada.pack()
        self.boton=Button(master,text="Buscar",command=self.salidaTexto)
        self.boton.pack()
        
    def salidaTexto(self):
        print(self.dato.get())
    

root=Tk()
Pokedex(root)
root.mainloop()