import logging
import traceback
import contextlib

logging.basicConfig(
    level=logging.ERROR,
    filename='error.log',
    format="%(asctime)s:%(levelname)s:%(message)s"
)

# decorar la funcion con @contextlib.contextmanager
@contextlib.contextmanager
def write_on_log_error():
    try:
        yield """ es un placeholder del bloque de with
                funciona si  result = 10 / 0 se encontrara en esta parte
                             print(result)
              """
    except Exception as error:
        exception_info = {
            'message': str(error),
            'detail':  traceback.format_exc()
        }
    logging.error( exception_info)


with write_on_log_error():
    result = 10 / 0
    print(result)

with write_on_log_error():
    file = open('user.txt')

#agrupar las lineas de codigo que pueden causar un error, se puede enviar 
#n veces 