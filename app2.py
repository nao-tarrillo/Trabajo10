import libreria
def pedir_cuadernos():
    libreria.pedir_nombre("ingrese cuadernos:")
    print("se agrega cuadernos")
def pedir_boligrafos():
    print("se agrega boligrafos")
def pedir_uniforme():
    print("se agrega  uniforme")

def pedir_precio():
    libreria.pedir_numero("ingresar precio")
    print ("se agrega precio")


def agregar_producto():
    opc=0
    max=4
      while(opc!=max):
         print("##### PRODUCTO ######")
         print("#1.cuadernos    #")
         print("#2.boligrafos   #")
         print"#3.uniforme      #")
         print("#4.salir        #")
         print("#######################")
       opc=libreria.pedir_numero("ingrese su opcion:",1,4)
      if(opc==1):
          agregar_cuadernos()
      if(opc==2):
          agregar_boligrafos()
      if(opc==3):
          agregar_uniforme()

def agregar_precio():
    opc=0
    max=4
      while(opc!=max):
         print("##### PRECIO ######")
         print("#1.prec1 (S/2-S/10)  #")
         print("#2.prec2 (S/10-S/15) #")
         print("#3.prec3 (S/25-S/45) #")
         print("#4.salir    #")
         print("#######################")
       opc=libreria.pedir_numero("ingrese su opcion:",1,4)
      if(opc==1):
          agregar_prec1()
      if(opc==2):
          agregar_prec2()
      if(opc==3):
          agregar_prec3()

opc=0
max=3
   while(opc!=3):
       print("####### MENU ######")
       print("#1.producto       #")
       print("#2.precio         #")
       print("#3.salir          #")
       print("##################")

opc=libreria.pedir_numero("ingrese opcion",1,3)
   if (opc==1):
       agregar_producto()
   if(opc==2):
       agregar_precio()
print("fin del programa")
#fin_menu
