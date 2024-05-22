# Archivo de Logs apartir de las Exceptiones
import logging

logging.basicConfig(
    level=logging.ERROR,
    filename='error.log' #None en consola,  sino archivo de tipo a
)

try:
    10 / 0

except Exception as error:
    logging.error('Lo sentimos no es completar la operacion.')


# por default se almacena en consola el logging.error