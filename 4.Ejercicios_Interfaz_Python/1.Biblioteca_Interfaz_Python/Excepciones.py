try:
    # Intentar dividir dos números
    numerador = 10
    denominador = 0
    resultado = numerador / denominador
    print("El resultado es:", resultado)
except ZeroDivisionError:
    # Manejar la excepción si se intenta dividir por cero
    print("Error: No se puede dividir por cero.")
else:
    # Este bloque se ejecuta si no hay excepciones
    print("División exitosa.")
finally:
    # Este bloque se ejecuta siempre
    print("Operación completada.")
