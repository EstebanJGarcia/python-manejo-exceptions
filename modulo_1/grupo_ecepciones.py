"""#from modulo_1.exception import CustomError1, CustomError2, CustomError3
# Donde modulo_1 es un folder  .  exception que es el archivo que esta dentro del folder modulo_1
# ejemplo   folder.archivo.py >>>  modulo_1.exception
"""
# MAnejar los error por grupo ExceptionGroup
from exception import CustomError1, CustomError2,CustomError3
try:#3.11 python
    raise ExceptionGroup('Un grupo de errores propios.',
                         [CustomError1(), CustomError2(), CustomError3()]
    )

except* CustomError1:
    print('Error tipo 1')

except* CustomError2:
    print('Error tipo 2')

except* CustomError3:
    print('Error tipo 3')

# al colocar * en la exception pernolaziada se separa del grupo
# ejm *CustomError2

#code xD n