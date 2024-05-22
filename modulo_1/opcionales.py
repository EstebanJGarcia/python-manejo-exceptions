# opcionales  else - finally

try:
    number1 : int = 10
    number2 : int = 2
    result : float = number1 /  number2
    #Recomendable hacer except del tipo de error que se espera en este caso ZeroDivisionError
except:
    print('Lo sentimos no fue posible completar la operacion.')
else:
    print('El resultado de la operacion es :' , result)
finally:
    print('El programa ha finalizado.')

"""
    Else: se ejecuta si y solo si la funcion no obtuvo un error.
    finally: se ejecuta siempre aunque se captara un except
"""