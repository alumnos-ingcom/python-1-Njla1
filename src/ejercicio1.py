################
# Nicolas Levin - @Njla1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Conversión de temperaturas
Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.

Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como un número decimal, utilice esta formula para calcular los grados centígrados y retorne el resultado obtenido. Y viceversa.
"""
#if - elif - return

def convertir_a_centigrados(fahrenheit):
    """
    Esta funcion convierte un dato en grados fahrenheit a grados centigrados.
    Por ejemplo: 356.0ºF = 180.0ºC
    """
    centigrados  = (fahrenheit-32)/1.8
    return centigrados


def convertir_a_fahrenheit(centigrados):
    """
    Esta funcion convierte un dato en grados centigrados a grados fahrenheit.
    Por ejemplo: 78.0ºC = 172.4ºF
    """
    fahrenheit = centigrados*1.8 + 32
    return fahrenheit


def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    opcion = int(input("Cual conversion desea realizar?:\n1 = Centigrados -> Fahrenheit\n2 = Fahrenheit -> Centigrados\n"))
    if opcion == 1:
        centigrados = float(input("Ingrese la cantidad de grados centigrados a convertir: "))
        fahrenheit = convertir_a_fahrenheit(centigrados)
        print(f"{centigrados}ºC = {fahrenheit}ºF")
    elif opcion == 2:
        fahrenheit = float(input("Ingrese la cantidad de grados fahrenheit a convertir: "))
        centigrados = convertir_a_centigrados(fahrenheit)
        print(f"{fahrenheit}ºF = {centigrados}ºC")
    pass


if __name__ == "__main__":  # pragma: no cover
    principal()