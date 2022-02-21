from ast import Str
keywords = ["defvar","=","move","turn","face","put","pick","move-dir","run-dirs","mov-face","skip","if","loop","repeat","defun"]
error= False
def parser(code:str): 
    tokens= code.split() 
    for token in tokens:
        if token == "(":
            tokens2 =tokens.copy()
            tokens2.remove(token)
            block(tokens2)
       
def block(tokens:list):
    counter=0
    for token in tokens:
        if token == "(":
            tokens2 =tokens.copy()
            tokens2.remove(token)
            block(tokens2)
        if token not in keywords:
            global error
            error= True
        if token == "defvar":
            defvar= True
            tempvar= token
            continue

    
def archivo(nombre_archivo:str):
    txtfile = open(nombre_archivo, "r")
    comandcode=""
    for linea in txtfile:
       comandcode += " "+linea
    if comandcode[0] != "(":
        global error
        error= True
    else:
        parser(comandcode)
    

def ejecutar():
    nombre_archivo=input("Ingrese el nombre del archivo: ")
    try:
        archivo(nombre_archivo)
        print("Yes")
    except:
            print("No")
    
ejecutar()