################
# Nicolas Levin - @Njla1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Números positivos y negativos
Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero utilizando sumas y restas.
"""
# def - if - elif - return
def signo(numero):
    """
    Devuelve un numero entero en relacion al signo del numero:
         1 Positivo
         0 Cero
        -1 Negativo
    """
    aux = numero + numero
    if aux > numero:
        return 1
    elif aux < numero:
        return -1
    else:
        return 0

def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    pass

if __name__ == "__main__":  # pragma: no cover
    principal()