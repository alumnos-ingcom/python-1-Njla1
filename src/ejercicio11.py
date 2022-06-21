################
# Nicolas Levin - @Njla1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
11. Multiplos de
Escribir una función que indique con True si un número entero es multiplo de otro, utilizando sumas y restas.
"""
# if - else - while - 

def es_multiplo(numero, multiplo):
    """Determina si un numero es multiplo de otro por medio de sumas.
       Retorna:
               True : si es multiplo
               False: no es multiplo
    """
    suma = 0
    num_aux = abs(numero)
    mul_aux = abs(multiplo)
    while suma < num_aux:
        suma = suma + mul_aux
    if suma == num_aux:
        return True
    else:
        return False
    
    
    
def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese un numero entero: "))
    multiplo = int(input("Ingrese el numero que desea saber si es multiplo: "))
    if es_multiplo(numero, multiplo):
        print(f"El numero {numero} es multiplo de {multiplo}")
    else:
        print(f"El numero {numero} no es multiplo de {multiplo}")
    pass


if __name__ == "__main__":  # pragma: no cover
    principal()