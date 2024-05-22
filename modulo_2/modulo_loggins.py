# Logging
# En consola y categorizados
#
#   INFO      = 10
#   DEBUG     = 20
#   WARNING   = 30
#   ERROR     = 40
#   CRITICAL  = 50
import logging


logging.basicConfig(level=logging.INFO) # logging.INFO | 10

logging.info('Hola, este es un mensaje informativo')
logging.debug('Hola, este es un mensaje para debug')
logging.warning('Hola, este es un mensaje para debug')
logging.error('Hola, este es un mensaje de error')
logging.critical('Hola, este es un mensaje critico!')

# POr default solo muestra mensaje nivel >=30