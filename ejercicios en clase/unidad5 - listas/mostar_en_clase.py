# Generar una lista con booleanos que indiquen que es true si es par y false si es impar

# numeros = [4, 7, 10, 13, 22]
# listanueva = []

# for i in numeros:
#     if i % 2 == 0:
#         listanueva.append(True)
#     else:
#         listanueva.append(False)

# print(f"La lista de números es: {numeros} \nLa nueva lista es: {listanueva}")


#Estructura Match --> según cada color qué es lo que debe ejecutarse

# colores = ["rojo", "azul", "verde", "blanco"]

# for color in colores:
#     match color:
#         case "rojo" | "azul" | "amarillo":     # la --> | es como un or 
#             print(f"el {color} es color primario")
#         case "verde" | "naranja" | "violeta":
#             print(f"el {color} es color secundario")
#         case "blanco" | "negro":
#             print(f"el {color} no es un color primario ni secundario")
#         case _:        # case _: --> significa que no es ninguna de las anteriores, como un else
#             print(f"el {color} color desconocido")


#Crear un menú de opciones en la que el usuario pueda elegir e ir variando entre las opciones hasta que presione para salir del menú.
nombres = ["Ana", "Luis"]

opcion = 0
while opcion != 4:
    opcion = int(input("\nIngrese el número de la opción que desea ejecutar: \n1. Mostrar la lista de nombres. \n2. Agregar un nombre a la lista. \n3. Eliminar un nombre de la lista. \n4. Salir del menú. \n" ))

    match opcion:
        case 1:
            print(nombres)
        case 2: 
            nuevo_nombre = input("Ingrese un nombre para agregar a la lista: ").title()
            nombres.append(nuevo_nombre)
            print(nombres)
        case 3:
            eliminar_nombre = input("Ingrese el nombre de la lista que desea eliminar").title()
            if eliminar_nombre in nombres:
                nombres.remove(eliminar_nombre)
                print(nombres)
            else:
                print(f"{eliminar_nombre} no se encuentra dentro de la lista de nombres.")
        case 4:
            print(f"Gracias por visitar nuestro sitio. Que vuelva pronto.")
        case _: 
            print("La opción ingresada es incorrecta.")


# Dada la lista numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90], utiliza slicing para obtener: los primeros tres elementos, los últimos dos elementos, y los elementos en posiciones pares.

# Convierte la cadena "Python,Java,C++,JavaScript,PHP" en una lista de lenguajes de programación utilizando split(). Luego añade "Ruby" a la listae imprime los lenguajes por consola.