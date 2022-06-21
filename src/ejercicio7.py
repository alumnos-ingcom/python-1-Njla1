################
# Nicolas Levin - @Njla1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
7. Transformación de un número
Escribir un programa que permita transformar un número solicitado expresado en grados, minutos y segundos a segundos a segundos. Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.

Recuerden que un grado son 60 minutos y un minuto son 60 segundos.
"""
# def - if - elif - else - return - abs
def signo(numero):
    """
    Devuelve un numero entero en relacion al signo del numero:
         1 Positivo
         0 Cero
        -1 Negativo
    """
    if numero < 0:
        return -1
    elif numero > 0:
        return 1
    else:
        return 0
    
    

def sexadecimal_a_decimal(horas, minutos, segundos):
    """
    Transforma un valor hexadecimal de horas,minutos y segundos a su equivalente decimal.
    Por ejemplo:
    
         horas : minutos : segundos => numero decimal
           3   :    8    :    5     =>     11285
           
    """
    decimal = horas*3600+minutos*60+segundos
    return decimal

def decimal_a_sexadecimal(numero):
    """
    Transforma un numero decimal a su equivalente hexadecimal.
    Por ejemplo:
    
         numero decimal  => horas : minutos : segundos             
              5743       =>   1   :    35   :    43
                                 
    """
    horas = 0
    minutos = 0
    segundos = 0
    sgn = signo(numero)
    numero = abs(numero)
    while numero >= 3600:
        numero = numero - 3600
        horas = horas + 1
    while numero >= 60:
        numero = numero - 60
        minutos = minutos + 1
    horas = horas*sgn
    minutos = minutos*sgn
    segundos = numero*sgn
    return horas, minutos, segundos


def principal():  # pragma: no cover
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    opcion = int(input("Que conversion desea realizar?\n1 = Sexadecimal -> Decimal\n2 = Decimal -> Sexadecimal\n"))
    if opcion == 1:
        horas = int(input("Horas: "))
        minutos = int(input("Minutos: "))
        segundos = int(input("Segundos: "))
        decimal = sexadecimal_a_decimal(horas, minutos, segundos)
        print(f"{horas} : {minutos} : {segundos} => {decimal}")
    elif opcion == 2:
        numero = int(input("Numero decimal a convertir: "))
        horas, minutos, segundos = decimal_a_sexadecimal(numero)
        print(f"{numero} => {horas} : {minutos} : {segundos}")
    pass


if __name__ == "__main__":  # pragma: no cover
    principal()