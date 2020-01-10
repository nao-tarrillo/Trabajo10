import libreria
def pedir_nombre():
    libreria.pedir_nombre("ingrese nombre")
    print("se agrega nombre")

def pedir_moneda():
    libreria.pedir_nombre("ingresar dolares")
    print("se agrego dolares")
def pedir_soles():
    print("se agrego soles")

def pedir_tipo_de_pago():
    libreria.pedir_nombre("ingresar efectivo:")
    print("se agrego efectivo")
def pedir_transferencia():
    print("se agrego transferencia")

def pedir_monto():
    libreria.pedir_numero("ingresar monto")
    print("se agrego monto")

def agregar_cliente():
    input("agregar cliente")
    print("se agrega cliente")
def agregar_moneda():
    input("agregar moneda")
    print("agregar moneda")
def agregar_tipo_de_pago():
    input("agregar tipo de pago")
    print("se agrega tipo de pago")
def agregar_monto():
    input("agregar monto")
    print("agregar monto")

def agregar_moneda():
    opc=0
    max=3
    while(opc!=max):
        print("#### MONEDA #####")
        print("#1.dolares      #")
        print("#2.soles        #")
        print("#3.salir        #")
        print("#####################")
 opc=libreria.pedir_numero(''ingrese opc:'' 1,3)
   if (opc==1):
       agregar_dolares()
   if(opc==2):
       agregar_soles()

def agregar_pago_por():
    opc=0
    max=4
    while(opc!= max):
        print("######## PAGO POR  ######")
        print("#1.efectivo <= S/2500   #")
        print("#2.transferencia >=2500 #")
        print("#3.salir                #")
        print("#########################")
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    if (opc==1):
       agregar_efectivo()
    if(opc==2):
       agregar_transferencia()


opc=0
max=3
   while(opc!=3):
       print("#####################")
       print("#1.cliente:          ")
       print("#2.tipo de moneda   #")
       print("#3.tipo de pago     #")
       print("#4.monto a pagar    #")
       print("#5.salir            #")
opc=libreria.pedir_numero(''ingrese opc:'' 1,5)
   if (opc==1):
       agregar_cliente()
   if(opc==2):
       agregar_tipo_moneda():
   if(opc==3):
       agregar_tipo_de_pago():
   if(opc==4):
       agregar_monto_a_pagar():

print(''fin del programa'')
#fin_menu
