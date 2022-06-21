################
# Nicolas Levin - @Njla1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Comparación de números
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:

Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
"""
# def - if - elif - return
def compara(numero, otro_numero):
    """
    Devuelve un numero entero en relacion a la relacion de dos numeros:
         1 Si el primer numero es mayor al segundo
         0 Si ambos numeros son iguales
        -1 Si el primer numero es menor al segundo
    """
    aux = numero - otro_numero
    if aux > 0:
        return 1
    elif aux < 0:
        return -1
    else:
        return 0

def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    compara = compara(num1,num2)
    if compara == 1:
        print(f"El numero {num1} es mayor que {num2}")
    elif compara == -1:
        print(f"El numero {num1} es menor que {num2}")
    else:
        print("Ambos numeros son iguales")
    pass

if __name__ == "__main__":  # pragma: no cover
    principal()