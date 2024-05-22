# es recomendable crear una archivo con todas las exceptiones 

class UsernameRukiaException(Exception):
    
    def __init__(self):
        self.message = 'El username no puede ser Rukia.'
        super().__init__(self.message) # para visualizar en consola


class UsernameLenException(Exception):

    def __init__(self , username : str):
        self.message = f'El username: {username} debe poseer una longitud mayor igual a 6.'
        super().__init__(self.message) # para visualizar en consola


class CustomError1(Exception):
    def __init__(self) -> Exception:
        super().__init__('Error numero uno')


class CustomError2(Exception):
    def __init__(self) -> Exception:
        super().__init__('Error numero dos')
        

class CustomError3(Exception):
    def __init__(self) -> Exception:
        super().__init__('Error numero tres')
        