
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


def esSeparador(c):
    separadores = "\n\t "
    return c in separadores


def esSimboloEsp(c):
    especiales = "¡#$%&/*+-=:;[]{}(),"
    return c in especiales


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
    tokens = []
    dentro = False
    token = ""
    for c in cad:
        if dentro:  # esta dentro del token
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
        else:  # esta fuera del token
            if esSimboloEsp(c):
                tokens.append(c)
            elif esSeparador(c):
                a = 0
            else:
                dentro = True
                token = c
    return tokens


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
print(cad2)

programa=cad2

tokens = tokeniza(programa)
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
    print(v.nombre, v.tipo, v.valor, v.direccion)
