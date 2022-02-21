from ast import Str
from sqlalchemy import null
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

def defvar(name: str, n: int):
    name = str(int)
    keywords[name]=str(int)

def igual(name: str, n: int):
    name=str(int)
    keywords[name]=str(int)

def move(n: int):
    return None

def turn(d: str):
    esCorrecto=False
    if d==":left" or d==":right" or d==":around":
        esCorrecto=True
    else:
        esCorrecto
    return esCorrecto

def face(o: str):
    esCorrecto=False
    if o==":north" or o==":south" or o==":east" or o==":west":
        esCorrecto=True
    else:
        esCorrecto
    return esCorrecto
        
def put (x: str, n: int):
    esCorrecto=False
    final=False
    if x=="balloons" or x=="chips":
        esCorrecto=True
    else: 
        esCorrecto=False
    if esCorrecto==False:
        final
    else:
        final=True
    return final

def pick (x: str, n: int):
    esCorrecto=False
    final=False
    if x=="balloons" or x=="chips":
        esCorrecto=True
    else: 
        esCorrecto=False
    if esCorrecto==False:
        final
    else:
        final=True

def move_dir(n: int, d: str):
    esCorrecto=False
    if d==":front" or d==":right" or d==":left" or d==":back":
        esCorrecto=True
    else:
        esCorrecto
    return esCorrecto

def run_dirs(d: list):
    d=[]
    esCorrecto=False
    if ":front" in d or ":right" in d or ":left" in d or ":back" in d:
        esCorrecto=True
    elif len(d)==0:
        esCorrecto
    else:
        esCorrecto
    return esCorrecto

def move_face(n: int, o: str):
    esCorrecto=False
    if o==":north" or o==":south" or o==":east" or o==":west":
        esCorrecto=True
    else:
        esCorrecto
    return esCorrecto

def skip():
    return None
#----------------------------Control structures-------------------------

def conditional(condition: str, block1: str, block2: str):
    respuesta=None
    if condition not in conditional:
        respuesta
    if condition==True:
        respuesta = block1
    else:
        respuesta=block2
    return respuesta

def loop(condition: str, block: str):
    while condition==True:
        return block
        
def repeat(n: int, block: str):
    while n>0:
        block
        n-=1
    return block

def defun(name: str, params: str, block: str):
    def name(params):
        block

#--------------------------Conditions------------------------------------

conditions=[face, put, pick, move, (not face), (not put), (not pick), (not move)]

    

















    
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