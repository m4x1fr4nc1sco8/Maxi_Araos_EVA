'''Este algoritmo permite administrar el stock de la tienda'''
import os

print('*'*50)
print('STOCK'.center(50, '*'))
print('*'*50)
productos = {'harina': 10, 'huevos': 50, 'escoba': 5, 'jugo de naranja': 3}
menup = ['Ver productos', 'Agregar producto', 'Eliminar producto', 'Salir']
while True:
    for ind, opt in enumerate(menup):
        print(f'{ind+1}. {opt}')
    ans = input('Que quieres hacer?\n')
    if ans == '1':
        os.system('cls')
        for a, b in productos.items():
            print(f'{a}: {b}')
        print()
    elif ans == '2':
        os.system('cls')
        while True:
            opcion = input('Que producto deseas agregar?\n')
            if opcion.replace(' ', '').isalpha():  
                break
        if opcion.lower in productos:
            os.system('cls')
            print('Error: El producto ya existe\n')
            continue
        else:
            os.system('cls')
            productos [opcion.lower()] = 0
            print('Producto agregado exitosamente\n')
    elif ans == '3':
        os.system('cls')
        while True:
            opcion = input('Que producto desea eliminar?\n')
            if opcion.replace(' ', '').isalpha():
                break
        if opcion.lower() in productos:
            os.system('cls')
            del productos[opcion.lower()]
            print('Producto borrado exitosamente!\n')
        else:
            os.system('cls')
            print('Error: El producto no existe')
    elif ans == '4':
        os.system('cls')
        exit('Muchas gracias por usar nuestro programa, Adios!\n')
    else:
        os.system('cls')
        print('Error: Opcion no valida\n')