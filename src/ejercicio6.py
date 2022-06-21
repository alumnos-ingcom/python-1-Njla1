################
# Nicolas Levin - @Njla1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. Ordenar 3 valores
Escribir una función que a partir de tres variables de tipo entero retorne una tupla con dichos valores ordenados de menor a mayor. Y Viceversa
"""
# while - if - elif - return

def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Ordena tres numeros de mayor a menor.
    Por ejemplo: 3, -8, 12 => 12, 3, -8
    """
    while tres > dos or dos > uno:
        if uno < dos:
            aux = uno
            uno = dos
            dos = aux
        if dos < tres:
            aux = dos
            dos = tres
            tres = aux
    return uno,dos,tres
    
        
def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Ordena tres numeros de menor a mayor.
    Por ejemplo: 3, -8, 12 => -8, 3, 12
    """
    while tres < dos or dos < uno:
        if uno > dos:
            aux = uno
            uno = dos
            dos = aux
        if dos > tres:
            aux = dos
            dos = tres
            tres = aux
    return uno,dos,tres

def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    print("Ingrese 3 numeros a ordenar")
    uno = int(input("Ingrese el primer numero: "))
    dos = int(input("Ingrese el segundo numero: "))
    tres = int(input("Ingrese el tercer numero: "))
    opcion = int(input("Como desea ordenarlos?\n1 = MAYOR a menor\n2 = menor a MAYOR\n"))
    if opcion == 1:
        uno, dos, tres = ordenar_mayor_a_menor(uno,dos,tres)
    elif opcion == 2:
        uno, dos, tres = ordenar_menor_a_mayor(uno,dos,tres)
    print(f"{uno},{dos},{tres}")
    
if __name__ == "__main__":  # pragma: no cover
    principal()

    
    
    