# PPO - usando clases
# Nuestras excepciones deben heredar de la clase padre Exception
# consideracion siempre que se haga una clase tipo Exception, NombrClaseException(Exception):
# Exception('String del causante de la Exception')
"""
from exception import UsernameLenException, UsernameRukiaException
"""
# las exceptiones es mejor guardalas en un modulo exception.py
class UsernameRukiaException(Exception):
    

    def __init__(self):
        self.message = 'El username no puede ser Rukia.'
        super().__init__(self.message) # para visualizar en consola


class UsernameLenException(Exception):


    def __init__(self , username : str):
        self.message = f'El username: {username} debe poseer una longitud mayor igual a 6.'
        super().__init__(self.message) # para visualizar en consola


def validate_username(username: str) -> bool:

    if username == 'Rukia':
        raise UsernameRukiaException()

    if len(username) < 6:
        raise UsernameLenException(username) #el parametro es obligatorio
    return True

try:
    result = validate_username('Rukia')
    print(result)

except UsernameRukiaException as error:
    print(error)


except UsernameLenException as error:
    print(error)


except Exception as error:
    print('>>> Lo sentimos, no fue posible completar la operacion')
    print(error)

