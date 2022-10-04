import RPi.GPIO as GPIO, Adafruit_DHT, sys, requests, json
from gpiozero import Buzzer
from time import sleep
from rpi_lcd import LCD

GPIO.setmode(GPIO.BCM)

buzzer = Buzzer(18) #Inicializar buzzer}
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 21
MQ_PIN = 25
GPIO.setup(25,GPIO.IN)

def alerta_telegram(tem,hum,gashum):
    url='https://api.telegram.org/'
    bot='bot5585883929'
    api_key='AAH-a6FprInxGEqmOfHaUGHWNnbz4L1NOfQ'
    chat_id='-609887845'
    if gashum == 0:
        mensaje='ALERTA LECTURA IRREGULAR:\nTemperatura: {} °C\nHumedad relativa: {}%\nNo se detecta gas ni humo'.format(tem,hum)
    elif gashum == 1:
        mensaje='ALERTA LECTURA IRREGULAR:\nTemperatura: {} °C\nHumedad relativa: {}%\nHUMO/GAS DETECTADO'.format(tem,hum)
    r = requests.post(url + bot + ':' + api_key + '/sendMessage', data={'chat_id': chat_id, 'text': mensaje})

def encender_alarma(tem, hum, gashum):
    if tem >= 30.0 and hum <= 30.0 or gashum == 1: 
        for i in range(7):       
            buzzer.on()
            sleep(0.12)
            buzzer.off()
            sleep(0.05)

def enviar_json(tem, hum):
    #Crear JSON con datos
    datos = {"temperatura":"{}".format(tem), "humedad":"{}".format(hum)}
    datos_json = json.dumps(datos)
    #Hacer peticion POST a API
    url = "http://192.168.120.58:80"
    path = "/cesfam/api/sensor.php"
    remoto = url+path
    peticion = requests.post(remoto, datos_json)
    retorno = (peticion.status_code, peticion.content, datos_json)
    return retorno

try:
    lcd = LCD() #Inicializar lcd
    lcd.text("En funcionamiento...", 1)
    while True:
        #Lecturas de sensores
        humedad, temperatura = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN) #Humedad temperatura
        gas_humo_detectado = GPIO.input(MQ_PIN) #Humo gas

        if humedad is not None and temperatura is not None:
            lcd.text(str(humedad) + " Hum", 2)
            lcd.text(str(temperatura) + " Tmp", 3)
            if gas_humo_detectado == 1:
                lcd.text("HUMO/GAS DETECTADO",4)
            elif gas_humo_detectado == 0:
                lcd.text("NO DETECTA HUMO/GAS",4)

            #Enviar post a API (ver funcion)
            print(enviar_json(temperatura,humedad))

            if humedad <= 30.0 and temperatura >= 30.0 or gas_humo_detectado == 1: #1 = True = Verdadero = Gas/humo detectado
                print(enviar_json(temperatura,humedad))
                alerta_telegram(temperatura,humedad,gas_humo_detectado)
                encender_alarma(temperatura,humedad,gas_humo_detectado)
        else:
            #Realmente no siempre es falla, aveces el sensor se salta
            #un ciclo de ejecucion y por eso no llena las variables
            #de temperatura y humedad
            print("Sensor de humedad fallando...")
        sleep(3)
    lcd.clear()
except KeyboardInterrupt:
    lcd.clear()
    lcd.text("Cerrando...", 4)
    print("Cerrando...")
    sleep(2)
    lcd.clear()
    sys.exit()