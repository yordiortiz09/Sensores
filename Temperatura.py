import Adafruit_DHT
from Sensor import Sensor

class TemperaturaHumedad(Sensor):
    def __init__(self, pin):
        super().__init__(pin)
        
    def leer_valor(self):
        humedad, temperatura = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, self.pin)
        if humedad is not None and temperatura is not None:
            humedad = round(humedad, 2)
            temperatura = round(temperatura, 2)
            return temperatura, humedad
        else:
            return None