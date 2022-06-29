import random

tipoDefensa = {
    "agua":random.randint(28,40),
    "fuego":random.randint(30,48),
    "tierra":random.randint(35,50),
    "aire":random.randint(25,36)
}

tipoFuerza ={
    "agua":random.randint(40,68),
    "fuego":random.randint(45,70),
    "tierra":random.randint(45,70),
    "aire":random.randint(40,68)
}

def recorrer(lista,valor):
    for i in lista.items():
        print(i[valor])
        

        
def eleccion(lista):
    eleccion =int (input("agua, presione 1- fuego, presione 2 -tierra, presione 3- aire, presione 4- : "))
    lst= []
    lst.extend(lista.values())
    rest = 0
    for i in lst:
        if eleccion == 1:
            rest = i
        elif eleccion == 2:
            rest = i
        elif eleccion == 3:
            rest = i
        elif eleccion == 4:
            rest = i
        else:
            print("valor incorrecto")
    return rest
        

def boton_inicio():
    print("JUGAR -1")
    print("CREAR Personaje nuevo -2")
    v = int(input("0 para CANCELAR: "))
    return v 
    