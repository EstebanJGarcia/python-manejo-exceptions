# trabajamos nuestras propias funciones
#from typing import List

def validate_username(username: str) -> bool:

    if username == 'Rukia':
        raise Exception('El username no puede ser Rukia')

    if len(username) < 6:
        raise Exception('El username debe poseer una longitud mayor a 6 caracteres.')
    return True

try:
    result = validate_username('Rukia')
    print(result)
except Exception as error:
    print(error)
    print('>>> Lo sentimos, no fue posible competar la operacion.')