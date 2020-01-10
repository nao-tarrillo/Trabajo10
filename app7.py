import libreria
def pedir_habitacion():
    libreria.pedir_nombre("ingrese matrimonial")
    print("se agrega matrimonial")
def pedir_suite():
    print("se agrega suite")
def pedir_doble():
    print("se agrega doble")
def pedir_presidencial():
    print("se agrega presidencial")

def pedir_extra():
    libreria.pedir_nombre("ingrese jacussi")
    print("se agrego jacussi")
def pedir_cama_agua():
    print("se agrego cama agua")
def pedir_mini_bar():
    print("se agrego mini_bar")

def agregar_habitacion():
    input("agregar habitacion")
    print("se agrega habitacion")

def agregar_extras():
    input("agregar extra")
    print("agregar extras")

def agregar_extras():
    opc=0
    max=4
    while(opc!= max):
        print("#### EXTRAS  ####")
        print("#1.matrimonial  #")
        print("#2.suite        #")
        print("#3.doble        #")
        print("#4.presidencial #")
        print("#5.salir        #")
        print("####################")
        opc=libreria.pedir_numero("ingrese opcion:",1,5)
    if (opc==1):
       agregar_matrimonial()
    if(opc==2):
       agregar_suite()
    if(opc==3):
       agregar_doble()
    if (opc==4):
        agregar_presidencial()

opc=0
max=3
   while(opc!=max):
       print("##### HOTEL ######")
       print("#1.Habitacion  #")
       print("#2.extras   #")
       print("#3.salir   #")
    opc=libreria.pedir_numero("ingrese opcion", 1,4)
      if (opc==1):
       agregar_habitacion()
      if(opc==2):
       agregar_extras()

print(''fin del programa'')
#fin_menu
