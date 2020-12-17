from os import path, mkdir

from mantenedores import ventas, productos, vendedores


def create_database():
    files_names = ['ENC_VTA', 'DET_VTA', 'PRODUCTOS', 'VENDEDORES']
    if not path.isdir('./db'):
        mkdir('./db/')
    for name in files_names:
        full_name = 'db/' + name + '.dat'
        if not path.isfile(full_name):
            file = open(full_name, 'w')
            file.close()


create_database()
continuar = True
opt, opt_final = 0, 0
while opt != 5:
    print('1. Ventas')
    print('2. Vendedores')
    print('3. Productos')
    print('4. Productos')
    print('5. Salir')
    opt = int(input('Ingrese opcion: '))
    if opt == 1:
        print('1. Registrar venta')
        print('2. Consultar venta')
        print('3. Anular venta')
        opt_final = int(input('Ingrese opcion: '))
        if opt_final == 1:
            ventas.realizar_venta()
        elif opt_final == 2:
            ventas.consultar_venta()
        elif opt_final == 3:
            ventas.anular_venta()
        else:
            print('Opcion no reconocida.')
    elif opt == 2:
        print('1. Agregar vendedor')
        print('2. Modificar vendedor')
        print('3. Consultar vendedor')
        print('4. Eliminar vendedor')
        print('5. Listar vendedores')
        opt_final = int(input('Ingrese opcion: '))
        if opt_final == 1:
            vendedores.agregar()
        elif opt_final == 5:
            vendedores.listar()
    elif opt == 3:
        print('1. Agregar productos')
        print('2. Modificar productos')
        print('3. Consultar productos')
        print('4. Eliminar productos')
        print('5. Listar productos')
        opt_final = int(input('Ingrese opcion: '))
    elif opt == 4:
        print('1. Productos con stock critico')
        print('2. Recaudacion diaria')
        print('3. Ventas por vendedor')
        opt_final = int(input('Ingrese opcion: '))
    elif opt != 5:
        print('Opcion no valida.')
