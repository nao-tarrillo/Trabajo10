import os
assert (libreria.validar_cantidad(13)== True)
assert (libreria.validar_cantidad("HOLA")== False)
assert (libreria.validar_cantidad("rosa")== False)
#fin_validar_cantidad

assert (libreria.validar_precio("precio")== False)
assert (libreria.validar_precio(5.6)== False)
assert (libreria.validar_precio(3.5)== True)
#fin_validar_precio

assert (libreria.validar_producto("lapiz")== False)
assert (libreria.validar_productp("cuaderno")== True)
assert (libreria.validar_producto(4.5)== False)
#fin_validar_producto

assert (libreria.validar_precio(4.5)== True)
assert (libreria.validar_precio("lapiz")== False)
assert (libreria.validar_precio(8)== True)
#fin_validar_precio

assert (libreria.validar_producto("laptop")== True)
assert (libreria.validar_producto("iphome")== False)
assert (libreria.validar_producto("mac")== False)
#fin_validar_producto

assert (libreria.validar_nro_cuenta(1345678934567856)== True)
assert (libreria.validar_nro_cuenta("1345678934567856")== False)
assert (libreria.validar_nro_cuenta("cuenta")== False)
#fin_validar_producto

