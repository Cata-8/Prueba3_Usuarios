from funcion_usuarios import menu, ingresar, buscar, eliminar

usuarios = []

menu()


while True:
    opt = int(input("Ingrese opción: "))
    if opt == 1:
        ingresar(usuarios)
    elif opt == 2:
        buscar(usuarios)
    elif opt == 3:
        eliminar(usuarios)
    elif opt == 4:
        break
    else:
        print("Debe ingresar una opción válida!!")
    
print("Programa terminado. Hasta Luego.")
    

