################
# Nicolas Levin - @Njla1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
9. Factores Primos
Escribir una función que retorne una tuple con factores primos de un numero entero positivo.
"""
# Reemplazar por las funciones del ejercicio

def es_primo(numero):
    """Determina si un numero es primo o no.
       Retorna:
               True : si es primo
               False: no es primo
    """
    if numero == 2:
        return True
    elif numero % 2 == 0:
        return False
    n = 3
    while n < (numero/2):
        if numero % n == 0:
            return False
        n = n + 2
    return True

def factores_primos(numero):
    """
    Devuelve los factores primos de un numero entero positivo 
    """
    factores = ()
    div = 2
    if es_primo(numero):
        factores + (numero,)
    else:
        while numero > 1:
            if es_primo(div):
                if numero % div == 0:
                    factores = factores + (div,)
                    numero = numero/div
                else:
                    div = div + 1
    return factores
            
    
def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese un numero entero positivo:"))
    factores = factores_primos(numero)
    if factores[0] == -1:
        print("{numero} es primo")
    else:
        for n in factores:
            print(f"{n}")
    pass


if __name__ == "__main__":  # pragma: no cover
    principal()