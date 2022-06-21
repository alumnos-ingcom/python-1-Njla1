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
    largo = len(texto)
    i = 0
    while i <= largo/2:
        if texto[i] != texto[-1-i]:
             return False
        i = i + 1
    return True

def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    print("Este programa indica si la palabra ingresada es un palindromo o no.")
    texto = input("Ingrese una palabra: ")
    palindromo = es_palindromo(texto)
    if palindromo:
        print(f"La palabra '{texto}' es un palindromo")
    else:
        print(f"La palabra '{texto}' no es un palindromo")
    pass


if __name__ == "__main__":  # pragma: no cover
    principal()