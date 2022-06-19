from tkinter import Tk, Label, Button
import tkinter
import urllib.request,urllib.parse,urllib.error
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode= ssl.CERT_NONE

api = "https://pokeapi.co/api/v2/pokemon/"


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
        self.boton=Button(master,text="Buscar",command=self.buscar)
        self.boton.pack()
        
    def buscar(self):
        url=api+self.dato.get()
        print(url)

        self.web=urllib.request.urlopen(url)
        self.datos=self.web.read().decode()
        print('Retrieved', len(self.datos), 'characters')


root=Tk()
Pokedex(root)
root.mainloop()