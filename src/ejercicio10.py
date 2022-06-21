################
# Nicolas Levin - @Njla1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
10. Palíndromo
Escribir una función que indique con True si una palabra o frase ingresada se trata de un palindromo. Palíndromo, es si se lee igual de derecha a izquierda que de izquierda a derecha.
"""
# if - else - while - len - return

def es_palindromo(texto):
    """Determina si una cadena es palindromo o no.
       Retorna:
               True : si es palindromo
               False: no es palindromo
    """
    L = len(texto)
    i = 0
    while i <= L/2:
        if texto[i] != texto[-1-i]:
             return False
        i = i + 1
    return True

def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    texto = input("Ingrese una palabra: ")
    palin = es_palindromo(texto)
    if palin:
        print("palindromo")
    else:
        print("NO")
    pass


if __name__ == "__main__":  # pragma: no cover
    principal()