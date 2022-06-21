################
# Nicolas Levin - @Njla1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
8. Números primos
Escribir una función que indique con True si un numero indicado es Primo.
"""
# if - else - while - return

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
    

def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese un numero entero: "))
    primo = es_primo(numero)
    if primo:
        print(f"El numero {numero} es primo.")
    else:
        print(f"El numero {numero} no es primo.")
    pass


if __name__ == "__main__":  # pragma: no cover
    principal()