saldo = 150000
opcion = int(input("Ingrese el número de la opción que desea: \n 1. Consultar saldo \n 2. Retirar dinero \n 3. Despositar dinero \n 4. Salir"))

if opcion == 1:
    print(f"Su saldo es de ${saldo}")
elif opcion == 2:
    retirar = int(input("Ingrese el monto que desea retirar: "))
    saldo = saldo - retirar
    if retirar < saldo and retirar != 0 :
        print(f"La operación fue exitosa, saldo actual: ${saldo}")
    else :
        print("La operación no es correcta, por favor intetelo de nuevo.")
elif opcion == 3:
    deposito = int(input("Ingrese el monto que desea depositar: "))
    saldo += deposito    #esto es igual a --> saldo = saldo + deposito
    if deposito != 0:
        print(f"El deposito se realizó con éxito! Su saldo actual es: ${saldo}")
    else:
        print("La operación no es correcta, por favor intetelo de nuevo.")
elif opcion == 4:
    print("Gracias por elegirnos.")
else:
    print("Opción inválida.")