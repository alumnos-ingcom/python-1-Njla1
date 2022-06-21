################
# Nicolas Levin - @Njla1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Suma lenta
Escribir una función que haga la suma entre dos números enteros sin hacer la operación de manera directa. Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1.

La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""
#if - else - while - return

def suma_lenta(numero, otro_numero):
    """
    Realiza una suma de dos numeros enteros sumando de a uno.
    Por ejemplo: 4+3 = 4+1+1+1 = 7
    """
    if otro_numero > 0:
        while otro_numero > 0:
            numero = numero + 1
            otro_numero = otro_numero - 1
    else:
        while otro_numero < 0:
            numero = numero + -1
            otro_numero = otro_numero +1
    return numero
    
    
def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    print("SUMA LENTA DE DOS NUMEROS")
    num1 = int(input("Ingrese el primer numero entero: "))
    num2 = int(input("Ingrese el segundo numero entero: "))
    suma = suma_lenta(num1, num2)
    print(f"La suma de {num1} y {num2} = {suma}")
    pass


if __name__ == "__main__":  # pragma: no cover
    principal()