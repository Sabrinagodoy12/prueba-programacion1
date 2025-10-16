def generador_tablas_equipo():
    """
    Herramienta de estudio que genera tablas de verdad para 5 expresiones lógicas
    predefinidas, ideal para un equipo de 5 personas.
    Utiliza listas para almacenar y procesar las combinaciones de verdad.
    """
    
    # --- Uso de Listas para almacenar las combinaciones de verdad ---
    # Lista de listas para 2 variables (4 combinaciones)
    combinaciones_2_var = [
        [False, False],
        [False, True],
        [True, False],
        [True, True]
    ]
    
    # Lista de listas para 3 variables (8 combinaciones)
    combinaciones_3_var = [
        [False, False, False],
        [False, False, True],
        [False, True, False],
        [False, True, True],
        [True, False, False],
        [True, False, True],
        [True, True, False],
        [True, True, True]
    ]

    # Menú con las 5 expresiones para el equipo
    print("--- 🛠️ Herramienta de Lógica para el Equipo ---")
    print("Seleccione la expresión para generar su Tabla de Verdad:")
    print("1. Expresión Simple: A AND B")
    print("2. Expresión Inclusiva: A OR B")
    print("3. Expresión Condicional (Implicación): NOT A OR B")
    print("4. Expresión Exclusiva: A XOR B")
    print("5. Expresión de 3 Variables: (A OR B) AND C")
    
    eleccion = input("\nIngrese el número de su elección (1-5): ")

    # --- Lógica para procesar la elección del usuario ---
    if eleccion == '1':
        print("\nTabla de Verdad para: A AND B")
        print("-----------------------------")
        print(f"{'A':<7} | {'B':<7} | {'Resultado'}")
        print("-----------------------------")
        for fila in combinaciones_2_var:
            a, b = fila
            resultado = a and b
            print(f"{str(a):<7} | {str(b):<7} | {str(resultado)}")

    elif eleccion == '2':
        print("\nTabla de Verdad para: A OR B")
        print("----------------------------")
        print(f"{'A':<7} | {'B':<7} | {'Resultado'}")
        print("----------------------------")
        for fila in combinaciones_2_var:
            a, b = fila
            resultado = a or b
            print(f"{str(a):<7} | {str(b):<7} | {str(resultado)}")

    elif eleccion == '3':
        print("\nTabla de Verdad para: NOT A OR B  (A -> B)")
        print("------------------------------------------")
        print(f"{'A':<7} | {'B':<7} | {'Resultado'}")
        print("------------------------------------------")
        for fila in combinaciones_2_var:
            a, b = fila
            resultado = (not a) or b
            print(f"{str(a):<7} | {str(b):<7} | {str(resultado)}")

    elif eleccion == '4':
        print("\nTabla de Verdad para: A XOR B")
        print("-----------------------------")
        print(f"{'A':<7} | {'B':<7} | {'Resultado'}")
        print("-----------------------------")
        for fila in combinaciones_2_var:
            a, b = fila
            resultado = a != b # XOR es equivalente a 'no es igual'
            print(f"{str(a):<7} | {str(b):<7} | {str(resultado)}")
    
    elif eleccion == '5':
        print("\nTabla de Verdad para: (A OR B) AND C")
        print("---------------------------------------")
        print(f"{'A':<7} | {'B':<7} | {'C':<7} | {'Resultado'}")
        print("---------------------------------------")
        for fila in combinaciones_3_var:
            a, b, c = fila
            resultado = (a or b) and c
            print(f"{str(a):<7} | {str(b):<7} | {str(c):<7} | {str(resultado)}")

    else:
        print("\nError: Opción no válida. Por favor, ejecute de nuevo y elija un número del 1 al 5.")

# Ejecutar el programa
generador_tablas_equipo()
