from tkinter import DISABLED, PhotoImage, Tk, Label, Button,Text
import tkinter
import urllib.request,urllib.parse,urllib.error
import json
import ssl

from matplotlib.pyplot import text

ctx = ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode= ssl.CERT_NONE

api = "https://pokeapi.co/api/v2/pokemon/"


class Pokedex:

    def __init__(self,master):
        self.abilitiesl=str()
        self.master=master
        master.title("Pokedex")
        master.resizable(width=False, height=False)
        self.etiqueta=Label(master,text="Buscar Pokemon")
        self.etiqueta.place(relx=0.01, rely=0.015)
        master.geometry("400x400")
        self.dato=tkinter.StringVar()
        self.entrada=tkinter.Entry(master,textvariable=self.dato)
        self.entrada.place(relx=0.245, rely=0.015)
        self.boton=Button(master,text="Buscar",command=self.buscar)
        self.boton.place(relx=0.56, rely=0.010)
        
    def buscar(self):
        url=api+self.dato.get()
        url2="https://pokeapi.co/api/v2/pokemon-species/"+self.dato.get()
        print(url)
        try:
            self.request=urllib.request.Request(url)
            self.request.add_header("User-agent","chesse")
            self.datose=urllib.request.urlopen(self.request)
            self.data=self.datose.read().decode()
            self.js=json.loads(self.data)

            self.request=urllib.request.Request(url2)
            self.request.add_header("User-agent","chesse")
            self.datose=urllib.request.urlopen(self.request)
            self.data=self.datose.read().decode()
            self.js2=json.loads(self.data)
            
        except:
            print("Error")
        self.abilitiesl=""
        self.types=""
        self.info=""
        for line in self.js["abilities"]:
            self.abilitiesl=self.abilitiesl+"+"+line["ability"]["name"]+"\n"
        for line1 in self.js["types"]:
            self.types=self.types+"+"+line1["type"]["name"]+"\n"

        for textos in self.js2["flavor_text_entries"]:
            if textos["language"]["name"] == "es":
                self.info=textos["flavor_text"]


        self.imagen=self.js["sprites"]["front_default"]
        self.urlImagen=urllib.request.urlopen(self.imagen,context=ctx)
        file=open("pokemon.png","wb")
        file.write(self.urlImagen.read())
        file.close()
        
        self.habilidadest=Label(self.master,text="Habilidades")
        self.habilidadest.place(relx=0.06, rely=.080)

        self.habilidadest=Label(self.master,text="Tipo/s")
        self.habilidadest.place(relx=0.400, rely=.080)

        self.descripciont=Label(self.master,text="Descripción")
        self.descripciont.place(relx=0.400, rely=.300)


        self.img=PhotoImage(file="pokemon.png")
        self.esim=Label(self.master,image=self.img)
        self.esim.place(relx=0.700, rely=.065)

        self.texto=Text(self.master)
        self.texto.config(width=13, height=3)
        self.texto.insert(tkinter.INSERT,self.abilitiesl)
        self.texto.config(cursor="heart")
        self.texto.config(state=DISABLED)
        self.texto.place(relx=0.065, rely=.120)

        self.tipos=Text(self.master,width=10,height=3,cursor="heart")
        self.tipos.insert(tkinter.INSERT,self.types)
        self.tipos.place(relx=0.400, rely=.120)
        self.tipos.config(state=DISABLED)

        self.descripcion=Text(self.master,cursor="heart")
        self.descripcion.insert(tkinter.INSERT,self.info)
        self.descripcion.place( rely=.400)
        self.descripcion.config(state=DISABLED)


        
        


root=Tk()
Pokedex(root)
root.mainloop()