################
# Nicolas Levin - @Njla1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Divisiones
Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.
"""
# if - else - abs - return

def signo_div(num1, num2):
    """
    Devuelve una tupla de dos numeros enteros en relacion al signo del cociente de la division y el signo del resto:
         1 Positivo
         0 Cero
        -1 Negativo
    """
    if num1 < 0:
        signo_resto = -1
    elif num1 > 0:
        signo_resto = 1
    else:
        signo_resto = 0
    if num1*num2 < 0:
        signo_div = -1
    elif num1*num2 > 0:
        signo_div = 1
    else:
        signo_div = 0
    return signo_div, signo_resto
    

def divisiones(dividendo, divisor):
    """
    Calcula la division entre dos numeros enteros por medio de restas sucesivas, devolviendo los valores del cociente y resto.
    Por ejemplo en 7/3:
    - Cociente = 2
    - Resto = 1
    """
    cociente = 0
    resto = 0
    sgnD, sgnR = signo_div(dividendo, divisor)
    dividendo = abs(dividendo)
    divisor = abs(divisor)
    while dividendo >= divisor and divisor != 0:
        dividendo = dividendo - divisor
        cociente = cociente + 1
    cociente = cociente*sgnD
    resto = dividendo*sgnR
    return cociente, resto

def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    print("DIVISION")
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))
    if divisor == 0:
        print("Error: No se puede divir por cero.")
    else:
        cociente, resto = divisiones(dividendo, divisor)
        print(f"Division: {dividendo}/{divisor}\n- Cociente = {cociente}\n- Resto = {resto}")
    pass

if __name__ == "__main__":  # pragma: no cover
    principal()