import libreria
def pedir_precio1():
    libreria.pedir_numero("ingrese S/.:")
    print("se agrega S/.")

def pedir_cantidad("ingrese kg"):
    libreria.pedir_numero("ingrese kg")

def agregar_cantidad():
    input("agregar cantidad")
    print("se agrega cantidad")

def agregar_precios():
    input("agregar precios")
    print("agregar precios")

def agregar_precio():
    opc=0
    max=4
    while(opc!=max):
        print("#Sub_menu-Precios #")
        print("#1.prec1-> 1.5")
        print("#2.prec2->3.5")
        print("#3.prec3->5.5")
        print("#4.Salir  #")
        print("####################")
       opc=libreria.pedir_numero("ingrese opcion:",1,4)
    if(opc==1):
        pedir_precio1
    if (opc==2):
        pedir_precio2
    if (opc==3):
        pedir_precio3

def agregar_cantidad():
    opc=0
    max=4
    while(opc!= max):
        print("#sub-menu-Cantidad #")
        print("#1.cant1 -> 15 #")
        print("#2.cant2 -> 20 #")
        print("#3.cant3 -> 25#")
        print("####################")
        opc=libreria.pedir_numero("ingrese opcion:",1,3)
    if (opc==1):
       agregar_cant1()
    if(opc==2):
       agregar_cant2()
    if(opc==2):
       agregar_cant3()


opc=0
max=3
    while(opc!=3):
    print("####### MENU ########")
    print("#1.agregar cantidad #")
    print("#2.precio           #")
    print("#salir              #")
    print("#####################")

    opc=libreria.pedir_numero("ingrese opc:" 1,3)

    if(opc==1):
       agregar_cantidad()
    if(opc==2):
       agregar_precio()
print("fin del programa")
#fin_menu
