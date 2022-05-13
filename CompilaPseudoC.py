
class Variable:
    nombre = ""
    tipo = ""
    valor = ""
    direccion = ""

    def __init__(self, n, t, v, d):
        self.nombre = n
        self.tipo = t
        self.valor = v
        self.direccion=d

Tabla = []


def esSeparador(caracter):
    return caracter in " \n\t"

def esSimboloEsp(caracter):
    return caracter in "+-*;,.:!=%&/()[]{}<><=>=:=^"


def esPalReservada(cad):
    reservadas = ["main", "char", "int", "float", "double", "string", "if", "else", "do", "while", "for", "switch",
                  "short", "long", "extern", "static", "default", "continue", "break", "register", "sizeof", "typedef"]
    return cad in reservadas

def esTipo(cad):
    tipos = ["int", "char", "float", "double","string"]
    return cad in tipos


def esId(cad):
    return (cad[0] in "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")


def quitaComentarios(cad):
    # estados: A, B, C, Z
    estado = "Z"    
    #cad = "a=b/c;"
    cad2 = ""
    for c in cad:
        if (estado == "Z"):
            if (c == "/"):
                estado = "A"
            else:
                cad2 = cad2 + c
        elif (estado == "A"):
            if (c == "*"):
                estado = "B"
            else:
                estado = "Z"
                cad2 = cad2+"/"+c
        elif (estado == "B"):
            if (c == "*"):
                estado = "C"
        elif(estado == "C"):
            if (c == "/"):
                estado = "Z"
            else:
                estado = "B"
    return cad2


def tokeniza(cad):
    tokens = [] #Nuestra lista vacia
    dentro = False #Esta variable nos va indicar si el caracter esta dentro o fuera del token
    token = ""
    for c in cad: 
        if dentro:
            if esSeparador(c):
                tokens.append(token)
                token = ""
                dentro = False
            elif esSimboloEsp(c):
                tokens.append(token)
                tokens.append(c)
                token = ""
                dentro = False
            else:
                token = token + c
        else:
            if esSimboloEsp(c):
                tokens.append(c)
            elif esSeparador(c):
                a=0
            else:
                dentro = True
                token = c
    tokens.append(token)
    return tokens

def muestraTab():
    print("{:^15}{:^15}{:^15}{:^15}".format("Nombre","Tipo","Valor", "Dirección"))
    for v in Tabla:
        print("{:^15}{:^15}{:^15}{:^15}".format(v.nombre, v.tipo, v.valor, ""))

def estaEnTabla(nombreVar):
    esta = False
    for v in Tabla:
        if(v.nombre == nombreVar):
            esta = True
    return esta

def agregaVar(renglon):
    tipos = ["float", "int", "char", "string"]
    datos = tokeniza(renglon)
    print(datos)
    nombreVar = datos[2]
    tipoVar = datos[1]
    if(tipoVar in tipos):   
        if(estaEnTabla(nombreVar)):
            print("La variable", nombreVar, "ya fue declarada")
        else:
            if(len(datos) == 7):
                valorVar = datos[4]
                Tabla.append(Variable(nombreVar, tipoVar, valorVar, ""))
            else:
                Tabla.append(Variable(nombreVar, tipoVar, "0.0", ""))
    else:
        print("Tipo de dato inexistente", tipoVar)


cad = "var float x1;"\
    "var float x2;"\
    "/* coordenadas del 1er punto */"\
    "var float y1;"\
    "var float y2;"\
    "/* coordenadas del 2do punto */"\
    "var float m;"\
    "/* pendiente de la recta */"\
    "print(“escriba el valor de x1: “);"\
    "read(x1);"\
    "print(“escriba el valor de x2: “);"\
    "read(x2);"\
    "print(“escriba el valor de y1: “);"\
    "read(y1);"\
    "print(“escriba el valor de y2: “);"\
    "read(y2);"\
    "m = (y2 – y1) / (x2 – x1);"\
    "print(“la pendiente es: “, m);" \
    "end."


print("programa Original")
print(cad)
cad2=quitaComentarios(cad)
print("")
print("Programa sin Comentarios")
cadSplit = cad2.split(";")
instruciones = []
for a in range(len(cadSplit)):
    cad = cadSplit[a]
    info = tokeniza(cad)
    if(info[0] == "var"):
        agregaVar(cad)
    #elif(info[0] == "print"):
        #imprimir(cad)
    
muestraTab()


"""nombreVar = info[2]
    tipoVar = info[1]
    if(info[0] == "var"):
        Tabla.append(Variable(nombreVar, tipoVar, "0.0", ""))"""

#ciclo while para correr el programa








"""tokens = tokeniza(programa)
#print(programa)
estado = "z"
variables = []
for token in tokens:
    if (estado == "z"):
        if (token == "var"):
            estado = "a"
    elif (estado == "a"):
        if esId(token):
            estado = "b"
            repetido = False
            for v in variables:
                if (v.nombre == token):
                    repetido = True
            if (repetido):
                print("variable redeclarada!!")
                print(token)
                estado = "z"
            else:
                variables.append(Variable(token, "", "",""))

    elif (estado == "b"):
        if (token == ":"):
            estado = "c"
            #print("token:", token, "estado:", estado)
        elif (token == ","):
            estado = "a"
    elif (estado == "c"):
        if esTipo(token):
            estado = "d"
            #print("token:", token, "estado:", estado)
            for v in variables:
                if (v.tipo == ""):
                    v.tipo = token
    elif (estado == "d"):
        if (token == ";"):
            estado = "e"
            #print("token:", token, "estado:", estado)
    elif (estado == "e"):
        if (token == "begin"):
            estado = "z"
            #print("token:", token, "estado:", estado)
            
        elif esId(token):
            estado = "a"
            repetido = False
            for v in variables:
                if (v.nombre == token):
                    repetido = True
            if (repetido):
                print("variable redeclarada!!")
                print(token)
                estado = "z"
            else:
                variables.append(Variable(token, "", "", ""))

for v in variables:
    print(v.nombre, v.tipo, v.valor, v.direccion)"""