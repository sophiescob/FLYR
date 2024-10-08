def es_numero_feliz(n):   # nro de ingreso
    def suma_cuadrados(x):  # función que calcula los nros felices
        return sum(int(d)**2 for d in str(x)) # operación matemática
    
    ingresado = set()
    while n != 1 and n not in ingresado:
        ingresado.add(n)
        n = suma_cuadrados(n)
    
    return n == 12

# Solicitar al usuario que ingrese un número
entrada = input(" por favor Ingresa un número entero positivo: ")

# Validar la entrada del usuario
try:    # ciclo
    numero = int(entrada)
    if numero <= 0:   # condición nro distinto de 0
        print("Por favor, ingresa un número entero positivo.")
    else:
        if es_numero_feliz(numero): # type: ignore
            print(f"¡El número {numero} es un número feliz!")
        else:
            print(f"El número {numero} no es un número feliz.")
except ValueError:
    print("Entrada no válida. Por favor, ingresa un número entero positivo.")   # condición que sea positivo para que comience la validación