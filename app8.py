import libreria
def pedir_plantas():
    libreria.pedir_nombre("ingrese zapote:")
    print("se agrega zapote:")
def pedir_eucalipto():
    print("se agrega eucalipto")
def pedir_molle():
    print("se agrega molle")

def pedir_cantidad():
    libreria.pedir_numero("ingresar cantidad")
    print("cantidad")
def pedir_():
    print("se agrego cantidad2")


def agregar_plantas():
    input("agregar plantas")
    print("se agrega plantas)

def agregar_cantidad():
    opc=0
    max=3
    while(opc!=max):
        print("#### CANTIDAD ####")
        print("#1. Kg           #")
        print("#2. Ramos        #")
        print("#3. salir        #")
        print("##################")
        opc=libreria.pedir_numero("ingrese cantidad:",1,3)
        if(opc==1):
            pass
        if(opc==2):
            pass


opc=0
max=3
while(opc!=max):
    print("#### INVENTARIO ####")
    print("#1. plantas   #")
    print("#2.cantidad   #")
    print("#3.salir      #")
    opc=libreria.pedir_numero(''ingrese opc:'' 1,3)
    if (opc==1):
        agregar_plantas()
    if(opc==2):
        agregar_cantidad()
print("fin del programa")
#fin_menu
