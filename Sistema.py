import RPi.GPIO as GPIO
import Ultrasonico
from Temperatura import TemperaturaHumedad
import Temperatura
import Led

class Sistema:
    def __init__(self, led_pins, ultrasonico_pins, temp_hum_pin):
        self.leds = [Led(pin) for pin in led_pins]
        self.ultrasonicos = [Ultrasonico(pin[0], pin[1]) for pin in ultrasonico_pins]
        self.temp_hum = TemperaturaHumedad(temp_hum_pin)
        
    def configurar_sensores(self):
        for led in self.leds:
            led.configurar_pin()
        for ultrasonico in self.ultrasonicos:
            ultrasonico.configurar_pin()
        self.temp_hum.configurar_pin()
        
    def leer_led(self, num_led):
        if num_led >= 0 and num_led < len(self.leds):
            return GPIO.input(self.leds[num_led].pin)
        else:
            return None
        
    def encender_led(self, num_led):
        if num_led >= 0 and num_led < len(self.leds):
            self.leds[num_led].encender()
            
    def apagar_led(self, num_led):
        if num_led >= 0 and num_led < len(self.leds):
            self.leds[num_led].apagar()
            
    def medir_distancia(self, num_ultrasonico):
        if num_ultrasonico >= 0 and num_ultrasonico < len(self.ultrasonicos):
            return self.ultrasonicos[num_ultrasonico].medir_distancia()
        else:
            return None
        
    def medir_temperatura_y_humedad(self):
        return self.temp_hum.med
    
led_pins = [4]
ultrasonico_pins = [(23, 24), (5, 6), (12, 16)]
temp_hum_pin = 18

sistema = Sistema(led_pins, ultrasonico_pins, temp_hum_pin)
sistema.configurar_sensores()
