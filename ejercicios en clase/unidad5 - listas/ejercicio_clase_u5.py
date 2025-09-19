
# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
# • Mostrar el total vendido por cada producto. 
# • Mostrar el día con mayores ventas totales. 
# • Indicar cuál fue el producto más vendido en la semana.

productos = [
    [1, 5, 6, 2, 5, 9, 8], [2, 5, 10, 3, 10, 8, 5],  [6, 2, 5, 7, 5, 1, 5], [5, 0, 2, 3, 5, 2, 0]
]
#Muestro la tabla de las ventas de productos
for fila in productos:
        for celda in fila:
         print(celda, end=" ")
        print()

#Muestro el total de las ventas de cada producto
productos_total = []

for i in range(4):
    total = 0
    for j in range (7):
        total += productos[i] [j]
    productos_total.append(total)
    print(f"El total del producto {i+1} es de: {total}")

#Muestro el día con mayores ventas totales
mayor_ventas = 0
dia_mayor = 0

for j in range(7):
    print(f"J:{j}", end=" ")
    suma_dia = 0
    for i in range(4):
        print(f"I:{i}")
        suma_dia += productos[i][j]
        print(f"Suma: {suma_dia}")
    if suma_dia > mayor_ventas:
        mayor_ventas = suma_dia
        dia_mayor = j

print(f"El día que más se vendió es el día {dia_mayor+1} y el total fue: {mayor_ventas}")

#Muestro el producto más vendido
mas_vendido = 0
producto = 0

for i in range(4):
    if productos_total[i] > mas_vendido:
        mas_vendido = productos_total[i]
        producto = i

print(f"El producto que más se vendió fue el: {producto+1} con {mas_vendido} ventas en la semana.")
