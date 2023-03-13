import RPi.GPIO as GPIO
from ultrasonico import Ultrasonico

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

trigger_pin = 23
echo_pin = 24

sensor = Ultrasonico(trigger_pin, echo_pin)

distancia = sensor.medir_distancia()
print("Distancia: %.2f cm" % distancia)

del sensor