import libreria
def pedir_laptop():
    libreria.pedir_nombre("ingrese laptop:")
    print("se agrega laptop")
def pedir_celular():
    print("se agrega celular")
def pedir_impresora():
    print("se agrega impresora")

def pedir_nro_cuenta():
    libreria.pedir_numero("ingrese nro_cuenta")
    print("agregar nro_cuenta")


def pedir_precio():
    libreria.pedir_numero("ingrese precio")
    print("agregar precio")


def agregar_producto():
    opc=0
    max=4
    while(opc!=max):
        print("#### MENU PRODUCTO #####")
        print("#1.laptop     #")
        print("#2.celular    #")
        print("#3.impresora  #")
        print("#4.salir      #")
        print("#####################")
 opc=libreria.pedir_numero(''ingrese opc:'' 1,4)
   if (opc==1):
       agregar_laptop()
   if(opc==2):
       agregar_celular()
   if(opc==3):
       agregar_impresora()

def agregar_dni():
    opc=0
    max=2
    while(opc!=max):
        print("#### MENU PRODUCTO #####")
        print("#1.nro cuenta >= 16    #")
        print("#2.salir               #")
        print("#####################")
 opc=libreria.pedir_numero("ingrese opcion",1,2)
   if (opc==1):
       agregar_nro_cuenta()


def agregar_precio():
v    opc=0
    max=4
    while(opc!=max):
        print("#### MENU PRECIOS #####")
        print("#1.prec1 >= 2500    #")
        print("#2.prec2 >= 1000    #")
        print("#3.prec3 >= 900     #")
        print("#4.salir              #")
        print("#####################")
 opc=libreria.pedir_numero("ingrese opcion",1,4)
   if (opc==1):
       agregar_prec1()
   if(opc==2):
       agregar_prec2()
   if(opc==3):
       agregar_prec3()

opc=0
max=3
    while(opc!=3):
    print("####### MENU ########")
    print("#1.producto         #")
    print("#2.nro cuenta       #")
    print("#3.precio           #")
    print("#4.salir            #")
    print("#####################")

6opc=libreria.pedir_numero("ingrese opc:" 1,4)
    if(opc==1):
       agregar_producto()
    if(opc==2):
       agregar_nro_cuenta()
    if(opc==3):
        agregar_dni()

print(''fin del programa'')
#fin_menu
