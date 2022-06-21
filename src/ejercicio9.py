################
# Nicolas Levin - @Njla1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
9. Factores Primos
Escribir una función que retorne una tuple con factores primos de un numero entero positivo.
"""
# if - elif - else - while - return

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
    divisor = 3
    while divisor < (numero/2):
        if numero % divisor == 0:
            return False
        divisor = divisor + 2
    return True

def factores_primos(numero):
    """
    Devuelve una tupla con los factores primos de un numero entero positivo.
    Retorna (0) en caso de que el numero ingresado sea primo.
    """
    factores = ()
    divisor = 2
    if es_primo(numero):
        factores = factores + (0,)
    else:
        while numero > 1:
            if es_primo(divisor):
                if numero % divisor == 0:
                    factores = factores + (divisor,)
                    numero = numero/divisor
                else:
                    divisor = divisor + 1
    return factores
            
    
def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese un numero entero positivo:"))
    factores = factores_primos(numero)
    print(f"Los factores primos de {numero} son: ")
    for n in factores:
        print(f"{n}")
    pass


if __name__ == "__main__":  # pragma: no cover
    principal()