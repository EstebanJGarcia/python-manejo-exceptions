from typing import List
try:
    numbers : List[int] = [0,1,2,3,4,5,6]

    number1 : int = numbers[0]
    number2 : int = numbers[10]
    result : float = number1 /  number2
    #Recomendable hacer except del tipo de error que se espera en este caso ZeroDivisionError


except ZeroDivisionError as error:
    print('lo sentimos no se puede dividir sobre 0.')
    print(error)


except NameError as error:
    print('La variable no se encuentra definida.')
    print(error)


except IndexError as error:
    print('Lo sentimos no encontramos el indice', error)


else:
    print('El resultado de la operacion es :' , result)

    
finally:
    print('El programa ha finalizado.')

"""
un error en una variable que no existe al no manejar ese tipo de error
se corta el programa asi que añadimos un except NameError

Traceback (most recent call last):
  File "f:\multuple_error.py", line 4, in <module>   
    result : float = number1 /  number3
                                ^^^^^^^
NameError: name 'number3' is not defined. Did you mean: 'number1'?

Al manejar NameError
e sequence '\m'
La variable no se encuentra definida.
name 'number3' is not defined
El programa ha finalizado.


Traceback (most recent call last):
  File "f:\multuple_error.py", line 6, in <module>
    number2 : int = numbers[10]
                    ~~~~~~~^^^^
IndexError: list index out of range
"""