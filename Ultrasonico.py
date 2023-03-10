from Sensor import Sensor
import RPi.GPIO as GPIO
import time

class Ultrasonico(Sensor):
    def __init__(self, pin_trigger, pin_echo):
        self.pin_trigger = pin_trigger
        self.pin_echo = pin_echo
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_trigger, GPIO.OUT)
        GPIO.setup(self.pin_echo, GPIO.IN)
        GPIO.output(self.pin_trigger, False)
        
    def leer_valor(self):
        GPIO.output(self.pin_trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.pin_trigger, False)
        start = time.time()
        end = time.time()
        while GPIO.input(self.pin_echo)==0:
            start = time.time()
        while GPIO.input(self.pin_echo)==1:
            end = time.time()
        duracion = end-start
        distancia = duracion*17150
        return round(distancia, 2)
