def fooBar(n):
    """
    Esta función imprime "Foo", "Bar", o "FooBar" dependiendo de los escenarios de pruebas,
    o muestra el número en caso de no cumplir con ninguna de las condiciones.
    """

	# Validar si el numero (n) es divisible entre 3 y 5
    if n % 3 == 0 and n % 5 == 0:
        print("FooBar")
    elif n % 3 == 0:
        print("Foo")
    elif n % 5 == 0:
        print("Bar")
    else:
        print(n)


# Ejemplos de prueba
fooBar(9)   # Salida: Foo
fooBar(10)  # Salida: Bar
fooBar(15)  # Salida: FooBar
fooBar(16)  # Salida: 16