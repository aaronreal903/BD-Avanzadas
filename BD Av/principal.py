print 'menu'


print '1. READ'
print '2. INSERTAR'
print '3. BORRAR'
print '4. ACTUALIZAR'


initial_string = raw_input('Ingresa una opcion\n')


if(initial_string == "read"):
    print 'estas leyendo'

elif(initial_string == "insertar"):
    print 'Estas insertando'

elif(initial_string == "borrar"):
    print 'Estas borrando'

elif(initial_string == "actualizar"):
    print 'Estas actualizando'