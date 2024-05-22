#Notas a las exeptiones - para dar mas contexto
class UsernameException(Exception):

    def __init__(self):
        super().__init__('El username no es valido')

    def it_valid_to_raise(self):
        return len(self.__notes__) > 0
    
    def show_notes(self):
        for note in self.__notes__:
            print(">>>" ,note)



def username_validation(username : str) -> Exception | None:

    username_error = UsernameException()

    if len(username) <= 5:
        username_error.add_note('La longitud debe ser mayor a 5.')

    if username.lower() == 'rukia':
        username_error.add_note('El username no puede ser Rukia')

    if '@' in username:
        username_error.add_note('El signo @ no puede encontrarse en el username')

    if username_error.it_valid_to_raise():
        raise username_error
    
    return True

try:
    username = 'Rukia'
    username_validation(username)

except UsernameException as error:
    print(error)
    print(error.show_notes())

