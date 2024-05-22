try:
    raise Exception('No es posible continuar.')

except Exception as error:
    pass

finally:
    print('Finalizamos el bloque')