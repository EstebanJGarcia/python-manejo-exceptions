from contextlib import suppress

with suppress(Exception):
    result = 10 /0
    print( result)
# Exception general o Algo particualar como ZeroDivisionError
print('Finalizamos el programa')