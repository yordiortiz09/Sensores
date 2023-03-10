import Adafruit_DHT

class TemperaturaHumedad:
    def __init__(self, pin):
        self.pin = pin
        self.sensor = Adafruit_DHT.DHT11
        
    def medir_temperatura_y_humedad(self):
        humedad, temperatura = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humedad is not None and temperatura is not None:
            return {'temperatura': temperatura, 'humedad': humedad}
        else:
            return None
        
    def configurar_pin(self):
        pass