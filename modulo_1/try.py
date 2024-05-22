# try - except

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
        try se va colocar el codigo donde posible se dispare un error
        except el codigo que se ejecutara cuando una excepcion sera lanzada
        finally siempre se va ejercutar
        else : se ejecutara si no hay error.
    """