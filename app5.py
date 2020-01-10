import libreria
def pedir_nombre():
    libreria.pedir_nombre("ingrese nombre:")
    print("se agrega nombre")
def pedir_cursos():
    libreria.pedir_nombre("ingrese AM:")
    print("se agrega AM:")
def pedir_IU():
    print("se agrega IU:")
def pedir_TE():
    print("se agrega TE:")
def pedir_MB():
    print("se agrega MB:")

def pedir_notas():
    libreria.pedir_nota1("ingresar nota1")
    print("se agrega nota1")
def pedir_nota2():
    print("ingresar nota2")
def pedir_nota3():
    print("ingresar nota3")
def pedir_nota4():
    print("ingresa nota4")

def agregar_cliente():
    input("agregar cliente")
    print("se agrega cliente")
def agregar_cursos():
    input("agregar cursos")
    print("agregar cursos")
def agregar_notas():
    input("agregar notas")
    print("se agrega notas")

def agregar_cursos():
    opc=0
    max=4
    while(opc!=max):
        print("#############")
        print("#1.AM:      #")
        print("#2.IU:       #")
        print("#3.TE:       #")
        print("#4.MB:       #")
        print("#5.salir    #")
        print("#################")
       opc=libreria.pedir_numero("ingrese opcion:",1,4)
    if(opc==1):
        pedir_AM()
    if (opc==2):
        pedir_IU()
    if (opc==3):
        pedir_TE()
    if (opc==4):
        pedir_MB()

def agregar_notas():
    opc=0
    max=4
    while(opc!= max):
        print("####NOTAS ####")
        print("#1.nota1   #")
        print("#2.nota2   #")
        print("#3.nota3   #")
        print("#4.nota4   #")
        print("####################")
        opc=libreria.pedir_numero("ingrese opcion:",1,3)
    if (opc==1):
       agregar_nota1()
    if(opc==2):
       agregar_nota2()
    if(opc==3):
       agregar_nota3()

opc=0
max=3
   while(opc!=3):
       print("######################")
       print("#1.alumno #")
       print("#2.cursos        #")
       print("#3.notas         #")
       print("#4.salir         #")
opc=libreria.pedir_numero("ingrese opcion:", 1,4)
   if (opc==1):
       agregar_alumno()
   if(opc==2):
       agregar_cursos()
   if(opc==3):
       agregar_notas()

print(''fin del programa'')
#fin_menu
