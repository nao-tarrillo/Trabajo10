import libreria
def pedir_nombre_restaurante():
    libreria.pedir_nombre("agregar Blue garden:")
    print ("agrega Blue garden:")
def pedir_El_sagitario():
    print("agregar El sagitario:")
def pedir_El_paisa():
    print("agregar El paisa:")
def pedir_El_comedor():
    print("agregar El paisa")

def pedir_platos():
    libreria.pedir_nombre("agregar chupe de camarones")
    print("se agrega chupe de camarones")
def pedir_cabrito():
    print("se agrega cabrito")
def pedir_arroz_pollo():
    print("se agrega arroz con pollo")
def pedir_ensalada():
    print("se agrega ensalada")
def pedir_aguadito():
    print("se agrega aguadito")
def pedir_refresco():
    libreria.pedir_nombre("agregar maracuya")
    print("se agrega maracuya")
def pedir_lima():
    print("se agrega lima")
def pedir_cebada():
    print("se agrega cebada")

def agregar_restaurante():
    input("agregar restaurante")
    print("se agrega restaurante")

def agregar_platos():
    input("agregar platos")
    print("se agrega platos")

def agregar_refrescos():
    input("agregar refrescos")
    print("agregar refrescos")

def agregar_restaurante():
    opc=0
    max=5
    while(opc!=max):
        print("### RESTAURANTES ###")
        print("#1.Blue garden   #")
        print("#2.El sagitario  #")
        print("#3.El paisa      #")
        print("#4.El comedor    #")
        print("#5.salir         #")

def agregar_platos():
    opc=0
    max=6
    while(opc!=max):
        print("######## PLATOS #########")
        print("#1.chupe de camarones#")
        print("#2.cabrito#")
        print("#3.arroz con pollo ##")
        print("#4.ensalada #")
        print("#5.aguadito #")
        print("#6.salir   #")
        print("####################")
       opc=libreria.pedir_numero("ingrese opcion:",1,6)
    if(opc==1):
        pedir_chupe_de_camarones()
    if (opc==2):
        pedir_cabrito()
    if (opc==3):
        pedir_arroz_con_pollo()
    if (opc==4):
        pedir_ensalada()
    if(opc==5):
        pedir_aguadito()

def agregar_refrescos():
    opc=0
    max=4
    while(opc!=max):
        print("###### REFRESCOS ######")
        print("#1.maracuya")
        print("#2.lima")
        print("#3.cebada")
        print("#4.salir")
opc=0
max=3
   while(opc!=max):
       print("#### MENU #####")
       print("#1.platos  #")
       print("#2.refrescos #")
       print("#3.salir   #")
       print("########################")
opc=libreria.pedir_numero(''ingrese opc:'' 1,4)
   if (opc==1):
       agregar_platos()
   if(opc==2):
       agregar_refrescos()

print(''fin del programa'')
#fin_menu
