Contacto = {
    "nombre": input("Ingrese su nombre:"),
    "telefono": int(input("Ingrese su telefono:")),
    "email": input("Ingrese su email:"),
    "Edad": int(input("Ingrese su edad:"))
}   
print(Contacto)

while True:
    print("===MENU====")
    print("1. Ver ficha de contacto")
    print("2. Editar ficha de contacto")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion:"))
    if opcion == 1:
        print("Ficha de contacto:")
        print("Nombre:", Contacto["nombre"])
        print("Telefono:", Contacto["telefono"])
        print("Email:", Contacto["email"])
        print("Edad:", Contacto["Edad"])
    elif opcion == 2:
        Contacto["campo"] = input("Ingrese el campo que desea editar: (nombre, telefono, email, edad):")
        Contacto["valor"] = input("Ingrese el nuevo valor:")
        if Contacto["campo"] in Contacto:
            Contacto[Contacto["campo"]] = Contacto["valor"]
            print("Campo actualizado:", Contacto)
        else:
            print("Campo no encontrado.")
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida. Por favor, ingrese una opcion del menu.")
