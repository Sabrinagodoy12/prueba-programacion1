#Entrada
bacterias_inicial = int(input("Ingrese la cantidad inicial de bacterias: "))
horas = int(input("Ingrese la cantidad de horas que han pasado: "))

#Proceso
bacterias_total = bacterias_inicial * (2**horas)

#Salida
print (f"En un principio había {bacterias_inicial} bacterias, luego de {horas} hora/s, hay {bacterias_total} bacterias en total.")