import RPi.GPIO as GPIO
import time

class Ultrasonico:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        self.velocidad_sonido = 34300  
        self.tiempo_max = 0.04  
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def medir_distancia(self):
        # enviar pulso de sonido
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)
        
     
        tiempo_inicio = time.time()
        while GPIO.input(self.echo_pin) == 0:
            if time.time() - tiempo_inicio > self.tiempo_max:
                return None
        tiempo_inicio = time.time()
        while GPIO.input(self.echo_pin) == 1:
            if time.time() - tiempo_inicio > self.tiempo_max:
                return None
        tiempo_fin = time.time()
        
     
        duracion = tiempo_fin - tiempo_inicio
        distancia = (duracion * self.velocidad_sonido) / 2
        return distancia

    def configurar_pin(self):
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)