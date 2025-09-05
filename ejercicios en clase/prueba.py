num = input("numero entero").strip()

while not num.lstrip().isdigit():
    print("Error, ingresa un número entero: ")
    num(input("Número entero: "))


valor1 = int(input("Ingrese un número entero: "))
valor2 = int(input("Ingrese otro número entero: "))

minimo = min(valor1, valor2)
maximo = max(valor1, valor2)


suma = sum(range(minimo, maximo))

print("hola", end=" ")