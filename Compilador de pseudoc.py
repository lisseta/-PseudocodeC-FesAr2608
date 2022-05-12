
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



def quitaComentarios(cad):   # Quita Comentarios correcto

    
 estado = "Z"

 # Aqui se recibe el codigo para quitar comentarios
 cadComentado = "main(){ /*inicio*/ \n int a;  /*se declara a*/"  #Eliminar esta cuando ya reciba  el codigo

 cadSinComentar = ""

 for c in cadComentado:
    if (estado == "Z"):
        if (c == "/"):
            estado = "A"
        else:
            cadSinComentar = cadSinComentar + c
    elif (estado == "A"):
        if (c == "*"):
            estado = "B"
        else:
            estado = "Z"
            cadSinComentar = cadSinComentar+"/"+c
    elif (estado == "B"):
        if (c == "*"):
            estado = "C"
    elif(estado == "C"):
        if (c == "/"):
            estado = "Z"
        else:
            estado = "B"
            
    #print(cadSinComentar)

 return cadSinComentar


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
