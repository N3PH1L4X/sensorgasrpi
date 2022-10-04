import RPi.GPIO as GPIO

patente = GPIO.lectura(20)

if patente != null:
    url = f"localhost:9000/patentes.php?patente={patente}"