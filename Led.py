from Sensor import Sensor
import RPi.GPIO as GPIO

class Led(Sensor):
    def __init__(self, pin):
        super().__init__(pin)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        GPIO.output(self.pin, False)
        
    def encender(self):
        GPIO.output(self.pin, True)
        
    def apagar(self):
        GPIO.output(self.pin, False)



