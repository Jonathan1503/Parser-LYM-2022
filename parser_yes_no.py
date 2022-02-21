from ast import Str
from lib2to3.pgen2.parse import ParseError
keywords = ["defvar","=","move","turn","face","put","pick","move-dir","run-dirs","mov-face","skip","if","loop","repeat","defun"]
comandcode= ""
variables= {}
orientations=["left","right","around"]
cardinals=["north","south","west","east"]
objects=["balloons","chips"]
directions=["left","front","right","back"]
tokens= []
functions= {}

      
def block():
 if len(tokens) > 0:
    if tokens[0] == "(":
        tokens.remove(tokens[0])
        block()
    elif tokens[0] == "defvar":
        namevar= tokens[1]
        valvar= int(tokens[2])
        newvar(namevar,valvar)
        if tokens[3] != ")":
            raise ParseError("no")
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        block()
    elif tokens[0] == "=":
        var= tokens[1]
        if var not in variables:
            raise ParseError("no")
        else:
            variables[var]=tokens[2]
            if tokens[3] != ")":
                raise ParseError("no")
            tokens.remove(tokens[0])
            tokens.remove(tokens[0])
            tokens.remove(tokens[0])
            tokens.remove(tokens[0])
            block()
    elif tokens[0] == "move":
        if tokens[1] not in variables:
            value= int(tokens[1])
        else:
            pass
        if tokens[2] != ")":
            raise ParseError("no")
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        block()
    elif tokens[0] == "turn":
        if tokens[1] != ":":
            raise ParseError("no")
        if tokens[2] not in orientations:
            raise ParseError("no")
        if tokens[3] != ")":
            raise ParseError("no")
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        block()
    elif tokens[0] == "face":
        if tokens[1] != ":":
            raise ParseError("no")
        if tokens[2] not in cardinals:
            raise ParseError("no")
        if tokens[3] != ")":
            raise ParseError("no")
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        block()
    elif tokens[0] == "put" or tokens[0] == "pick":
        if tokens[1] not in objects:
            raise ParseError("no")
        if tokens[2] not in variables:
            value= int(tokens[2])
        else:
            pass
        if tokens[3] != ")":
            raise ParseError("no")
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        block()
    elif tokens[0] == "move-dir":
         if tokens[1] not in variables:
             value= int(tokens[1])
         else:
             pass
         if tokens[2] != ":":
             raise ParseError("no")
         if tokens[3] not in directions:
             raise ParseError("no")
         if tokens[4] != ")":
             raise ParseError("no")
         tokens.remove(tokens[0])
         tokens.remove(tokens[0])
         tokens.remove(tokens[0])
         tokens.remove(tokens[0])
         tokens.remove(tokens[0])
         block()
    elif tokens[0] == "run-dirs":
        if tokens[1] != "(":
             raise ParseError("no")
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        run()
        if tokens[0] != ")":
             raise ParseError("no")
        tokens.remove(tokens[0])
        block()
    elif tokens[0] == "move-face":
        if tokens[1] not in variables:
             value= int(tokens[1])
        else:
             pass
        if tokens[2] != ":":
             raise ParseError("no")
        if tokens[3] not in cardinals:
             raise ParseError("no")
        if tokens[4] != ")":
             raise ParseError("no")
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        block()
    elif tokens[0] == "skip":
        if tokens[1] != ")":
             raise ParseError("no")
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        block()
    elif tokens[0] == "if" or tokens[0] =="loop":
          tokens.remove(tokens[0])
          ifblock()
          block()

    elif tokens[0] == "repeat":
        if tokens[1] not in variables:
            value= int(tokens[1])
        if tokens[2] != "(":
            raise ParseError("no")
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        ifparser()
        block()
    
    elif tokens[0] == "defun":
        paramlist= []
        name= tokens[1]
        i= 3
        while True:
            
            if tokens[i] == ")":
                break
            paramlist.append(tokens[i])
            i+=1
        newfunction(name,paramlist)
        
        if tokens[2] != "(":
            raise ParseError("no")
        for i in range(0,i+1):
            tokens.remove(tokens[0])
        
        if tokens[0] != "(":
            raise ParseError("no")
        tokens.remove(tokens[0])
        ifparser()
        tokens.remove(tokens[0]) 
        block()
    elif tokens[0] in functions:
        lista= []
        i= 1
        while True:
            if tokens[i] == ")":
                break
            lista.append(tokens[i])
            i+=1
        key= tokens[0]
        paramslist= functions[key]
        if set(lista) != set(paramslist):
            raise ParseError("no")
        for i in range(0,(i+1)):
            tokens.remove(tokens[0])
        block() 
    elif tokens[0]==")":
        pass
       
def newfunction(name:str,params:list):
    functions[name]= params
    

def run():
    counter= 0
    for i in tokens:
        counter +=1
        if i == ")":
            break
        
    for i in range(0,counter):
        if i != (counter-1):
            if tokens[i] != (":") and tokens[i] not in directions:
                raise ParseError("no")
            if tokens[i] == (":"):
                if tokens[i+1] not in directions:
                    raise ParseError("no")
            if tokens[i] in directions:
                if tokens[i+1] != (":"):
                    raise ParseError("no")
        else:
            if tokens[i] not in directions:
                raise ParseError("no")
            if tokens[i+1] != ")":
                raise ParseError("no")
    for i in range(0,(counter+1)):
        tokens.remove(tokens[0])

def ifblock():
    iflist=[]
    if tokens[0] != "(":
        raise ParseError("no")
    tokens.remove(tokens[0])
    if tokens[0] == "facing-p" or tokens[0]=="can-move-p":
        if tokens[1] not in cardinals:
            raise ParseError("no")
        if tokens[2] != ")":
            raise ParseError("no")
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        ifparser()
    elif  tokens[0] == "can-put-p" or tokens[0] == "can-pick-p":
        if tokens[1] not in objects:
            raise ParseError("no")
        if tokens[2] not in variables:
             value= int(tokens[2])
        if tokens[3] != ")":
            raise ParseError("no")
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        ifparser()
    elif tokens[0] == "not":
        if tokens[2] != ")":
            raise ParseError("no")
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        tokens.remove(tokens[0])
        ifparser()


def ifparser():
    global tokens
    iflist=[]
    counteropen= 1
    counterclosed= 0
    position= 0
    for token in tokens:
        if token == ")":
            counterclosed+=1
        elif token == "(":
            counteropen +=1
        if counteropen == counterclosed:
            break
        position +=1
    for i in range(0,(position+1)):
        iflist.append(tokens[i])
        
    
    tokensbackup= tokens.copy()
    tokens= iflist
    block()
    tokens= tokensbackup
    for i in range(0,(position+1)):
        tokens.remove(tokens[0])
        
    
    
    

def newvar(varname:str,varval:int):
    variables[varname]= varval

def archivo(nombre_archivo:str):
    txtfile = open(nombre_archivo, "r")
    
    for linea in txtfile:
    
        global comandcode
        comandcode += " "+linea
    global tokens
    tokens = comandcode.split()     
    if tokens[0] != "(":
        raise ParseError("no")
    else:     
        block()
    

def ejecutar():
    nombre_archivo=input("Ingrese el nombre del archivo: ")
    try:
        archivo(nombre_archivo)
        print("Yes")
    except:
        print("No")


    
    
ejecutar()