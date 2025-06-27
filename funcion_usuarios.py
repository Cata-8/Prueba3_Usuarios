
def menu():
    print("Menú principal")
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir.")
    
def validar_contrasenia(contrasenia):
    if len(contrasenia) < 8:
        return False
    if " " in contrasenia:
        return False
    tiene_numero = any(char.isdigit() for char in contrasenia)
    tiene_letra = any(char.isalpha() for char in contrasenia)
    return tiene_numero and tiene_letra 

def nombre_repetido(nombre, lista_usuarios):
    for u in lista_usuarios:
        if u["nombre"] == nombre.lower():
            return True
    return False
    
def ingresar(lista_usuarios):
    
    while True:
        nombre = input("Ingrese nombre de usuario: ")
        if nombre_repetido(nombre,lista_usuarios):
            print("El nombre ya se encuentra en la lista")
        else:
            break
    
    sexo = input("Ingrese sexo: ")
    sexo_valido = ["F", "M"]
    while sexo not in sexo_valido:
        print("Debe ingresar M o F solamente. Intente de nuevo.")
        sexo = input("Ingrese sexo: ")
        
    while True:
        contrasenia = input("Ingrese contraseña: ")
        if not validar_contrasenia(contrasenia):
            print("Contraseña no valida. La contraseña debe ser de largo mínimo 8, tener mínimo 1 número y 1 letra.")
        else:
            break
        
    lista_usuarios.append (
        {"nombre" : nombre.lower(),
         "sexo": sexo.upper(),
         "contrasenia": contrasenia})
    
    for i in lista_usuarios:
        print(i)
    
def buscar (lista_usuarios):
    nombre = input("Ingrese usuario a buscar: ").lower()
    for usuarios in lista_usuarios:
        if usuarios["nombre"] == nombre:
            print(f"El sexo del usuario es: {usuarios["sexo"]} y la contraseña es: {usuarios["contrasenia"]}")
            return
        
def eliminar(lista_usuarios):
    while True:
        nombre = input("Ingrese usuario a buscar: ").lower()
        encontrado = False
        for usuarios in enumerate(lista_usuarios):
            if usuarios["nombre"] == nombre:
                encontrado = True
        if encontrado == True:
            lista_usuarios.pop(usuarios)
            print("Usuario eliminado con éxito!")
            break
        else:
            print("No se pudo eliminar usuario!")
            
        
        
        
    
    
    #tipo = input("Ingrese tipo: ")
    #tipos_validos = ["fuego","agua","hierba","veneno","psiquico","luchador","electrico"] 
    #while tipo not in tipos_validos:
    #    print("Debe ingresar: “fuego”, “agua”,” hierba”,” veneno”,” psíquico”,”luchador”,”eléctrico”.")
    #    tipo = input("Ingrese tipo: ")
    #print("Pokemon ingresado con éxito!!")
    #lista_pokemones.append(
    #    { "id": id_pokemon, 
    #     "nombre": nombre.lower(),
    #     "codigo": codigo,
    #     "tipo": tipo.lower()})
    #
    #for i in lista_pokemones:
    #    print(i)
        
    
#def buscar(lista_pokemones):
#    nombre = input("Ingrese pokemon a buscar: ")
#    for pokemon in lista_pokemones:
#        if pokemon["nombre"] == nombre:
#            print(f"El tipo de pokemon es : {pokemon["tipo"]} y su código es : {pokemon["codigo"]}")
#            return