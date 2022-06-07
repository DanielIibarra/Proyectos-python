from symtable import Symbol


def sumasresta(lista,boleano=False):
    sep = list()
    if len(lista) > 5:
        print("Error: Too many problems.")
    else:
        sep = list()
        for operacion in lista:
            sep = sep + operacion.split()
        if len(lista) == 1:
            print("",sep[0])
            print(sep[1],sep[2])
            print("----  ")
            if boleano==True:
                if sep[1] != "+" and sep[1]!="-":
                    print("Error: Operator must be '+' or '-'.")
                else:
                    print("",eval(lista[0]))

        elif len(lista) == 2:
            print(" ",sep[0],"    ",sep[3],)
            print(sep[1],sep[2],"    ",sep[4],sep[5])
            print("----    ","----    ")
            if boleano==True:
                if sep[1] != "+" and sep[1]!="-" or sep[4] != "+" and sep[4]!="-":
                    print("Error: Operator must be '+' or '-'.")
                else:    
                    print("",eval(lista[0]),"     ",eval(lista[1]))

        elif len(lista) == 3:
            print("",sep[0],"    ",sep[3],"    ",sep[6])
            print(sep[1],sep[2],"   ",sep[4],sep[5],"   ",sep[7],sep[8])
            print("----   ","----   ","----   ")
            if boleano==True:
                if sep[1] != "+" and sep[1]!="-" or sep[4] != "+" and sep[4]!="-" or sep[7] != "+" and sep[7]!="-":
                    print("Error: Operator must be '+' or '-'.")
                else:    
                    print("",eval(lista[0]),"     ",eval(lista[1]),"    ",eval(lista[2]))

        elif len(lista) == 4:
            print("",sep[0],"    ",sep[3],"    ",sep[6],"    ",sep[9])
            print(sep[1],sep[2],"   ",sep[4],sep[5],"   ",sep[7],sep[8],"   ",sep[10],sep[11])
            print("----   ","----   ","----   ","----   ")
            if boleano==True:
                if sep[1] != "+" and sep[1]!="-" or sep[4] != "+" and sep[4]!="-" or sep[7] != "+" and sep[7]!="-" or sep[10]!="-" and sep[10] != "+":
                    print("Error: Operator must be '+' or '-'.")
                else:    
                    print("",eval(lista[0]),"     ",eval(lista[1]),"    ",eval(lista[2]),"    ",eval(lista[3]))
            
        else:
            print("",sep[0],"   ","",sep[3],"  ","",sep[6],"  ","",sep[9],"  ","",sep[12],"  ",)
            print(sep[1],sep[2],"   ",sep[4],sep[5],"  ",sep[7],sep[8],"  ",sep[10],sep[11]," ",sep[13],sep[14])
            print("----  ","----   ","----  ","----  ","---- ")
            if boleano==True:
                if sep[1] != "+" and sep[1]!="-" or sep[4] != "+" and sep[4]!="-" or sep[7] != "+" and sep[7]!="-" or sep[10]!="-" and sep[10] != "+" or sep[13]!="-" and sep[13] != "+":
                    print("Error: Operator must be '+' or '-'.")
                else:    
                    print("",eval(lista[0]),"    ",eval(lista[1]),"    ",eval(lista[2]),"    ",eval(lista[3]),"   ",eval(lista[4]))
