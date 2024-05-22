# POO -> Herencia -> exception -> BaseException
# La clase padre maneja el error.
# Exception tiene una clase pader BaseException


from typing import List
try:
    numbers : List[int] = [0,1,2,3,4,5,6]

    number1 : int = numbers[0]
    number2 : int = numbers[0]
    result : float = number1 /  number2
    #Recomendable hacer except del tipo de error que se espera en este caso ZeroDivisionError


except Exception as error:
    print('Lo sentimos, no fue posible completar la operacion') # mensaje muy general
    print(error) # imprime el mensaje del error
#va de antemano ya que no sabemos

else:
    print('El resultado de la operacion es :' , result)

    
finally:
    print('El programa ha finalizado.')

"""
Traceback (most recent call last):
PS F:\clase_padre.py"
Lo sentimos, no fue posible completar la operacion
list index out of range
El programa ha finalizado.
"""