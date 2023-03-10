import RPi.GPIO as GPIO

class Sensor:
    def __init__(self, pin):
        self.pin = pin
        
    def configurar_pin(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)
        
    def leer_valor(self):
        pass