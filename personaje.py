import random
from tipos import *

class Personaje:
        nombre = None
        salud = 100
        defensa = None
        fuerza = None
        defenderse = False
        
        def __init__(self,nombre, defensa, fuerza):
            self.nombre= nombre
            self.defensa=defensa
            self.fuerza= fuerza
            
        def __str__(self):
            return self.nombre.upper() 
        
        def __perder_vida(self,daño):
            
            if self.salud == 0 or daño > self.salud:
                print(f"{self.nombre} estas muerto ")
                self.salud= "muerto"
            else:
                self.salud -= daño
        
    
        def atacar(self,enemigo):
            print(f'{self.nombre} ataca a {enemigo.nombre}')
            ataque = self.fuerza + (int(random.randint(1,10)))
            print(ataque)
            if self.defenderse:
                ataque -= 2
            enemigo.calcular_daño_recibido(ataque)
            enemigo.__perder_defensa()
            
        
        def defender(self):
            print(f'{self.nombre} se defiende ahora')
            self.defenderse = True
            print(self.defenderse)
        
        def __perder_defensa(self):
            self.defensa -= 1
            
        def calcular_daño_recibido(self,daño_atacante):
            
            coe_ataque = 0
            if self.defenderse and self.defensa >= 10:
                coe_ataque = daño_atacante - self.defensa - 10 
                print("opcion 1", coe_ataque)
            elif self.defenderse or self.defensa > 10:
                coe_ataque = daño_atacante - self.defensa
                print("opcion 2", coe_ataque)
            elif self.defenderse and self.defensa < 10:
                coe_ataque = daño_atacante -(self.defensa / 2)
            else:
                coe_ataque = daño_atacante
            if coe_ataque < 0:
                coe_ataque = 0
            self.__perder_vida(coe_ataque)

        def mostrar_estadistica(self):
            print(f'{self.nombre} - {self.salud} - {self.defensa} - {self.fuerza}')

listaPersonaje=[]

medusa = Personaje("medusa",(random.randint(25,45)), 47)
centauro = Personaje("centauro",(random.randint(25,45)),47 )
listaPersonaje.append(medusa)
listaPersonaje.append(centauro)


def lista_personaje():
    for i in listaPersonaje:
        print (i)

def crear_personaje():
    nombre= input("que nombre le quieres colocar a tu personaje: ")
    print("Seleccione el tipo de Defensa")
    defensa= eleccion(tipoDefensa)
    print("Seleccione el tipo de Fuerza")
    fuerza= eleccion(tipoFuerza)
    pj= Personaje(nombre,defensa,fuerza)
    listaPersonaje.append(pj)
    print("personaje creado y argregado a la lista")
    lista_personaje()
    
def elegir_personaje():
    cont = 1
    for i in listaPersonaje:
        print("Presione ", cont ," para ", i.nombre.upper())
        cont += 1 
    h = int(input("elija: "))- 1
    for e in listaPersonaje:
        pj = listaPersonaje[h]
    print("personaje elejido", pj)
    return pj

def pelea(x,y):
    ban = True
    cam= 1
    while ban:
        if cam == 1:
            print(x.nombre.upper(), "elige")
            jugada(x,y)
            cam = 0
        else:
            print(y.nombre.upper(), "elige")
            jugada(y,x)
            cam +=1
        if x.salud == "muerto":
            print(x.nombre.upper(), "ha perdido")
            print(y.nombre.upper(), "GANADOR")
            ban = False
        elif y.salud == "muerto":
            print(y.nombre.upper(), "ha perdido")
            print(x.nombre.upper(), "GANADOR")
            ban = False
        
    
def jugada(pjE,pjR):
    ele =int(input( "elejir su jugada- 1 atacar ,2- defenderse: "))
    if ele == 1:
        pjE.atacar(pjR)
    elif ele == 2:
        pjE.defender()
    pjE.mostrar_estadistica()
    pjR.mostrar_estadistica()


print("STREETBOX IEN")
cond = True
while cond:
    elec = boton_inicio()
    if elec == 1:
        lista_personaje()
        print("Elejir personaje 1")
        pj1= elegir_personaje()
        print("Elejir personaje 2")
        pj2= elegir_personaje()
        print("Fight")
        pelea(pj1,pj2)
    elif elec == 2:
        crear_personaje()
    elif elec== 0:
        cond = False
        print("Nos Vemos")
        
